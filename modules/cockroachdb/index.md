---
title: CockroachDB
categories:
  - relational-database
officialPartner:
  name: Cockroach Labs
  url: https://cockroachlabs.com
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/cockroachdb/
    maintainer: official
    example: |
      ```java
      var cockroach = new new CockroachContainer(DockerImageName.parse("cockroachdb/cockroach:v22.2.3"));
      cockroach.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/databases/cockroachdb/
    maintainer: core
    example: |
      ```go
      cockroachdbContainer, err := cockroachdb.RunContainer(ctx, testcontainers.WithImage("cockroachdb/cockroach:v22.2.3")
      ```
description: |
  CockroachDB is an open-source, cloud-native, resilient, distributed SQL database.
---