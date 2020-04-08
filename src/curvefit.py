
import numpy as np
import pandas as pd
import datetime
import sys
from datetime import timedelta
from scipy.optimize import curve_fit # curve-fit() function imported from scipy
from matplotlib import pyplot as plt

# Constants
DAYOFFSET = 43860 #Excel date for start of the data 31 Jan 2020 for CSV
EXCELDTFACT = 24*60*60*1000000000 # Excel date format conversion factor
EXCELDTOFFSET = 18291 # Excel date for start of the data 31 Jan 2020
LARGENUMBER = 9999999999.9 # Large starting number for err

# Parameters
data_input_fname = "./data/DailyConfirmedCases.xlsx"
output_fname = "./out/fit.md"
#  Number of days to predict for
prediction = 7
# Factor and offset ranges withing which to seek optimum
fact_low = 0.2
fact_high = 0.4
fact_increment = 0.01
offset_low = 5
offset_high = 15
# Day to start plot at
plt_start = 45
# Day to start doubliong time calc and plot
doubling_time_start = 50  # Day to start doubliong time calc and plot

# Test exponential function with coefficients as parameters
def test(x, a, b):
    return a*b**x

# curve_fit() function takes the test-function
# x-data and y-data as argument and returns
# the coefficients a and b in param and
# the estimated covariance of param in param_cov
def exp_fit(cases, days, predicted_days):
    param, param_cov = curve_fit(test, days, cases)

    # ans stores the new y-data according to
    # the coefficients given by curve-fit() function
    Ans = (param[0]*param[1]**predicted_days)
    return Ans, param, param_cov

def doubling_time(cases, days):
    dt = [0.0] * len(days)
    for i in range(doubling_time_start-1,len(days)):
        # create subset, i+1 as this is the number of elements, NOT index
        iteration_cases = cases[0:i+1]
        iteration_days = days[0:i+1]
        #Ans, param, param_cov = exp_fit(cases, caseDays, predicted_days)
        param, param_cov = curve_fit(test, iteration_days, iteration_cases)
        dt[i] = np.log(2)/np.log(param[1])
    return dt

# Test assumption that on average a fraction of people who were diagnosed
# an "offset" number of days ealier, die.
def offset_fit(daily_cases, daily_deaths, days, predicted_days):
    # Iterate over range of offsets and factors - brute force approach
    no_days = len(days)
    predicted_deaths = [0] * no_days
    # Large starting number for error
    lowest_error = LARGENUMBER
    # Calculate error for each number of days in offset range
    for offset in range (offset_low, offset_high):
        fact = fact_low
        # For ech offset day calculate error for each factor
        while fact <= fact_high:
            error = 0
            # Sum error for each day by comparing off-set daily cases
            # with deaths
            for i in range(offset, no_days):
                predicted_deaths[i] = daily_cases[i-offset] * fact
                # Calculate  of error, sq gives less stable results due to
                # exponential nature of data
                # error += abs(predicted_deaths[i] - daily_deaths[i])**2
                error += abs(predicted_deaths[i] - daily_deaths[i])
            if error < lowest_error:
                lowest_error = error
                best_offset = offset
                best_fact = fact
            fact += fact_increment
        #endwhile
    #endfor
    # Make sure that prediction range does not exceed offset
    offset_prediction = min(prediction, best_offset)
    # ans stores the new y-data according to
    # the coefficients given by curve-fit() function
    deaths_ans = [0.0] * (no_days + prediction)
    for i in range(best_offset, no_days + offset_prediction):
        deaths_ans[i] = daily_cases[i-best_offset] * best_fact

    # error = np.sqrt(lowest_error/(no_days-best_ffset))
    error = lowest_error/(no_days-best_offset)
    return deaths_ans, best_offset, best_fact, error

# Read data from Excel spreadsheet and map it into lists
def prep_data():
    # Create a dataframe from xlsx
    df = pd.read_excel(data_input_fname)

    Dates = df["DateVal"].values.tolist()
    #convert dates to day number
    days = [d/EXCELDTFACT - EXCELDTOFFSET for d in Dates]

    daily_cases = df["CMODateCount"].values.tolist()
    daily_cases = np.nan_to_num(daily_cases)      #Replace NaNs with 0

    daily_deaths = df["DailyDeaths"].values.tolist()
    daily_deaths = np.nan_to_num(daily_deaths)    #Replace NaNs with 0

    # Create a new list for days that estimate is to be calculated for
    no_days = len(days)
    predicted_days = days.copy()
    for i in range(no_days, no_days + prediction):
        predicted_days.append(predicted_days[i-1]+1)

    return days, daily_cases, daily_deaths, predicted_days

