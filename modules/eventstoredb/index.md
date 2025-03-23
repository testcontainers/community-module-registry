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
      dotnet add package Testcontainers.EventStoreDb
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/eventstoredb/
    maintainer: core
    example: |
      ```javascript
      const container = await new EventStoreDBContainer("eventstore/eventstore:24.10").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/eventstoredb --save-dev
      ```
description: |
  EventStoreDB is an event sourcing database that stores data in streams of immutable events.
---
