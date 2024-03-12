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
description: |
  Oracle Database Express Edition is a free, smaller-footprint edition of Oracle Database.
---