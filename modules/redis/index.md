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
    installation: |
      ```xml
      <dependency>
          <groupId>com.redis</groupId>
          <artifactId>testcontainers-redis</artifactId>
          <version>2.2.2</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/redis/
    maintainer: core
    example: |
      ```go
      redisContainer, err := redis.Run(ctx, "redis:6")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/redis
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
    installation: |
      ```bash
      dotnet add package Testcontainers.Redis --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/redis/
    maintainer: core
    example: |
      ```javascript
      const container = await new RedisContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/redis --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/redis/README.html
    maintainer: community
    example: |
      ```python
      with RedisContainer() as redis_container:
        redis_client = redis_container.get_client()
      ```
    installation: |
      ```bash
      pip install testcontainers[redis]
      ```
description: |
  Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices.
---
