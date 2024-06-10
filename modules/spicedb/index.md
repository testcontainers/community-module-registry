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
        container, err := spicedbcontainer.RunContainer(ctx,
                testcontainers.WithImage("authzed/spicedb:v1.33.0"),
            )
      ```
description: |
  SpiceDB is a graph database purpose-built for storing and evaluating access control data.
---
