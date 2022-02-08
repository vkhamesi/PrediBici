# PrediBici
Project carried out as part of an innovation week at École Centrale de Lyon.

This educational project focused on the ergonomics of deploying a network of self-service bicycles in Mexico City. The idea developed here is to retrieve raw data available in open source as CSV files on the website <a href="url">https://www.ecobici.cdmx.gob.mx</a>, then to exploit them. 

The raw data are signals sent by the city's self-service bicycle stations to a server. These signals contain the information :
<ul>
  <li>user's gender</li>
  <li>user's age</li>
  <li>bike's ID</li>
  <li>bikes station of departure ID</li>
  <li>departure date</li>
  <li>departure time</li>
  <li>bikes station of arrival ID</li>
  <li>arrival date</li>
  <li>arrival time</li>
</ul>

These data made it possible to carry out a <b>descriptive statistical study</b> of the users of this service (gender, age and habits) but also the flow of bikes within the city. The purpose of this project was then to develop a program that takes as arguments a station ID and a date, and returns the <b>evolution of the number of bikes</b> in the station as a function of the time on that day in that given station. Finally, from these built time series, the idea was to develop a <b>predictive model</b> using exponential moving averages (Holt-Winters) models, and also autoregressive integrated moving average (ARIMA). These models could predict the evolution in the near future of the number of bicycles available at a station, and therefore also of the number of parking spaces available in a station, so that Ecobici users could plan an optimized route and don't have to look too long for a bike or any available parking space.

The following image shows Ecobici stations in Mexico City :

<img src="https://github.com/vkhamesi/PrediBici/blob/main/citystations.png" width="50%" class="center">

This is what raw data looks like as a CSV file :
```
F;32;11584;452;01/07/2019;0:01:35;312;01/07/2019;0:29:28
M;19;10219;136;01/07/2019;0:02:47;133;01/07/2019;0:13:35
M;28;11496;180;01/07/2019;0:02:54;348;01/07/2019;0:13:58
M;44;11948;181;01/07/2019;0:03:01;291;01/07/2019;0:39:25
M;24;8112;18;01/07/2019;0:04:45;111;01/07/2019;0:17:33
```

By processing these data, we can trace the evolution of the number of bikes in a given station on a given day, and compute moving averages to smooth the evolution. The x-axis is in unit of time, and the total duration is from midnight to midnight. 

<img src="https://github.com/vkhamesi/PrediBici/blob/main/timeseries.png" width="60%" class="center">

<img src="https://github.com/vkhamesi/PrediBici/blob/main/movingaverages.png" width="70%" class="center">

Finally, we tried to predict the evolution of bikes within a station. These predictions rely on parameters (especially for the ARIMA model, check https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average for more details).

<img src="https://github.com/vkhamesi/PrediBici/blob/main/predictions.png" width="70%" class="center">

