---
title: SurrealDB
categories:
  - nosql-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/surrealdb/
    maintainer: core
    example: |
      ```go
      surrealdbContainer, err := surrealdb.Run(ctx, "surrealdb/surrealdb:v1.1.1")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/surrealdb
      ```
  - id: rust
    url: https://github.com/testcontainers/testcontainers-rs-modules-community
    maintainer: community
    example: |
      ```rust
      let docker = Cli::default();
      let surrealdb_container = docker.run(SurrealDb::default());
      ```
    installation: |
      ```rust
      use testcontainers_modules::{surrealdb, testcontainers::runners::SyncRunner};
description: |
  SurrealDB is an end-to-end cloud-native database designed for modern applications, including web, mobile, serverless, Jamstack, backend, and traditional applications.

  With SurrealDB, you can simplify your database and API infrastructure, reduce development time, and build secure, performant apps quickly and cost-effectively.

  Read more on [SurrealDB Website](https://surrealdb.com).
---
