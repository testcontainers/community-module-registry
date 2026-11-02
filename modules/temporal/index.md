---
title: Temporal
categories:
  - other
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Temporal
    maintainer: core
    example: |
      ```csharp
      var temporalContainer = new TemporalBuilder("temporalio/temporal:1.5.1")
        .Build();
      await temporalContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Temporal
      ```
description: |
  Temporal is an open-source durable execution platform for building reliable applications and workflows that survive failures. The module runs the Temporal development server, including the Web UI.
---
