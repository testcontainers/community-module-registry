---
title: Infinispan
categories:
  - nosql-database
  - vector-database
docs:
  - id: java
    url: https://github.com/infinispan/infinispan
    maintainer: community
    example: |
      ```java
      var infinispan = new InfinispanContainer();
      infinispan.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.infinispan</groupId>
          <artifactId>infinispan-server-testdriver-core</artifactId>
          <version>16.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Infinispan is an open-source in-memory database that can hold nearly any type of data, from plain-text to structured objects.
---
