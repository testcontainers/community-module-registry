---
title: Trino
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/trino/
    maintainer: core
    example: |
      ```java
      var trino = new TrinoContainer(DockerImageName.parse("trinodb/trino:352"));
      trino.start();
      ```
description: |
  Trino is an open-source distributed SQL query engine designed to query large data sets distributed over one or more heterogeneous data sources.
---