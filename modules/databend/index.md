---
title: Databend
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/databend/
    maintainer: core
    example: |
      ```java
      DatabendContainer databend = new DatabendContainer("datafuselabs/databend:v1.2.615");
      databend.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>databend</artifactId>
          <version>1.20.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/databend/
    maintainer: core
    example: |
      ```go
      databendContainer, err := databend.Run(ctx, "datafuselabs/databend:v1.2.615", databend.WithUsername("test1"), databend.WithPassword("pass1"))
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/databend
      ```
description: |
    Databend, built in Rust, is an open-source cloud data warehouse.
---