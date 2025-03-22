---
title: pgvector
categories:
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/postgres/
    maintainer: core
    example: |
      ```java
      var image = DockerImageName.parse("pgvector/pgvector:pg16")
          .asCompatibleSubstituteFor("postgres");
      var pgVector = new PostgreSQLContainer<>(image);
      pgVector.start();
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
      pgVectorContainer, err := postgres.Run(ctx,
        "pgvector/pgvector:pg16",
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
      var pgVectorContainer = new PostgreSqlBuilder()
        .WithImage("pgvector/pgvector:pg16")
        .Build();
      await pgVectorContainer.StartAsync();
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
      const container = await new PostgreSqlContainer("pgvector/pgvector:pg16").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/postgresql --save-dev
      ```
description: |
  pgvector, open-source vector similarity search for Postgres.
---
