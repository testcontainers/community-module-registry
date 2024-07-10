---
title: Azure SQL Edge
categories:
  - cloud
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.SqlEdge
    maintainer: core
    example: |
      ```csharp
      var sqlEdgeContainer = new SqlEdgeBuilder()
        .WithImage("mcr.microsoft.com/azure-sql-edge:1.0.7")
        .Build();
      await sqlEdgeContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.SqlEdge --version 3.9.0
      ```
description: |
  Azure SQL Edge is an Internet of Things (IoT) database for edge computing which combines capabilities such as data streaming and time series with built-in machine learning and graph features.
---