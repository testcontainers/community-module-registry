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
      var dapr = new DaprContainer("daprio/daprd:1.16.4");
      dapr.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.dapr</groupId>
          <artifactId>testcontainers-dapr</artifactId>
          <version>1.16.4</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: nodejs
    url: https://github.com/dapr/testcontainer-node
    maintainer: official
    example: |
      ```javascript
      const dapr = await new DaprContainer("daprio/daprd:1.16.4").start();
      ```
    installation: |
      ```bash
      npm install @dapr/testcontainer-node --save-dev
      ```
description: |
  Dapr is a CNCF and open-source project that enables developers with consistent application-level APIs to develop secure, scalable, and resilient cloud-native applications.
---
