---
title: Ignition
categories:
  - other
docs:
  - id: java
    url: https://github.com/mussonindustrial/testcontainers-ignition/
    maintainer: community
    example: |
      ```java
      var ignition = new IgnitionContainer("inductiveautomation/ignition:8.1.33")
        .acceptLicense();
      ignition.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>com.mussonindustrial</groupId>
          <artifactId>testcontainers-ignition</artifactId>
          <version>0.3.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Ignition is a powerful integrated development environment with everything you need to create virtually any kind of industrial software application – SCADA, IIoT, MES and beyond – all on one platform.
---