def main():
    # Open output file, use md format to write to it
    f_out = open(output_fname, "w+")

    # Read data from input file and create lists
    print("Read data ...")
    days, daily_cases, daily_deaths, predicted_days = prep_data()

    print("Fit curve to diagnosed cases ...")
    cases_ans, cases_param, cases_param_cov = exp_fit(daily_cases, days,
                                                        predicted_days)
    print("<h3>Exponential function coefficients for new cases</h3>",
          file=f_out)
    print(cases_param, file=f_out)
    print("<h4>Covariance of coefficients</h4>", file=f_out)
    print(cases_param_cov, file=f_out)

    # Plot results
    plot_title = "Exponential curve fit to UK reported daily cases"
    plt.title(plot_title)
    plt.plot(days, daily_cases, '-', color ='red', label ="Daily cases")
    plt.plot(predicted_days, cases_ans, '--', color ='blue',
             label="Predicted cases")
    plt.legend()
    plt.grid(True)
    plt.xlim([plt_start, len(predicted_days)])
    plt.ylabel("Daily Cases")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/cases.png")
    plt.yscale('log')
    plt.title(plot_title + "\n(logarithmic y-scale)")
    plt.ylabel("Daily Cases (log)")
    plt.savefig("./out/cases-log.png")
    #plt.show()
    plt.close()

    print("Calculate doubling times for new cases...")
    dt = doubling_time(daily_cases, days)
    plot_title = "Doubling time for UK reported daily cases"
    plt.title(plot_title)
    plt.plot(days, dt, '-', color ='red', label ="Doubling time")
    plt.legend()
    plt.grid(True)
    plt.xlim([doubling_time_start, len(days)])
    plt.ylabel("Doubling time in Days")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/casesdt.png")
    plt.close()

    print("Fit curve to new deaths ...")
    deaths_ans, deaths_param, deaths_param_cov = exp_fit(daily_deaths, days,
                                                          predicted_days)
    print("<h3>Exponential function coefficients for daily deaths</h3>",
          file=f_out)
    print(deaths_param,file=f_out)
    print("<h4>Covariance of coefficients</h4>", file=f_out)
    print(deaths_param_cov, "<br/>", file=f_out)

    plot_title = "Exponential curve fit to UK reported daily deaths"
    plt.title(plot_title)
    plt.plot(days, daily_deaths, '-', color ='black', label ="Daily deaths")
    plt.plot(predicted_days, deaths_ans, '--', color ='grey',
             label ="Predicted deaths")
    plt.legend()
    plt.grid(True)
    plt.xlim([plt_start, len(predicted_days)])
    plt.ylabel("Daily Deaths")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/deaths.png")
    plt.yscale('log')
    plt.title(plot_title + "\n(logarithmic y-scale)")
    plt.ylabel("Daily Deaths (log)")
    plt.savefig("./out/deaths-log.png")
    #plt.show()
    plt.close()

    print("Calculate doubling times for deaths...")
    dt = doubling_time(daily_deaths, days)
    plot_title = "Doubling time for UK reported daily deaths"
    plt.title(plot_title)
    plt.plot(days, dt, '-', color ='black', label ="Doubling time")
    plt.legend()
    plt.grid(True)
    plt.xlim([doubling_time_start, len(days)])
    plt.ylabel("Doubling time in Days")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/deathsdt.png")
    plt.close()

    # Estimate best offset and factor to use new daily cases as
    # predictor for deaths
    print("Predict deaths based on new cases ...")
    deaths_ans, offset, fact, error = offset_fit(daily_cases, daily_deaths,
                                                  days, predicted_days)
    print("<h3>Best offset and factor for third graph</h3>", file=f_out)
    print (offset, "{:,.0f}%".format(fact *100), file=f_out)
    #print(bestOffset, bestFact)
    print("<h4>Average Error</h4>", file=f_out)
    print("{:,.2f}".format(error), file=f_out)

    # Plot results
    title =  "Deaths estimated by new cases \n"
    title += "Ofsset by {:,.0f} days ".format(offset)
    title += "and multiplied by {:,.0f}%".format(fact *100)
    plt.title(title)
    plt.plot(days, daily_deaths, '-', color ='black', label ="Daily deaths")
    plt.plot(predicted_days, deaths_ans, '--', color ='grey',
             label ="Predicted deaths")
    plt.legend()
    plt.grid(True)
    plt.xlim([plt_start, len(predicted_days)])
    plt.ylabel("Daily Deaths")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/cases-deaths.png")
    #plt.show()
    plt.close()

    print("<br /><br />Last updated on {}".format(datetime.datetime.now()),
          file=f_out)
    print("Completed on {}".format(datetime.datetime.now()))
    f_out.close()

if __name__ == '__main__':
    main()
