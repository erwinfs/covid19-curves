# UK COVID-19 Curves

This project contains some Python code that fits exponential curves to
official UK COVID-19 data that is released daily.

![Graph of actual cases and exponential curve](cases.png)
![Graph of actual cases and exponential curve](cases-log.png)
![Graph of actual cases and exponential deaths](deaths.png)
![Graph of actual cases and exponential deaths](deaths-log.png)

The following graph shows how the daily cases, offset by the stated number of days,
and  multiplied by the factor (%), mapped against actual deaths reported.
The offset (or lag) and factor are determined by brute force:
It is the combination that produces the lowest error.

![Graph of predicted deaths based on earlier new cases](cases-deaths.png)

Output Details
--------------
