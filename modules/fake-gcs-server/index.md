---
title: fake-gcs-server
categories:
  - other
docs:
  - id: java
    url: https://github.com/Aiven-Open/testcontainers-fake-gcs-server
    maintainer: community
    example: |
      ```java
      var fakeGcsServer = new FakeGcsServerContainer();
      fakeGcsServer.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.aiven</groupId>
          <artifactId>testcontainers-fake-gcs-server</artifactId>
          <version>0.1.0</version>
      </dependency>
      ```
description: |
  fake-gcs-server provides an emulator for Google Cloud Storage API.
---
