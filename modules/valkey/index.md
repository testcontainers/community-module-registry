---
title: Valkey
categories:
  - nosql-database
  - vector-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/valkey/
    maintainer: core
    example: |
      ```go
      valkeyContainer, err := valkey.Run(context.Background(), "docker.io/valkey/valkey:7.2.5")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/valkey
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/valkey/
    maintainer: core
    example: |
      ```javascript
      const container = await new ValkeyContainer("valkey/valkey:8.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/valkey --save-dev
      ```
description: |
  Valkey is an open source (BSD) high-performance key/value datastore that supports a variety of workloads such as caching, message queues, and can act as a primary database. Valkey can run as either a standalone daemon or in a cluster, with options for replication and high availability.
---
