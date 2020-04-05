
import numpy as np
import pandas as pd
import datetime
from datetime import timedelta
from scipy.optimize import curve_fit # curve-fit() function imported from scipy
from matplotlib import pyplot as plt

# Constants
DAYOFFSET = 43860 #Excel date for start of the data 31 Jan 2020 for CSV
EXCELDTFACT = 24*60*60*1000000000 # Excel date format conversion factor
EXCELDTOFFSET = 18291 # Excel date for start of the data 31 Jan 2020
LARGENUMBER = 9999999999.9 # Large starting number for err
pltStart = 45 # Day to start plot at


# Parameters
fileName = "./data/DailyConfirmedCases.xlsx"
prediction = 5 #  Number of days to predict for
# Factor and offset ranges withing which to seek optimum
factLow = 0.2
factHigh = 0.4
factIncrement = 0.01
offsetLow = 5
offsetHigh = 15
pltStart = 45 # Day to start plot at
doublingTimeStart = 50  # Day to start doubliong time calc and plot

# Test exponential function with coefficients as parameters
def test(x, a, b):
    return a*b**x

# curve_fit() function takes the test-function
# x-data and y-data as argument and returns
# the coefficients a and b in param and
# the estimated covariance of param in param_cov
def exp_fit(DailyCases, Days, pDays):
    Param, Param_cov = curve_fit(test, Days, DailyCases)

    # ans stores the new y-data according to
    # the coefficients given by curve-fit() function
    Ans = (Param[0]*Param[1]**pDays)
    return Ans, Param, Param_cov

def doubling_time(DailyCases, Days):
    dt = [0.0] * len(Days)
    for i in range(doublingTimeStart-1,len(Days)):
        cases = DailyCases[0:i]
        caseDays = Days[0:i]
        #Ans, Param, Param_cov = exp_fit(cases, caseDays, pDays)
        Param, Param_cov = curve_fit(test, caseDays, cases)
        dt[i] = np.log(2)/np.log(Param[1])
    return dt


# Test assumption that on average a fraction of people who were diagnosed
# an "offset" number of days ealier, die.
def offset_fit(DailyCases, DailyDeaths, Days, pDays):
    # Iterate over range of offsets and factors - brute force approach
    noDays = len(Days)
    PredictedDeaths = [0] * noDays
    # Large starting number for error
    lowestError = LARGENUMBER
    # Calculate error for each number of days in offset range
    for offset in range (offsetLow, offsetHigh):
        fact = factLow
        # For ech offset day calculate error for each factor
        while fact <= factHigh:
            error = 0
            # Sum error for each day by comparing off-set daily cases
            # with deaths
            for i in range(offset, noDays):
                PredictedDeaths[i] = DailyCases[i-offset] * fact
                # Calculate  of error, sq gives less stable results due to
                # exponential nature of data
                # error += abs(PredictedDeaths[i] - DailyDeaths[i])**2
                error += abs(PredictedDeaths[i] - DailyDeaths[i])
            if error < lowestError:
                lowestError = error
                bestOffset = offset
                bestFact = fact
            fact += factIncrement
        #endwhile
    #endfor

    # ans stores the new y-data according to
    # the coefficients given by curve-fit() function
    DeathsAns = [0.0] * (noDays + prediction)
    for i in range(bestOffset, noDays + prediction):
        DeathsAns[i] = DailyCases[i-bestOffset] * bestFact

    # error = np.sqrt(lowestError/(noDays-bestOffset))
    error = lowestError/(noDays-bestOffset)
    return DeathsAns, bestOffset, bestFact, error

# Read data from Excel spreadsheet and map it into lists
def prep_data():
    # Create a dataframe from xlsx
    df = pd.read_excel(fileName)

    Dates = df["DateVal"].values.tolist()
    Days = [d/EXCELDTFACT - EXCELDTOFFSET for d in Dates] #convert dates to day number

    DailyCases = df["CMODateCount"].values.tolist()
    DailyCases = np.nan_to_num(DailyCases)      #Replace NaNs with 0

    DailyDeaths = df["DailyDeaths"].values.tolist()
    DailyDeaths = np.nan_to_num(DailyDeaths)    #Replace NaNs with 0

    # Create a new list for days that estimate is to be calculated for
    noDays = len(Days)
    pDays = Days.copy()

    for i in range(noDays, noDays + prediction):
        pDays.append(pDays[i-1]+1)

    return Days, DailyCases, DailyDeaths, pDays

