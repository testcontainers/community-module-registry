---
title: KurrentDB
categories:
  - nosql-database
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.KurrentDb
    maintainer: core
    example: |
      ```csharp
      var kurrentDbContainer = new KurrentDbBuilder()
        .WithImage("kurrentplatform/kurrentdb:25.1")
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
