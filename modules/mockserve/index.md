---
title: Mockserver
categories:
  - web
docs:
  - id: java
    url: https://java.testcontainers.org/modules/mockserver/
    maintainer: core
    example: |
      ```java
      var mockServer = new MockServerContainer(DockerImageName
        .parse("mockserver/mockserver:5.15.0"));
      mockServer.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mockserver/
    maintainer: core
    example: |
      ```go
      mockServerContainer, err := mockserver.RunContainer(ctx, testcontainers.WithImage("mockserver/mockserver:5.15.0"))
      ```
description: |
  MockServer allows you to mock any server or service via HTTP or HTTPS, such as a REST or RPC service.
---