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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>trino</artifactId>
          <version>1.19.8</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Trino is an open-source distributed SQL query engine designed to query large data sets distributed over one or more heterogeneous data sources.
---