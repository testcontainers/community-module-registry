---
title: Grafana
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/grafana/
    maintainer: core
    example: |
      ```java
      var lgtm = new LgtmStackContainer("grafana/otel-lgtm:0.6.0");
      lgtm.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>grafana</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Grafana is the open source analytics & monitoring solution for every database.
---