# Introduction and Goals

This project analysis Twitter data concerning the sentiment of tweet in Germany and compares the data to cases of COVID-19 in Germany. Furthermore, this application displays the political and epidemical situation in Germany in 2020. To just use the application visit [covidioten.app](https://covidioten.app/#/polit).
This is only the repository where the data analysis is stored. For the Frontend visit the [UI repository](https://github.com/Covidioten/UI). 
The Webserver Backend is stored in [webserver repository](https://github.com/Covidioten/WebServer).

# Execution instructions

Instructions:
Define FLASK_APP ENV variable to set config:
```
export FLASK_APP=project
```

Start flask server:
```
flask run
```

To add data points manually, send a GET request to /data-point/from-file

To add news entries manually, send a GET request to /news/from-file


Testing:
`pytest`


# Architecture Constraints

Hadoop should be used


## Business Context
Political decisions have an influence on the sentiment of a country
To research the impact of these decisions on the sentiment we analyze the correlation between the calculated sentiment and political statements and actions.
