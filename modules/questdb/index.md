---
title: QuestDB
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/questdb/
    maintainer: core
    example: |
      ```java
      var questdb = new QuestDBContainer(DockerImageName.parse("questdb/questdb:6.5.3"));
      questdb.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-questdb</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/questdb/
    maintainer: core
    example: |
      ```go
      questdbContainer, err := questdb.Run(context.Background(), "questdb/questdb:7.3.10")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/questdb
      ```

description: |
  QuestDB is an open-source time-series database for high throughput ingestion and fast SQL queries with operational simplicity. It supports schema-agnostic ingestion using the InfluxDB line protocol, PostgreSQL wire protocol, and a REST API for bulk imports and exports.
---
