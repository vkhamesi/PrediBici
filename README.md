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
<img src="https://github.com/vkhamesi/PrediBici/blob/main/citystations.png" width="100%">

This is what raw data looks like as a CSV file :
<img src="https://github.com/vkhamesi/PrediBici/blob/main/citystations.png" width="40%">
