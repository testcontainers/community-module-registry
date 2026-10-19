---
title: Garnet
categories:
  - nosql-database
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Redis
    maintainer: core
    example: |
      ```csharp
      var garnetContainer = new RedisBuilder("ghcr.io/microsoft/garnet:1.0.99")
        .Build();
      await garnetContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Redis
      ```
description: |
  Garnet is a high-performance, Redis-compatible in-memory cache-store from Microsoft Research. It works with existing Redis clients through the RESP wire protocol.
---
