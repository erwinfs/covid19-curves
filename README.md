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
[9.57078074 1.09755694]
<h4>Covariance of coefficients</h4>
[[ 1.47358207e+01 -2.65935821e-02]
 [-2.65935821e-02  4.83395490e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[0.10970844 1.14014346]
<h4>Covariance of coefficients</h4>
[[ 0.00460978 -0.00073811]
 [-0.00073811  0.00011859]] <br/>
<h3>Best offset and factor for third graph</h3>
7 26%
<h4>Average Error</h4>
17.61
<br /><br />Last updated on 2020-04-07 18:57:15.535710
