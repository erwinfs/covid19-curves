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
[32.18197075  1.07445225]
<h4>Covariance of coefficients</h4>
[[ 1.13018375e+02 -5.60893638e-02]
 [-5.60893638e-02  2.81398202e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[0.84857741 1.10298867]
<h4>Covariance of coefficients</h4>
[[ 1.44611542e-01 -2.73266165e-03]
 [-2.73266165e-03  5.19243122e-05]] <br/>
<h3>Best offset and factor for third graph</h3>
7 22%
<h4>Average Error</h4>
32.02
<br /><br />Last updated on 2020-04-12 16:02:51.572943
