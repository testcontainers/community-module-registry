---
title: Timescale
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/postgres/
    maintainer: core
    example: |
      ```java
      var image = DockerImageName.parse("timescale/timescaledb:2.1.0-pg11")
          .asCompatibleSubstituteFor("postgres");
      var timescale = new PostgreSQLContainer(image);
      timescale.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-postgresql</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/postgres/
    maintainer: core
    example: |
      ```go
      timescaleContainer, err := postgres.Run(context.Background(),
        "timescale/timescaledb:2.1.0-pg11",
        postgres.WithDatabase("test"),
        postgres.WithUsername("user"),
        postgres.WithPassword("password"),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/postgres
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.PostgreSql
    maintainer: core
    example: |
      ```csharp
      var timescaleContainer = new PostgreSqlBuilder()
        .WithImage("timescale/timescaledb:2.1.0-pg11")
        .Build();
      await timescaleContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.PostgreSql
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/postgresql/
    maintainer: core
    example: |
      ```javascript
      const container = await new PostgreSqlContainer("timescale/timescaledb:2.1.0-pg11").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/postgresql --save-dev
      ```
description: |
  An open-source time-series SQL database optimized for fast ingest and complex queries. Packaged as a PostgreSQL extension.
---
