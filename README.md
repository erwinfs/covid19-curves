# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily here: <https://www.arcgis.com/home/item.html?id=e5fd11150d274bebaaf8fe2a7a2bda11>

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
[10.43351215  1.09588078]
<h4>Covariance of coefficients</h4>
[[ 1.47232633e+01 -2.39889122e-02]
 [-2.39889122e-02  3.93690087e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[0.10855973 1.14034246]
<h4>Covariance of coefficients</h4>
[[ 3.52791855e-03 -5.62495651e-04]
 [-5.62495651e-04  8.99846934e-05]] <br/>
<h3>Best offset and factor for third graph</h3>
7 25%
<h4>Average Error</h4>
19.88
<br /><br />Last updated on 2020-04-08 17:26:01.459714
