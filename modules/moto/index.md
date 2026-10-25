---
title: Moto
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/georgeracu/testcontainers-moto
    maintainer: community
    example: |
      ```java
      var moto = new MotoContainer("motoserver/moto:5.1.22");
      moto.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.github.georgeracu</groupId>
          <artifactId>testcontainers-moto</artifactId>
          <version>0.1.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Moto serves every AWS service on a single port with no per-service opt-in, so `MotoContainer` gives you one container and one endpoint that any AWS SDK client can be pointed at — no AWS account, no network calls, no cost. A Spring Boot variant adds `@ServiceConnection` support for auto-configuring Spring Cloud AWS clients.
---
