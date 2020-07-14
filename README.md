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
<h3>Fit coefficients for new cases</h3>
[1.47572623e+05 9.66009373e-01]
<h4>Standard deviation errors on the parameters</h4>
[7.77659102e+03 4.54164488e-04]
<h3>Fit coefficients for daily deaths</h3>
[8.72255925e+03 9.72060961e-01]
<h4>Standard deviation errors on the parameters</h4>
[3.05304394e+02 3.61953183e-04] <br/>
<h3>Best offset and factor for third graph</h3>
4 13%
<h4>Average Error</h4>
65.48
<br /><br />Last updated on 2020-07-14 11:11:14.328429
