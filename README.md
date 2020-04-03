# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily here: <https://www.arcgis.com/home/item.html?id=e5fd11150d274bebaaf8fe2a7a2bda11>

![Graph of actual cases and exponential curve](./out/cases.png)
![Graph of actual cases and exponential curve](./out/cases-log.png)
![Graph of actual cases and exponential deaths](./out/deaths.png)
![Graph of actual cases and exponential deaths](./out/deaths-log.png)

The following graph shows how the daily cases, offset by the stated number of days,
and  multiplied by the factor (%), mapped against actual deaths reported.
The offset (or lag) and factor are determined by brute force:
It is the combination that produces the lowest error.

![Graph of predicted deaths based on earlier new cases](./out/cases-deaths.png)

Output Details
--------------
<h3>Exponential function coefficients for new cases</h3>
[1.25182293 1.13783816]
<h4>Covariance of coefficients</h4>
[[ 1.38840531e-01 -2.07406322e-03]
 [-2.07406322e-03  3.11090631e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[5.44821942e-04 1.24617849e+00]
<h4>Covariance of coefficients</h4>
[[ 9.18262635e-08 -3.37266110e-06]
 [-3.37266110e-06  1.24036188e-04]] <br/>
<h3>Best offset and factor for third graph</h3>
7 25%
<h4>Average Error</h4>
13.26
