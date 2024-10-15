---
title: EventStoreDB
categories:
  - nosql-database
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.EventStoreDb
    maintainer: core
    example: |
      ```csharp
      var eventStoreDbContainer = new EventStoreDbBuilder()
        .WithImage("eventstore/eventstore:22.10.1-buster-slim")
        .Build();
      await eventStoreDbContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.EventStoreDb --version 3.9.0
      ```
description: |
  EventStoreDB is an event sourcing database that stores data in streams of immutable events.
---
