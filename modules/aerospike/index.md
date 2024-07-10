---
title: Aerospike
categories:
  - nosql-database
  - vector-database
docs:
  - id: go
    url: https://github.com/ajeetdsouza/testcontainers-aerospike-go
    maintainer: community
    example: |
      ```go
      container, err := aeroTest.RunContainer(ctx)
      if err != nil {
        return err
      }
      ```
    installation: |
      ```bash
      go get -u github.com/ajeetdsouza/testcontainers-aerospike-go@latest
      ```
description: |
  Aerospike is a real-time, high performance NoSQL database.
---
