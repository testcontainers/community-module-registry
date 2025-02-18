---
title: Dapr
categories:
  - cloud
officialPartner:
  name: Diagrid
  url: https://www.diagrid.io/
docs:
  - id: java
    url: https://github.com/diagridio/testcontainers-dapr
    maintainer: official
    example: |
      ```java
      var dapr = new DaprContainer("daprio/daprd:1.13.2");
      dapr.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.dapr</groupId>
          <artifactId>testcontainers-dapr</artifactId>
          <version>0.13.3</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Dapr is a CNCF and open-source project to enable developers with a consistent set of application-level APIs to develop faster cloud-native applications.
---
