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
description: |
  Floci is a fast, free, open-source AWS emulator built with Quarkus Native. Starts in 24ms, uses 13 MiB at idle. Drop-in replacement for LocalStack — no auth token, no restrictions, ever.
---
