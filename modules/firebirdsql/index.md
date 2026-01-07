---
title: Firebird
categories:
  - relational-database
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.FirebirdSql
    maintainer: core
    example: |
      ```csharp
      var firebirdContainer = new FirebirdSqlBuilder("jacobalberty/firebird:v4.0")
        .Build();
      await firebirdContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.FirebirdSql
      ```
description: |
  Firebird is a relational database offering many ANSI SQL standard features that runs on Linux, Windows, and a variety of Unix platforms. Firebird offers excellent concurrency, high performance, and powerful language support for stored procedures and triggers. It has been used in production systems, under a variety of names, since 1981.
---
