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
      valkeyContainer, err := valkey.Run(ctx, "docker.io/valkey/valkey:7.2.5")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/valkey
      ```
description: |
  Valkey is an open source (BSD) high-performance key/value datastore that supports a variety of workloads such as caching, message queues, and can act as a primary database. Valkey can run as either a standalone daemon or in a cluster, with options for replication and high availability.
---