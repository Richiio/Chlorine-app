# Chlorine Concentration Sensor Data App
This application demonstrates how one can use Django and InfluxDB (a time series database) to store and manage data from IOT sensors.

The data used in this demonstration was chlorine concentration data recorded via sensors. 
It was obtained from the UCR Time Series Classification Archive as referenced below.

### Directory Structure
```
C:.
│   db.sqlite3
│   manage.py
│   __init__.py
│
├───sensor_app
│   │   admin.py
│   │   apps.py
│   │   models.py
│   │   sensor.py
│   │   tests.py
│   │   views.py
│   │   __init__.py
│   │
│   ├───migrations
│   │   │   __init__.py
│
└───sensor_project
    │   .env
    │   asgi.py
    │   settings.py
    │   urls.py
    │   wsgi.py
    │   __init__.py

```


### Reference
Hoang Anh Dau, Eamonn Keogh, Kaveh Kamgar, Chin-Chia Michael Yeh, Yan Zhu, Shaghayegh Gharghabi , Chotirat Ann Ratanamahatana, Yanping Chen, Bing Hu, Nurjahan Begum, Anthony Bagnall , Abdullah Mueen, Gustavo Batista, & Hexagon-ML (2019). The UCR Time Series Classification Archive. URL https://www.cs.ucr.edu/~eamonn/time_series_data_2018/
