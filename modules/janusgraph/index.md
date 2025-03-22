---
title: JanusGraph
categories:
  - nosql-database
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.JanusGraph
    maintainer: core
    example: |
      ```csharp
      var janusGraphContainer = new JanusGraphBuilder()
        .WithImage("janusgraph/janusgraph:1.0.0")
        .Build();
      await janusGraphContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.JanusGraph
      ```
description: |
  JanusGraph is a scalable graph database optimized for storing and querying graphs containing hundreds of billions of vertices and edges distributed across a multi-machine cluster.
---
