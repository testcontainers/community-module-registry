---
title: InfluxDB
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/influxdb/
    maintainer: core
    example: |
      ```java
      var influx = new InfluxDBContainer<>(DockerImageName.parse("influxdb:2.0.7");
      influx.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/databases/influxdb/
    maintainer: core
    example: |
      ```go
      influxdbContainer, err := influxdb.RunContainer(ctx, testcontainers.WithImage("influxdb:1.8.10"))
      ```
description: |
  InfluxDB is an open-source time series database for storage and retrieval of time series data in fields such as operations monitoring, application metrics, Internet of Things sensor data, and real-time analytics.
---
