---
title: Dapr
categories:
  - cloud
officialPartner:
  name: Diagrid
  url: https://www.diagrid.io/
docs:
  - id: java
    url: https://github.com/dapr/java-sdk/tree/master/testcontainers-dapr
    maintainer: official
    example: |
      ```java
      var dapr = new DaprContainer("daprio/daprd:1.16.0");
      dapr.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.dapr</groupId>
          <artifactId>testcontainers-dapr</artifactId>
          <version>1.16.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Dapr is a CNCF and open-source project that enables developers with consistent application-level APIs to develop secure, scalable, and resilient cloud-native applications.
---
