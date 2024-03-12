---
title: MySQL
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/mysql/
    maintainer: core
    example: |
      ```java
      var mysql = new MySQLContainer<>(DockerImageName.parse("mysql:5.7.34"));
      mysql.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mysql/
    maintainer: core
    example: |
      ```go
      mysqlContainer, err := mysql.RunContainer(ctx, testcontainers.WithImage("mysql:5.7.34"))
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.MySql
    maintainer: core
    example: |
      ```csharp
      var mySqlContainer = new MySqlBuilder()
        .WithImage("mysql:8.0")
        .Build();
      await mySqlContainer.StartAsync();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/mysql/
    maintainer: core
    example: |
      ```javascript
      const container = await new MySqlContainer().start();
      ```
description: |
  MySQL is an open-source relational database management system.
---