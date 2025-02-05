---
title: ScyllaDB
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/scylladb/
    maintainer: core
    example: |
      ```java
      var container = new ScyllaDBContainer(DockerImageName.parse("scylladb/scylla:6.2"));
      container.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>scylladb</artifactId>
          <version>1.20.5</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/scylla/README.html
    maintainer: core
    example: |
      ```python
      with ScyllaContainer(image = "scylladb/scylla:6.2") as scylla:
          cluster = scylla.get_cluster()
      ```
    installation: |
      ```bash
      pip install testcontainers[scylla]
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/scylladb/
    maintainer: core
    example: |
      ```javascript
      const container = await new ScyllaContainer("scylladb/scylla:6.2.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/scylladb --save-dev
      ```
description: |
  ScyllaDB is a distributed NoSQL wide-column database for data-intensive apps that require high performance and low latency.
---
