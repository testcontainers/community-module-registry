---
title: Oracle-XE
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/oraclexe/
    maintainer: core
    example: |
      ```java
      var oracle = new OracleContainer(DockerImageName.parse("gvenzl/oracle-xe:21-slim-faststart"));
      oracle.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>oracle-xe</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Oracle
    maintainer: core
    example: |
      ```csharp
      var oracleContainer = new OracleBuilder()
        .WithImage("gvenzl/oracle-xe:21.3.0-slim-faststart")
        .Build();
      await oracleContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Oracle --version 3.9.0
      ```
description: |
  Oracle Database Express Edition is a free, smaller-footprint edition of Oracle Database.
---