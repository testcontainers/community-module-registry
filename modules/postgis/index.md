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
      postgisContainer, err := postgres.Run(context.Background(),
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
      dotnet add package Testcontainers.PostgreSql
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/postgresql/
    maintainer: core
    example: |
      ```javascript
      const container = await new PostgreSqlContainer("postgis/postgis:12-3.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/postgresql --save-dev
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/postgres/struct.Postgres.html
    maintainer: community
    example: |
      ```rust
      use testcontainers::core::ImageExt;
      use testcontainers_modules::{postgres, testcontainers::runners::SyncRunner};

      let postgres_instance = postgres::Postgres::default().with_name("postgis/postgis").with_tag("16-3.5-alpine").start().unwrap();

      let connection_string = format!(
          "postgres://postgres:postgres@{}:{}/postgres",
          postgres_instance.get_host().unwrap(),
          postgres_instance.get_host_port_ipv4(5432).unwrap()
      );
      ```
    installation: |
      ```bash
      cargo add -F postgres --dev testcontainers-modules
      ```
description: |
  PostGIS extends the capabilities of the PostgreSQL relational database by adding support for storing, indexing, and querying geospatial data.
---
