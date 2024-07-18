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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>mockserver</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mockserver/
    maintainer: core
    example: |
      ```go
      mockServerContainer, err := mockserver.Run(ctx, "mockserver/mockserver:5.15.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/mockserver
      ```
description: |
  MockServer allows you to mock any server or service via HTTP or HTTPS, such as a REST or RPC service.
---