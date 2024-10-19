---
title: Oxia
categories:
  - other
docs:
  - id: java
    url: https://github.com/streamnative/oxia-java/tree/main/testcontainers
    maintainer: community
    example: |
      ```java
      var oxia = new OxiaContainer("streamnative/oxia:0.3");
      oxia.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.streamnative.oxia</groupId>
          <artifactId>oxia-testcontainers</artifactId>
          <version>0.0.14</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Oxia is a scalable metadata store and coordination system that can be used as the core infrastructure to build large-scale distributed systems.
---
