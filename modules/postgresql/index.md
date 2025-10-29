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
      var postgres = new PostgreSQLContainer(DockerImageName.parse("postgres:16-alpine"));
      postgres.start();
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
      postgresContainer, err := postgres.Run(context.Background(),
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
      dotnet add package Testcontainers.PostgreSql
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/postgresql/
    maintainer: core
    example: |
      ```javascript
      const container = await new PostgreSqlContainer("postgres:13.3-alpine").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/postgresql --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/postgres/README.html
    maintainer: core
    example: |
      ```python
      with PostgresContainer("postgres:16") as postgres:
          engine = sqlalchemy.create_engine(postgres.get_connection_url())
      ```
    installation: |
      ```bash
      pip install testcontainers[postgres]
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/postgres/struct.Postgres.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::postgres::Postgres::default().start()
      ```
    installation: |
      ```bash
      cargo add -F postgres --dev testcontainers-modules
      ```
description: |
  PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance.
---
