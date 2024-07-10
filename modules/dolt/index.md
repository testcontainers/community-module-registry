---
title: DoltDB
categories:
  - relational-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/dolt/
    maintainer: core
    example: |
      ```go
      doltContainer, err := dolt.Run(ctx, "dolthub/dolt-sql-server:1.32.4")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/dolt
      ```
description: |
  Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a Git repository.
---
