---
title: Floci (AWS)
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
          <artifactId>testcontainers-floci-aws</artifactId>
          <version>2.17.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Floci.Testcontainers.Aws
    maintainer: core
    example: |
      ```csharp
      await using var floci = new FlociBuilder("floci/floci:latest").Build();
      await floci.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Floci.Testcontainers.Aws
      ```
description: |
  A free, MIT-licensed AWS emulator and drop-in replacement for LocalStack. Give your coding agents a real AWS to build and test against: no auth token, no account, no bill.
---
