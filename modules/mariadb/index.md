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
      mariaDBContainer, err := mariadb.Run(ctx, "mariadb:11.0.3")
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
      dotnet add package Testcontainers.MariaDb --version 3.9.0
      ```
description: |
  MariaDB is a community-developed, commercially supported fork of the MySQL relational database management system.
---
