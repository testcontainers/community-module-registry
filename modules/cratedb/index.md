---
title: CrateDB
categories:
  - relational-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/cratedb/
    maintainer: core
    example: |
      ```go
      cratedbContainer, err := cratedb.Run(context.Background(), "crate:5.7")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/cratedb
      ```
description: |
  CrateDB is a distributed and scalable SQL database for storing and analyzing massive amounts of data in near real-time.
---
