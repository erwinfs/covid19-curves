# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily.

![Graph of actual cases and exponential curve](cases.png)
![Graph of actual cases and exponential deaths](deaths.png)

The following graph shows how the daily cases, offset by the stated number of days,
and  multiplied by the factor (%), map against actual deaths reported.
The offset (or lag) and factor are determined by brute force:
It is the combination that produces the lowest error.

![Graph of predicted deaths based on earlier new cases](cases-deaths.png)

Output Details
--------------
<h2>Exponential function coefficients for new cases:</h2><br/> 
[0.68559076 1.1502348 ] <br/>
<h2>Covariance of coefficients:</h2><br/> 
[[ 1.26549610e-01 -3.59215570e-03]
 [-3.59215570e-03  1.02333242e-04]] <br/><br/>
<h2>Exponential function coefficients for daily deaths:</h2><br/> 
[6.96579902e-05 1.29024605e+00] <br/> 
<h2>Covariance of coefficients:</h2><br/> 
[[ 7.66788961e-09 -2.34440786e-06]
 [-2.34440786e-06  7.17525515e-04]] <br/> <br/> 
<h2>Best offset and factor for third graph</h2><br/> 
7 25% <br/> 
<h2>Average Error</h2><br/> 
27.05
