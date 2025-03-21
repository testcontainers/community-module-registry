---
title: SpiceDB
categories:
  - other
docs:
  - id: go
    url: https://github.com/Mariscal6/testcontainers-spicedb-go
    maintainer: community
    example: |
      ```go
        spiceDBContainer, err := spicedb.Run(context.Background(), "authzed/spicedb:v1.33.0")
      ```
    installation: |
      ```bash
      go get github.com/Mariscal6/testcontainers-spicedb-go
      ```
description: |
  SpiceDB is a graph database purpose-built for storing and evaluating access control data.
---
