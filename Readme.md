
# Mini Take-Home Project

## Objective

Create a datapipe using NIFI, which allows the ingestion of data from aviationstack api, instantiate a master data set (following the fact model), and perform a simple transformation, creating a view of data. The services will be instantiated with docker-compose.

* Build a docker with the services you think are necessary. The database and the table have to be created when running docker.
  * Services:
    * postgress
    * nifi
    * api (mock data)
    * notebook

* Create a process in [Nifi] that allows obtaining the information from the API.
  - Aviation Data Flows
    - Ingestion Phase
      * Get Data from [AviationStack] API
    - Master Set
      -  Insert the information in the database (Postgres).
    - ETL on Batch Processing
      * Replace the "/" of the arrivalTerminal and departureTimezone fields for " - ". E.g: "Asia/Shanghai" to "Asia - Shanghai"
      * Insert the information in the database (Postgres).
* Create a Jupyter notebook to consume the information stored in the database.
* Show the information in a Pandas dataframe

## What I Learn?

- [Nifi] is a powerfull tool for distribute data, although I not sure if I will choose for production, since the lack of programatic support, like airflow etc.
- Connect Nifi process to 
  - Postgres DB
  - Create a ETL Batch
- Note: The maste repository is not appropiate to be mysql for bigdata.

## Background

### Real-time Flight Status

The [AviationStack] API was built to provide a simple way of accessing global aviation data for real-time and historical flights as well as allow customers to tap into an extensive data set of airline routes and other up-to-date aviation-related information. Requests to the REST API are made using a straightforward HTTP GET URL structure and responses are provided in lightweight JSON format. The objective of this project is to construct an ETL for a client in order to query information from the API, clean it, and store the results into a consumable database.

### Nifi

An easy to use, powerful, and reliable system to process and distribute data. Apache [NiFi] supports powerful and scalable directed graphs of data routing, transformation, and system mediation logic.

## Requirements

* Docker: [how to install](https://docs.docker.com/get-docker/)
  * Docker-Compose: [how to install](https://docs.docker.com/compose/install/)
* Python 3.*
* Docker Images:
  * [apache/nifi](https://hub.docker.com/r/apache/nifi/)
  * [postgres](https://hub.docker.com/_/postgres)
  * [fastApi](https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi)
* JDBC PostgresSQL Driver:
  * Driver required to be provisioned to NIFI instanciances, allowing to connect to progres database
  * [postgresql-42.2.18.jar](https://jdbc.postgresql.org/download.html)
## Environment

*Folder: docker-aviationstak*

* It is based on docker images orchestrated by docker-compose

```
docker-compose -f docker-aviationstak/docker-composer.ym build
docker-compose -f docker-aviationstak/docker-composer.ym up
```


## Links

* NIFI UI:
  * http://127.0.0.1:8080/nifi

* Notebook:
  * http://127.0.0.1:8001

# TODO

* add make as build tool



[AviationStack]: https://aviationstack.com/
[Nifi]: https://nifi.apache.org/