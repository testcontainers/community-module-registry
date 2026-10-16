---
title: Floci
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/floci-io/testcontainers-floci
    maintainer: official
    example: |
      ```java
      var floci = new FlociContainer();
      floci.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.floci</groupId>
          <artifactId>testcontainers-floci</artifactId>
          <version>2.0.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Floci
    maintainer: core
    example: |
      ```csharp
      var flociContainer = new FlociBuilder("floci/floci:1.5.13")
        .Build();
      await flociContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Floci
      ```
description: |
  Floci is a fast, free, open-source AWS emulator built with Quarkus Native. Starts in 24ms, uses 13 MiB at idle. Drop-in replacement for LocalStack — no auth token, no restrictions, ever.
---
