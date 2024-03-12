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
  - id: go
    url: https://golang.testcontainers.org/modules/clickhouse/
    maintainer: core
    example: |
      ```go
      clickHouseContainer, err := clickhouse.RunContainer(ctx, testcontainers.WithImage("clickhouse/clickhouse-server:23.3.8.21-alpine"))
      ```
description: |
  ClickHouse is an open-source database management system for analytical processing that allows users to generate reports using SQL queries in real-time.
---