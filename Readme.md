
# Mini Take-Home Project

## Objective: 

* Build a docker with the services you think are necessary. The database and the table have to be created when running docker.
* Create a process in Nifi that allows obtaining the information from the API.
* Replace the "/" of the arrivalTerminal and departureTimezone fields for " - ". E.g: "Asia/Shanghai" to "Asia - Shanghai"
* Insert the information in the database.
* Create a Jupyter notebook to consume the information stored in the database.
* Show the information in a Pandas dataframe

## Background

### Real-time Flight Status

The [AviationStack] API was built to provide a simple way of accessing global aviation data for real-time and historical flights as well as allow customers to tap into an extensive data set of airline routes and other up-to-date aviation-related information. Requests to the REST API are made using a straightforward HTTP GET URL structure and responses are provided in lightweight JSON format. The objective of this project is to construct an ETL for a client in order to query information from the API, clean it, and store the results into a consumable database.

### Nifi

An easy to use, powerful, and reliable system to process and distribute data. Apache [NiFi] supports powerful and scalable directed graphs of data routing, transformation, and system mediation logic.


[AviationStack]: https://aviationstack.com/
[Nifi]: https://nifi.apache.org/