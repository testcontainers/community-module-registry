---
title: K6
categories:
  - web
docs:
  - id: java
    url: https://java.testcontainers.org/modules/k6/
    maintainer: core
    example: |
      ```java
      var k6 = new K6Container("grafana/k6:0.49.0");
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>k6</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/k6/
    maintainer: core
    example: |
      ```go
      k6Container, err := k6.Run(ctx, "szkiba/k6x:v0.3.1")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/k6
      ```
description: |
  k6 is an open-source tool and cloud service that makes load testing easy for developers and QA engineers.
---