---
title: Azure Data Explorer Kusto emulator
categories:
  - other
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Kusto
    maintainer: core
    example: |
      ```csharp
      var kustoContainer = new KustoBuilder()
        .WithImage("mcr.microsoft.com/azuredataexplorer/kustainer-linux:latest")
        .Build();
      await kustoContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Kusto
      ```
description: |
  Kusto Query Language (KQL) is a powerful tool for exploring your data and discovering patterns, identifying anomalies and outliers, creating statistical modeling, and more. KQL is a simple yet powerful language to query structured, semi-structured, and unstructured data. The language is expressive, easy to read and understand the query intent, and optimized for authoring experiences. KQL is optimal for querying telemetry, metrics, and logs with deep support for text search and parsing, time-series operators and functions, analytics and aggregation, geospatial, vector similarity searches, and many other language constructs that provide the most optimal language for data analysis. The query uses schema entities that are organized in a hierarchy similar to SQLs: databases, tables, and columns.
---
