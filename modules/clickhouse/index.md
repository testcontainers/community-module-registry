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
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/clickhouse/
    maintainer: core
    example: |
      ```go
      clickHouseContainer, err := clickhouse.Run(context.Background(), "clickhouse/clickhouse-server:23.3.8.21-alpine")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/clickhouse
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.ClickHouse
    maintainer: core
    example: |
      ```csharp
      var clickHouseContainer = new ClickHouseBuilder()
        .WithImage("clickhouse/clickhouse-server:23.6-alpine")
        .Build();
      await clickHouseContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.ClickHouse
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/clickhouse/README.html
    maintainer: core
    example: |
      ```python
      with ClickHouseContainer("clickhouse/clickhouse-server:21.8") as clickhouse:
          client = clickhouse_driver.Client.from_url(clickhouse.get_connection_url())
          client.execute("select 'working'")
      ```
    installation: |
      ```bash
      pip install testcontainers[clickhouse]
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/clickhouse/struct.ClickHouse.html
    maintainer: community
    example: |
      ```rust
      use testcontainers_modules::{clickhouse, testcontainers::runners::SyncRunner};

      let clickhouse = clickhouse::ClickHouse::default().start().unwrap();
      let http_port = clickhouse.get_host_port_ipv4(8123).unwrap();

      // do something with the started clickhouse instance..
      ```
    installation: |
      ```bash
      cargo add -F clickhouse --dev testcontainers-modules
      ```
description: |
  ClickHouse is an open-source database management system for analytical processing that allows users to generate reports using SQL queries in real-time.
---
