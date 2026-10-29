---
title: Floci OCI
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/floci-io/testcontainers-floci
    maintainer: official
    example: |
      ```java
      var floci = new FlociOciContainer();
      floci.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.floci</groupId>
          <artifactId>testcontainers-floci-oci</artifactId>
          <version>2.17.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Floci.Testcontainers.Oci
    maintainer: core
    example: |
      ```csharp
      await using var floci = new FlociOciBuilder("floci/floci-oci:latest").Build();
      await floci.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Floci.Testcontainers.Oci
      ```
description: |
  A free, MIT-licensed Oracle Cloud Infrastructure emulator. Give your coding agents a real OCI to build and test against: no Oracle Cloud account, no uploaded API keys, no bill.
---
