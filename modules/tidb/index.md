---
title: TiDB
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/tidb/
    maintainer: core
    example: |
      ```java
      var tidb = new TiDBContainer(DockerImageName.parse("pingcap/tidb:v6.1.0"));
      tidb.start();
      ```
description: |
  TiDB is an open-source NewSQL database that supports Hybrid Transactional and Analytical Processing workloads. It is MySQL compatible and can provide horizontal scalability, strong consistency, and high availability.
---