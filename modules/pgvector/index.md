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
  - id: go
    url: https://golang.testcontainers.org/modules/postgres/
    maintainer: core
    example: |
      ```go
      pgVectorContainer, err := postgres.RunContainer(ctx,
        testcontainers.WithImage("pgvector/pgvector:pg16"),
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
      var pgVectorContainer = new PostgreSqlBuilder()
        .WithImage("pgvector/pgvector:pg16")
        .Build();
      pgVectorContainer.StartAsync();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/postgresql/
    maintainer: core
    example: |
      ```javascript
      const container = await new PostgreSqlContainer(image="pgvector/pgvector:pg16").start();
      ```
description: |
  pgvector, open-source vector similarity search for Postgres.
---