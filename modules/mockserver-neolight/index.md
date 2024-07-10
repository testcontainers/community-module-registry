---
title: MockServer NeoLight
categories:
  - web
docs:
  - id: java
    url: https://github.com/xdev-software/mockserver-neolight
    maintainer: community
    example: |
      ```java
      # Version is discovered automatically
      var mockServer = new MockServerContainer();
      mockServer.start();
      ```
    installation: |
      ```xml
      <dependency>
            <groupId>software.xdev.mockserver</groupId>
            <artifactId>testcontainers</artifactId>
            <version>1.0.2</version>
            <scope>test</scope>
      </dependency>
      ```
description: |
  This is a lightweight rewrite of the abandoned MockServer - which allows you to mock any server or service via HTTP, such as a REST or RPC service - with focus on simplicity, maintainability and Testcontainers.
---