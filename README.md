# UK COVID-19 Curves

Since 13 July the data was refreshed retrospectively to now contain all positive tests and all deaths.
This was done due to changes in reporting.

Given the reporting dip every weekend the script now uses a moving 7 day moving average.

This project contains some Python code that used to fit exponential curves to
official UK COVID-19 data that is released daily here: https://www.gov.uk/guidance/coronavirus-covid-19-information-for-the-public

A green line has been added, this shows the exponential curve calculated using
the data up to day 65, the peak. This estimates what would
have happened without intervention.

![Graph of actual cases and exponential curve](./out/cases.png)
![Graph of actual cases and exponential curve](./out/cases-log.png)

These graphs now show all deaths.
A green line has been added, this shows the exponential curve calculated using
the data up to day 71, the peak. This estimates what  
would have happened without intervention.

![Graph of actual cases and exponential deaths](./out/deaths.png)
![Graph of actual cases and exponential deaths](./out/deaths-log.png)

The following graph shows how the daily cases, offset by the stated number of days,
and  multiplied by the factor (%), mapped against actual deaths reported.
The offset (or lag) and factor are determined by brute force:
It is the combination that produces the lowest error. The switch to all positive
tests, rather than just Pillar 1 has made this approach less accurate.

![Graph of predicted deaths based on earlier new cases](./out/cases-deaths.png)

Output Details
--------------
<h3>Line coefficients for new cases</h3>
[3.31434559e+04 9.78183748e-01]
<h4>Covariance of coefficients</h4>
[[ 8.51948864e+06 -2.51114556e+00]
 [-2.51114556e+00  7.68418015e-07]] [2.91881631e+03 8.76594556e-04]
<h3>Fit coefficients for daily deaths</h3>
[8.72255925e+03 9.72060961e-01]
<h4>Covariance of coefficients</h4>
[[ 9.32107729e+04 -1.08859637e-01]
 [-1.08859637e-01  1.31010107e-07]] <br/>
<h3>Best offset and factor for third graph</h3>
4 13%
<h4>Average Error</h4>
65.48
<br /><br />Last updated on 2020-07-14 10:16:59.663851
