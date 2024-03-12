---
title: Presto
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/presto/
    maintainer: core
    example: |
      ```java
      var presto = new PrestoContainer(DockerImageName.parse("ghcr.io/trinodb/presto:344"));
      presto.start();
      ```
description: |
  Presto is a distributed query engine for big data using the SQL query language. Its architecture allows users to query data sources such as Hadoop, Cassandra, Kafka, AWS S3, Alluxio, MySQL, MongoDB and Teradata, and allows use of multiple data sources within a query.
---