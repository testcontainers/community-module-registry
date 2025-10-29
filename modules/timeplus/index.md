---
title: Timeplus
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/timeplus/
    maintainer: core
    example: |
      ```java
      var timeplus = new TimeplusContainer(DockerImageName.parse("timeplus/timeplusd:2.3.21"));
      timeplus.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-timeplus</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Timeplus is a simple, powerful, and cost-efficient stream processing platform.
---
