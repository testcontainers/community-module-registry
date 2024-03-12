---
title: RavenDB
categories:
  - nosql-database
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.RavenDb
    maintainer: core
    example: |
      ```csharp
      var ravenDbContainer = new RavenDbBuilder()
        .WithImage("ravendb/ravendb:5.4-ubuntu-latest")
        .Build();
      await ravenDbContainer.StartAsync();
      ```
description: |
  RavenDB is an open-source NoSQL database software designed to help businesses streamline multi-document ACID transactions and facilitate extract, transform, and load (ETL) operations.
---