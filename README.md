# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily here: https://www.gov.uk/guidance/coronavirus-covid-19-information-for-the-public

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
[214.99772345   1.03851441]
<h4>Covariance of coefficients</h4>
[[ 3.53626014e+03 -2.25826560e-01]
 [-2.25826560e-01  1.48599925e-05]]
<h3>Exponential function coefficients for daily deaths</h3>
[20.13678394  1.04679208]
<h4>Covariance of coefficients</h4>
[[ 4.67812461e+01 -3.15199827e-02]
 [-3.15199827e-02  2.16708509e-05]] <br/>
<h3>Best offset and factor for third graph</h3>
6 18%
<h4>Average Error</h4>
91.18
<br /><br />Last updated on 2020-04-25 18:00:31.857697
