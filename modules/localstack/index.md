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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>localstack</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/localstack/
    maintainer: core
    example: |
      ```go
      localstackContainer, err := localstack.Run(ctx, "localstack/localstack:1.4.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/localstack
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
    installation: |
      ```bash
      dotnet add package Testcontainers.LocalStack --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/localstack/
    maintainer: core
    example: |
      ```javascript
      const container = await new LocalstackContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/localstack --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/localstack/README.html
    maintainer: community
    example: |
      ```python
      with LocalStackContainer(image="localstack/localstack:2.0.1") as localstack:
        dynamo_client = localstack.get_client("dynamodb")
        tables = dynamo_client.list_tables()
      ```
    installation: |
      ```bash
      pip install testcontainers[localstack]
      ```
description: |
  LocalStack is a fully functional local AWS cloud stack. This module allows you to develop your cloud and serverless apps without actually using the cloud.
---
