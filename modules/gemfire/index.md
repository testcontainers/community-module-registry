---
title: Gemfire
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/gemfire/gemfire-testcontainers
    maintainer: community
    example: |
      ```java
      GemFireClusterContainer<?> gemfire = new GemFireClusterContainer<>()
      .acceptLicense()
      gemfire.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>dev.gemfire</groupId>
          <artifactId>gemfire-testcontainers</artifactId>
          <version>2.3.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  VMware GemFire is a data management platform that provides real-time, consistent access to data-intensive applications throughout widely distributed cloud architectures.
---
