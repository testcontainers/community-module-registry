---
title: Floci Azure
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/floci-io/testcontainers-floci
    maintainer: official
    example: |
      ```java
      var floci = new FlociAzContainer();
      floci.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.floci</groupId>
          <artifactId>testcontainers-floci-az</artifactId>
          <version>2.17.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Floci.Testcontainers.Az
    maintainer: core
    example: |
      ```csharp
      await using var floci = new FlociAzBuilder("floci/floci-az:latest").Build();
      await floci.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Floci.Testcontainers.Az
      ```
description: |
  A free, MIT-licensed Azure emulator with Azurite-compatible connection strings. Give your coding agents a real Azure to build and test against: no account, no subscription, no bill.
---
