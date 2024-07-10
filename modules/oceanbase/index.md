---
title: OceanBase
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/oceanbase/
    maintainer: community
    example: |
      ```java
      OceanbaseCEContainer oceanbase = new OceanbaseCEContainer("oceanbase/oceanbase-ce:4.2.2");
      oceanbase.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>oceanbase</artifactId>
          <version>1.19.8</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  OceanBase is an open source unlimited scalable distributed database for data-intensive transactional and real-time operational analytics workloads, with ultra-fast performance that has once achieved world records in the TPC-C benchmark test.
---
