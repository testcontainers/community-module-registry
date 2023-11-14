---
title: Microcks
isOfficial: true
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/microcks/microcks-testcontainers-java
    example: |
      ```java
      var microcks = new MicrocksContainer(DockerImageName.parse("quay.io/microcks/microcks-uber:1.8.0"));
      microcks.start();
      ```
  - id: go
    url: https://github.com/microcks/microcks-testcontainers-go
    example: |
      ```go
      microcksContainer, err := microcks.RunContainer(ctx, testcontainers.WithImage("quay.io/microcks/microcks-uber:1.8.0"))
      ```
  - id: nodejs
    url: https://github.com/microcks/microcks-testcontainers-node
    example: |
      ```javascript
      const microcks = await new MicrocksContainer().start();
      ```
description: |
  Microcks is an open-source cloud-native platform for mocking and contract-testing all kinds of APIs. It supports REST [OpenAPI](https://www.openapis.org/), [gRPC](https://grpc.io/), [GraphQL](https://graphql.org/), [Async APIs](https://www.asyncapi.com/) and SOAP WebServices.

  Microcks allows you to work in isolation by cutting dependencies; it can also be used for contract-testing the API you're developing.
  
  Read more on [Microcks.io](https://microcks.io).
---