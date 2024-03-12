---
title: PostgreSQL
categories:
  - relational-database
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/postgres/
    maintainer: core
    example: |
      ```java
      var postgres = new PostgreSQLContainer<>(DockerImageName.parse("postgres:9.6.12"));
      postgres.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/postgres/
    maintainer: core
    example: |
      ```go
      postgresContainer, err := postgres.RunContainer(ctx,
        testcontainers.WithImage("postgres:9.6"),
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
      var postgreSqlContainer = new PostgreSqlBuilder()
        .WithImage("postgres:15.1")
        .Build();
      postgreSqlContainer.StartAsync();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/postgresql/
    maintainer: core
    example: |
      ```javascript
      const container = await new PostgreSqlContainer().start();
      ```
description: |
  PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.
---