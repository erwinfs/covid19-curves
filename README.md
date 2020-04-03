# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily here: <https://www.arcgis.com/home/item.html?id=e5fd11150d274bebaaf8fe2a7a2bda11>

![Graph of actual cases and exponential curve](./out/cases.png)
![Graph of actual cases and exponential curve](./out/cases-log.png)
![Graph of actual cases and exponential deaths](./outdeaths.png)
![Graph of actual cases and exponential deaths](./outdeaths-log.png)

The following graph shows how the daily cases, offset by the stated number of days,
and  multiplied by the factor (%), mapped against actual deaths reported.
The offset (or lag) and factor are determined by brute force:
It is the combination that produces the lowest error.

![Graph of predicted deaths based on earlier new cases](./outcases-deaths.png)

Output Details
--------------
<h3>Exponential function coefficients for new cases</h3>
[0.86671959 1.14534482]
<h4>Covariance of coefficients</h4>
[[ 7.88729346e-02 -1.73673300e-03]
 [-1.73673300e-03  3.83860938e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[2.48642233e-04 1.26271377e+00]
<h4>Covariance of coefficients</h4>
[[ 2.96783119e-08 -2.45495817e-06]
 [-2.45495817e-06  2.03315216e-04]] <br/>
<h3>Best offset and factor for third graph</h3>
7 26%
<h4>Average Error</h4>
12.59
