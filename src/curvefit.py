
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit # curve-fit() function imported from scipy
from matplotlib import pyplot as plt

# Constants
DAYOFFSET = 43860 #Excel date for start of the data 31 Jan 2020 for CSV
EXCELDTFACT = 24*60*60*1000000000 # Excel date format conversion factor
EXCELDTOFFSET = 18291 # Excel date for start of the data 31 Jan 2020
LARGENUMBER = 9999999999.9 # Large starting number for error


# Parameters
prediction = 5 #  Number of days to predict for
# Factor and offset ranges withing which to seek optimum
factLow = 0.2
factHigh = 0.4
factIncrement = 0.01
offsetLow = 5
offsetHigh = 15

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
                # Calculate square of error
                error += abs(PredictedDeaths[i] - DailyDeaths[i])**2
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

    error = np.sqrt(lowestError/(noDays-bestOffset))
    return DeathsAns, bestOffset, bestFact, error

# Read data from Excel spreadsheet and map it into lists
def prep_data():
    # Create a dataframe from xlsx
    df = pd.read_excel('DailyConfirmedCases.xlsx')

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
    print("Exponential funcion coefficients for new cases:")
    print(CasesParam)
    print("Covariance of coefficients:")
    print(CasesParam_cov)

    # Plot results
    plt.title("Exponential curve fit to UK reported daily cases")
    plt.plot(Days, DailyCases, '-', color ='red', label ="Daily cases")
    plt.plot(pDays, CasesAns, '--', color ='blue', label ="Predicted cases")
    plt.legend()
    plt.ylabel("Cases")
    plt.xlabel("Days since 31 january 2020")
    plt.savefig("cases.png")
    plt.show()
    plt.close()

    DeathsAns, DeathsParam, DeathsParam_cov = exp_fit(DailyDeaths, Days, pDays)
    print("Exponential funcion coefficients for daily deaths:")
    print(DeathsParam)
    print("Covariance of coefficients:")
    print(DeathsParam_cov)

    plt.title("Exponential curve fit to UK reported daily deaths")
    plt.plot(Days, DailyDeaths, '-', color ='black', label ="Daily deaths")
    plt.plot(pDays, DeathsAns, '--', color ='grey', label ="Predicted deaths")
    plt.legend()
    plt.ylabel("Deaths")
    plt.xlabel("Days since 31 january 2020")
    plt.savefig("deaths.png")
    plt.show()
    plt.close()

    # Estimate best offset and factor to use new daily cases as
    # predictor for deaths
    DeathsAns, offset, fact, error = offset_fit(DailyCases, DailyDeaths, Days, pDays)
    print("Best offset and factor")
    print (offset, "{:,.0f}%".format(fact *100))
    #print(bestOffset, bestFact)
    print("Average Error")
    print("{:,.2f}".format(error))

    # Plot results
    title =  "Deaths estimated by new cases \n"
    title += "Ofsset by {:,.0f} days ".format(offset)
    title += "and multiplied by {:,.0f}%".format(fact *100)
    plt.title(title)
    plt.plot(Days, DailyDeaths, '-', color ='black', label ="Daily deaths")
    plt.plot(pDays, DeathsAns, '--', color ='grey', label ="Predicted deaths")
    plt.legend()
    plt.ylabel("Deaths")
    plt.xlabel("Days since 31 january 2020")
    plt.savefig("cases-deaths.png")
    plt.show()
    plt.close()

if __name__ == '__main__':
    main()