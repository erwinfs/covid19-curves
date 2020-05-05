# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily here: https://www.gov.uk/guidance/coronavirus-covid-19-information-for-the-public

The curves are becoming less relevant every day as the data is fortunately not
following an exponential curve any more.

Since 10 April positive tests have been divided into pillars. This data set only uses Pillar 1 -  just people that have been hospitalised and most critical key workers,
this ensures consistency with the previous data and is a better indicator for
the last graph.
A green line has been added, this shows the exponential curve calculated using
the data up to day 56, about a week after lockdown. This estimates what would
have happened without intervention.

![Graph of actual cases and exponential curve](./out/cases.png)
![Graph of actual cases and exponential curve](./out/cases-log.png)

The following graph shows the doubling time for new cases (up is good).
This is calculated by fitting an exponential curve up to the each date
and calculating the doubling time from the growth rate.
![Graph of actual cases and exponential curve](./out/casesdt.png)

These graphs now show all deaths.
A green line has been added, this shows the exponential curve calculated using
the data up to day 63, about a two weeks after lockdown. This estimates what  
would have happened without intervention.

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
[431.70291774   1.02472225]
<h4>Covariance of coefficients</h4>
[[ 1.28546968e+04 -3.75667054e-01]
 [-3.75667054e-01  1.15959547e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[50.8408738   1.02999843]
<h4>Covariance of coefficients</h4>
[[ 2.40172501e+02 -5.85419880e-02]
 [-5.85419880e-02  1.48378881e-05]] <br/>
<h3>Best offset and factor for third graph</h3>
6 18%
<h4>Average Error</h4>
105.34
<br /><br />Last updated on 2020-05-05 17:43:24.831843
