---
title: ScyllaDB
categories:
  - nosql-database
docs:
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/scylla/README.html
    maintainer: community
    example: |
      ```python
      with ScyllaContainer(image = "scylladb/scylla:6.2") as scylla:
        cluster = scylla.get_cluster()
      ```
    installation: |
      ```bash
      pip install testcontainers[scylla]
      ```
description: |
  ScyllaDB is a distributed NoSQL wide-column database for data-intensive apps that require high performance and low latency.
---
