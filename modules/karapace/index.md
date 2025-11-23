---
title: Karapace
categories:
  - other
docs:
  - id: java
    url: https://github.com/dcolazin/karapace-testcontainers
    maintainer: community
    example: |
      ```java
      var karapace = KarapaceContainer.builder().build();
      karapace.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.vetronauta</groupId>
          <artifactId>karapace-testcontainers</artifactId>
          <version>0.1.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Karapace is a free and open-source replacement for Confluent’s Schema Registry and Apache Kafka REST proxy.
---
