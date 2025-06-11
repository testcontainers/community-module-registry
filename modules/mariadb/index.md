---
title: MariaDB
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/mariadb/
    maintainer: core
    example: |
      ```java
      var mariaDB = new MariaDBContainer<>(DockerImageName.parse("mariadb:10.5.5"));
      mariaDB.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>mariadb</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mariadb
    maintainer: core
    example: |
      ```go
      mariaDBContainer, err := mariadb.Run(context.Background(), "mariadb:11.0.3")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/mariadb
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.MariaDb
    maintainer: core
    example: |
      ```csharp
      var mariaDbContainer = new MariaDbBuilder()
        .WithImage("mariadb:10.10")
        .Build();
      await mariaDbContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.MariaDb
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/mariadb/
    maintainer: core
    example: |
      ```javascript
      const container = await new MariaDbContainer("mariadb:11.5.2").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/mariadb --save-dev
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/mariadb/struct.Mariadb.html
    maintainer: community
    example: |
      ```rust
      use testcontainers_modules::{mariadb, testcontainers::runners::SyncRunner};

      let mariadb_instance = mariadb::Mariadb::default().start().unwrap();
      let mariadb_url = format!(
          "mariadb://{}:{}/test",
          mariadb_instance.get_host().unwrap(),
          mariadb_instance.get_host_port_ipv4(3306).unwrap(),
      );
      ```
    installation: |
      ```bash
      cargo add -F mariadb --dev testcontainers-modules
      ```
description: |
  MariaDB is a community-developed, commercially supported fork of the MySQL relational database management system.
---
