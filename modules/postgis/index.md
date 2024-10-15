---
title: PostGIS
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/postgres/
    maintainer: core
    example: |
      ```java
      var image = DockerImageName.parse("postgis/postgis:12-3.0")
          .asCompatibleSubstituteFor("postgres");
      var postgis = new PostgreSQLContainer<>(image);
      postgis.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>postgresql</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/postgres/
    maintainer: core
    example: |
      ```go
      postgisContainer, err := postgres.Run(ctx,
        "postgis/postgis:12-3.0",
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
      var postgisContainer = new PostgreSqlBuilder()
        .WithImage("postgis/postgis:12-3.0")
        .Build();
      await postgisContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.PostgreSql --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/postgresql/
    maintainer: core
    example: |
      ```javascript
      const container = await new PostgreSqlContainer(image = "postgis/postgis:12-3.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/postgresql --save-dev
      ```
description: |
  PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.
---
