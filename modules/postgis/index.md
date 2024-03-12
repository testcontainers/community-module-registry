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
  - id: go
    url: https://golang.testcontainers.org/modules/postgres/
    maintainer: core
    example: |
      ```go
      postgisContainer, err := postgres.RunContainer(ctx,
        testcontainers.WithImage("postgis/postgis:12-3.0"),
        postgres.WithDatabase("test"),
        postgres.WithUsername("user"),
        postgres.WithPassword("password"),
      )
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.PostgreSql
    maintainer: core
    example: |
      ```csharp
      var postgisContainer = new PostgreSqlBuilder()
        .WithImage("postgis/postgis:12-3.0")
        .Build();
      postgisContainer.StartAsync();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/postgresql/
    maintainer: core
    example: |
      ```javascript
      const container = await new PostgreSqlContainer(image = "postgis/postgis:12-3.0").start();
      ```
description: |
  PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.
---