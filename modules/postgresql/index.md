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
      var postgres = new PostgreSQLContainer<>(DockerImageName.parse("postgres:16-alpine"));
      postgres.start();
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
      postgresContainer, err := postgres.Run(ctx,
        "postgres:16-alpine",
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
      var postgreSqlContainer = new PostgreSqlBuilder()
        .WithImage("postgres:16")
        .Build();
      await postgreSqlContainer.StartAsync();
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
      const container = await new PostgreSqlContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/postgresql --save-dev
      ```
description: |
  PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.
---