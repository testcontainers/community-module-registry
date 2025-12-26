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
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.FakeGcsServer
    maintainer: core
    example: |
      ```csharp
      var fakeGcsServerContainer = new FakeGcsServerBuilder("fsouza/fake-gcs-server:1.47")
        .Build();
      await fakeGcsServerContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.FakeGcsServer
      ```
description: |
  fake-gcs-server provides an emulator for Google Cloud Storage API.
---
