---
title: LocalStack
categories:
  - cloud
officialPartner:
  name: LocalStack
  url: https://www.localstack.cloud/
docs:
  - id: java
    url: https://java.testcontainers.org/modules/localstack/
    maintainer: official
    example: |
      ```java
      var localstack = new LocalStackContainer(DockerImageName.parse("localstack/localstack:0.11.3"));
      localstack.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/localstack/
    maintainer: core
    example: |
      ```go
      localstackContainer, err := localstack.RunContainer(ctx, testcontainers.WithImage("localstack/localstack:1.4.0"))
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.LocalStack
    maintainer: core
    example: |
      ```csharp
      var localStackContainer = new LocalStackBuilder()
        .WithImage("localstack/localstack:2.0")
        .Build();
      await localStackContainer.StartAsync();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/localstack/
    maintainer: core
    example: |
      ```javascript
      const container = await new LocalstackContainer().start();
      ```
description: |
  LocalStack is a fully functional local AWS cloud stack. This module allows you to develop your cloud and serverless apps without actually using the cloud.
---