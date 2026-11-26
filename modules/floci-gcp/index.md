---
title: Floci GCP
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/floci-io/testcontainers-floci
    maintainer: official
    example: |
      ```java
      var floci = new FlociGcpContainer();
      floci.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.floci</groupId>
          <artifactId>testcontainers-floci-gcp</artifactId>
          <version>2.17.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Floci.Testcontainers.Gcp
    maintainer: core
    example: |
      ```csharp
      await using var floci = new FlociGcpBuilder("floci/floci-gcp:latest").Build();
      await floci.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Floci.Testcontainers.Gcp
      ```
description: |
  A free, MIT-licensed Google Cloud emulator. Give your coding agents a real GCP to build and test against: no project, no billing account, no auth token.
---
