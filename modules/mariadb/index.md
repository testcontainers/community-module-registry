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
  - id: go
    url: https://golang.testcontainers.org/modules/mariadb
    maintainer: core
    example: |
      ```go
      mariaDBContainer, err := mariadb.RunContainer(ctx, testcontainers.WithImage("mariadb:11.0.3"))
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
description: |
  MariaDB is a community-developed, commercially supported fork of the MySQL relational database management system.
---