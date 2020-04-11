# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily here: <https://www.arcgis.com/home/item.html?id=e5fd11150d274bebaaf8fe2a7a2bda11>

Also note the provisos stated here:
<https://www.gov.uk/guidance/coronavirus-covid-19-information-for-the-public#number-of-cases-and-deaths>

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
[24.49638309  1.07959976]
<h4>Covariance of coefficients</h4>
[[ 6.69731060e+01 -4.43270703e-02]
 [-4.43270703e-02  2.96247078e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[0.40575166 1.11622707]
<h4>Covariance of coefficients</h4>
[[ 2.92479885e-02 -1.17930504e-03]
 [-1.17930504e-03  4.77628174e-05]] <br/>
<h3>Best offset and factor for third graph</h3>
7 24%
<h4>Average Error</h4>
23.11
<br /><br />Last updated on 2020-04-11 16:01:36.364103
