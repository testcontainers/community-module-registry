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
      doltContainer, err := dolt.RunContainer(ctx, testcontainers.WithImage("dolthub/dolt-sql-server:1.32.4"))
      ```
description: |
  Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a Git repository.
---
