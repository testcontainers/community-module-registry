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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>mysql</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mysql/
    maintainer: core
    example: |
      ```go
      mysqlContainer, err := mysql.Run(ctx, "mysql:5.7.34")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/mysql
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
    installation: |
      ```bash
      dotnet add package Testcontainers.MySql --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/mysql/
    maintainer: core
    example: |
      ```javascript
      const container = await new MySqlContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/mysql --save-dev
      ```
description: |
  MySQL is an open-source relational database management system.
---
