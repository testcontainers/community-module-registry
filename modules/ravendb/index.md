---
title: RavenDB
categories:
  - nosql-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/ravendb/
    maintainer: core
    example: |
      ```go
      ravendbContainer, err := ravendb.Run(context.Background(), "ravendb/ravendb:6.0-ubuntu-latest")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/ravendb
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.RavenDb
    maintainer: core
    example: |
      ```csharp
      var ravenDbContainer = new RavenDbBuilder("ravendb/ravendb:5.4-ubuntu-latest")
        .Build();
      await ravenDbContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.RavenDb
      ```
description: |
  RavenDB is an open-source NoSQL database software designed to help businesses streamline multi-document ACID transactions and facilitate extract, transform, and load (ETL) operations.
---
