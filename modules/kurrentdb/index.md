---
title: KurrentDB
categories:
  - nosql-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/kurrentdb/
    maintainer: core
    example: |
      ```go
      kurrentdbContainer, err := kurrentdb.Run(context.Background(), "kurrentplatform/kurrentdb:26.1.1")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/kurrentdb
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.KurrentDb
    maintainer: core
    example: |
      ```csharp
      var kurrentDbContainer = new KurrentDbBuilder("kurrentplatform/kurrentdb:25.1")
        .Build();
      await kurrentDbContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.KurrentDb
      ```
description: |
  KurrentDB is an event-native database designed specifically to store, process, and deliver application state changes, known as events.
---
