---
title: Aerospike
categories:
  - nosql-database
  - vector-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/aerospike
    maintainer: core
    example: |
      ```go
      aerospikeContainer, err := aerospike.Run(ctx, "aerospike/aerospike-server:latest")
      ```
    installation: |
      ```bash
      go get -u github.com/testcontainers/testcontainers-go/modules/aerospike
      ```
description: |
  Aerospike is a real-time, high performance NoSQL database.
---
