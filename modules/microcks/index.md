---
title: Microcks
categories:
  - cloud
officialPartner:
  name: Microcks
  url: https://microcks.io/
docs:
  - id: java
    url: https://github.com/microcks/microcks-testcontainers-java
    maintainer: official
    example: |
      ```java
      var microcks = new MicrocksContainer(DockerImageName.parse("quay.io/microcks/microcks-uber:1.8.0"));
      microcks.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.github.microcks</groupId>
          <artifactId>microcks-testcontainers</artifactId>
          <version>0.2.8</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://github.com/microcks/microcks-testcontainers-go
    maintainer: official
    example: |
      ```go
      microcksContainer, err := microcks.RunContainer(context.Background(), testcontainers.WithImage("quay.io/microcks/microcks-uber:1.8.0"))
      ```
    installation: |
      ```bash
      go get github.com/microcks/microcks-testcontainers-go
      ```
  - id: nodejs
    url: https://github.com/microcks/microcks-testcontainers-node
    maintainer: official
    example: |
      ```javascript
      const microcks = await new MicrocksContainer().start();
      ```
    installation: |
      ```bash
      npm install @microcks/microcks-testcontainers --save-dev
      ```
  - id: dotnet
    url: https://github.com/microcks/microcks-testcontainers-dotnet
    maintainer: official
    example: |
      ```csharp
      var microcks = new MicrocksBuilder().WithImage("quay.io/microcks/microcks-uber:1.8.0").Build();
      await microcks.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Microcks.Testcontainers
      ``
description: |
  Microcks is an open-source cloud-native platform for mocking and contract-testing all kinds of APIs. It supports REST [OpenAPI](https://www.openapis.org/), [gRPC](https://grpc.io/), [GraphQL](https://graphql.org/), [Async APIs](https://www.asyncapi.com/) and SOAP WebServices.

  Microcks allows you to work in isolation by cutting dependencies; it can also be used for contract-testing the API you're developing.

  Read more on [Microcks.io](https://microcks.io).
---
