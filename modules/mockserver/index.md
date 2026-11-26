---
title: Mockserver
categories:
  - web
docs:
  - id: java
    url: https://www.mock-server.com/mock_server/mockserver_testcontainers.html
    maintainer: official
    example: |
      ```java
      var mockServer = new MockServerContainer();
      mockServer.start();
      MockServerClient client = mockServer.getClient();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.mock-server</groupId>
          <artifactId>mockserver-testcontainers</artifactId>
          <version>7.0.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mockserver/
    maintainer: core
    example: |
      ```go
      mockServerContainer, err := mockserver.Run(context.Background(), "mockserver/mockserver:5.15.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/mockserver
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/mockserver/
    maintainer: core
    example: |
      ```javascript
      const container = await new MockserverContainer("mockserver/mockserver:5.15.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/mockserver --save-dev
      ```
description: |
  MockServer allows you to mock any server or service via HTTP or HTTPS, such as a REST or RPC service.
---
