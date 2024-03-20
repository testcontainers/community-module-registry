---
title: fake-gcs-server
categories:
  - other
docs:
  - id: java
    url: https://github.com/Aiven-Open/testcontainers-fake-gcs-server
    isThirdParty: true
    example: |
      ```java
      var fakeGcsServer = new FakeGcsServerContainer();
      fakeGcsServer.start();

      // URL to connect to: fakeGcsServer.url()
      ```
description: |
  fake-gcs-server provides an emulator for Google Cloud Storage API.
---
