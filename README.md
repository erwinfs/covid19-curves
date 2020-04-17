# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily here: https://www.gov.uk/guidance/coronavirus-covid-19-information-for-the-public

The spreadsheet here does not seem to be public anymore. <https://www.arcgis.com/home/item.html?id=e5fd11150d274bebaaf8fe2a7a2bda11>

Since 10 April positive tests have been divided into pillars. This data set only uses Pillar 1 -  just people that have been hospitalised and most critical key workers,
this ensures consistency with the previous data and is a better indicator for
the last graph.

![Graph of actual cases and exponential curve](./out/cases.png)
![Graph of actual cases and exponential curve](./out/cases-log.png)

The following graph shows the doubling time for new cases (up is good).
This is calculated by fitting an exponential curve up to the each date
and calculating the doubling time from the growth rate.
![Graph of actual cases and exponential curve](./out/casesdt.png)

![Graph of actual cases and exponential deaths](./out/deaths.png)
![Graph of actual cases and exponential deaths](./out/deaths-log.png)

The following graph shows the doubling time for deaths (up is good).
![Graph of actual cases and exponential curve](./out/deathsdt.png)

The following graph shows how the daily cases, offset by the stated number of days,
and  multiplied by the factor (%), mapped against actual deaths reported.
The offset (or lag) and factor are determined by brute force:
It is the combination that produces the lowest error.

![Graph of predicted deaths based on earlier new cases](./out/cases-deaths.png)

Output Details
--------------
<h3>Exponential function coefficients for new cases</h3>
[87.75482099  1.05545171]
<h4>Covariance of coefficients</h4>
[[ 7.53657139e+02 -1.28610846e-01]
 [-1.28610846e-01  2.23337354e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[4.76438189 1.0722312 ]
<h4>Covariance of coefficients</h4>
[[ 3.44945558e+00 -1.07739747e-02]
 [-1.07739747e-02  3.39900217e-05]] <br/>
<h3>Best offset and factor for third graph</h3>
6 20%
<h4>Average Error</h4>
39.86
<br /><br />Last updated on 2020-04-17 14:16:57.757849
