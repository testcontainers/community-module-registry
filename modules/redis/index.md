---
title: Redis
categories:
  - nosql-database
  - vector-database
docs:
  - id: java
    url: https://github.com/redis-developer/testcontainers-redis
    maintainer: community
    example: |
      ```java
      var redis = new RedisContainer(DockerImageName.parse("redis:6.2.6"));
      redis.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/redis/
    maintainer: core
    example: |
      ```go
      redisContainer, err := redis.RunContainer(ctx, testcontainers.WithImage("redis:6"))
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Redis
    maintainer: core
    example: |
      ```csharp
      var redisContainer = new RedisBuilder()
        .WithImage("redis:7.0")
        .Build();
      await redisContainer.StartAsync();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/redis/
    maintainer: core
    example: |
      ```javascript
      const container = await new RedisContainer().start();
      ```
description: |
  Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices.
---