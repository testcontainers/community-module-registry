---
title: Azure SQL Edge
categories:
  - cloud
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/azure/
    maintainer: core
    example: |
      ```go
      sqledgeContainer, err := sqledge.Run(context.Background(), "mcr.microsoft.com/azure-sql-edge:1.0.7", sqledge.WithAcceptEULA())
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/azure/sqledge
      ```
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
      dotnet add package Testcontainers.SqlEdge
      ```
description: |
  Azure SQL Edge is an Internet of Things (IoT) database for edge computing which combines capabilities such as data streaming and time series with built-in machine learning and graph features.
---
