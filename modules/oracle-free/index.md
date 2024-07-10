---
title: Oracle Free
categories:
  - relational-database
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/oraclefree/
    maintainer: core
    example: |
      ```java
      var oracle = new OracleContainer("gvenzl/oracle-free:23.4-slim-faststart");
      oracle.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>oracle-free</artifactId>
          <version>1.19.8</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  Oracle Database Free is a free edition of the world's leading database specifically designed for anybody to develop, learn, and run on Oracle Database for free.
---