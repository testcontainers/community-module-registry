---
title: Aspire Dashboard
categories:
  - other
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.AspireDashboard
    maintainer: core
    example: |
      ```csharp
      var aspireDashboardContainer = new AspireDashboardBuilder("mcr.microsoft.com/dotnet/aspire-dashboard:13")
        .Build();
      await aspireDashboardContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.AspireDashboard
      ```
description: |
  The Aspire dashboard is a standalone tool for viewing the logs, traces, and metrics that your apps emit over the OpenTelemetry Protocol (OTLP). It provides a web interface to explore telemetry during local development.
---