def main():
    # Read data from input file and create lists
    Days, DailyCases, DailyDeaths, pDays = prep_data()

    CasesAns, CasesParam, CasesParam_cov = exp_fit(DailyCases, Days, pDays)
    print("<h3>Exponential function coefficients for new cases</h3>")
    print(CasesParam,)
    print("<h4>Covariance of coefficients</h4>")
    print(CasesParam_cov)

    # Plot results
    plotTitle = "Exponential curve fit to UK reported daily cases"
    plt.title(plotTitle)
    plt.plot(Days, DailyCases, '-', color ='red', label ="Daily cases")
    plt.plot(pDays, CasesAns, '--', color ='blue', label ="Predicted cases")
    plt.legend()
    plt.xlim([pltStart, len(pDays)])
    plt.ylabel("Daily Cases")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/cases.png")
    plt.yscale('log')
    plt.title(plotTitle + "\n(logarithmic y-scale)")
    plt.ylabel("Daily Cases (log)")
    plt.savefig("./out/cases-log.png")
    #plt.show()
    plt.close()

    dt = doubling_time(DailyCases, Days)
    plotTitle = "Doubling time for UK reported daily cases"
    plt.title(plotTitle)
    plt.plot(Days, dt, '-', color ='red', label ="Doubling time")
    plt.legend()
    plt.xlim([doublingTimeStart, len(Days)])
    plt.ylabel("Doubling time")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/casesdt.png")
    plt.close()

    DeathsAns, DeathsParam, DeathsParam_cov = exp_fit(DailyDeaths, Days, pDays)
    print("<h3>Exponential function coefficients for daily deaths</h3>")
    print(DeathsParam,)
    print("<h4>Covariance of coefficients</h4>")
    print(DeathsParam_cov, "<br/>")

    plotTitle = "Exponential curve fit to UK reported daily deaths"
    plt.title(plotTitle)
    plt.plot(Days, DailyDeaths, '-', color ='black', label ="Daily deaths")
    plt.plot(pDays, DeathsAns, '--', color ='grey', label ="Predicted deaths")
    plt.legend()
    plt.xlim([pltStart, len(pDays)])
    plt.ylabel("Daily Deaths")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/deaths.png")
    plt.yscale('log')
    plt.title(plotTitle + "\n(logarithmic y-scale)")
    plt.ylabel("Daily Deaths (log)")
    plt.savefig("./out/deaths-log.png")
    #plt.show()
    plt.close()

    dt = doubling_time(DailyDeaths, Days)
    plotTitle = "Doubling time for UK reported daily deaths"
    plt.title(plotTitle)
    plt.plot(Days, dt, '-', color ='black', label ="Doubling time")
    plt.legend()
    plt.xlim([doublingTimeStart, len(Days)])
    plt.ylabel("Doubling time")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/deathsdt.png")
    plt.close()

    # Estimate best offset and factor to use new daily cases as
    # predictor for deaths
    DeathsAns, offset, fact, error = offset_fit(DailyCases, DailyDeaths, Days, pDays)
    print("<h3>Best offset and factor for third graph</h3>")
    print (offset, "{:,.0f}%".format(fact *100))
    #print(bestOffset, bestFact)
    print("<h4>Average Error</h4>")
    print("{:,.2f}".format(error))

    # Plot results
    title =  "Deaths estimated by new cases \n"
    title += "Ofsset by {:,.0f} days ".format(offset)
    title += "and multiplied by {:,.0f}%".format(fact *100)
    plt.title(title)
    plt.plot(Days, DailyDeaths, '-', color ='black', label ="Daily deaths")
    plt.plot(pDays, DeathsAns, '--', color ='grey', label ="Predicted deaths")
    plt.legend()
    plt.xlim([pltStart, len(pDays)])
    plt.ylabel("Daily Deaths")
    plt.xlabel("Days since 31 January 2020")
    plt.savefig("./out/cases-deaths.png")
    #plt.show()
    plt.close()

    print("<br /><br />Last updated on {}".format(datetime.datetime.now()))

if __name__ == '__main__':
    main()
