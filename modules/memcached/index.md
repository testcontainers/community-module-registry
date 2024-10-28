---
title: Memcached
categories:
  - nosql-database
docs:
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/memcached/README.html
    maintainer: core
    example: |
      ```python
      with MemcachedContainer(image = "memcached:1.6.32") as memcached:
         host, port = memcached.get_host_and_port()
      ```
    installation: |
      ```bash
      pip install testcontainers[memcached]
      ```
description: |
  Memcached is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering.
---
