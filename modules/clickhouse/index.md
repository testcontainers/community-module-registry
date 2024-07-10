---
title: ClickHouse
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/clickhouse/
    maintainer: core
    example: |
      ```java
      var clickHouseContainer = new ClickHouseContainer();
      clickHouseContainer.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>clickhouse</artifactId>
          <version>1.19.8</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/clickhouse/
    maintainer: core
    example: |
      ```go
      clickHouseContainer, err := clickhouse.Run(ctx, "clickhouse/clickhouse-server:23.3.8.21-alpine")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/clickhouse
      ```
description: |
  ClickHouse is an open-source database management system for analytical processing that allows users to generate reports using SQL queries in real-time.
---