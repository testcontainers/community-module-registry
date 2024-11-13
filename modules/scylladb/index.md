---
title: ScyllaDB
categories:
  - nosql-database
docs:
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
