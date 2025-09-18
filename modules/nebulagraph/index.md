---
title: NebulaGraph
categories:
  - nosql-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/nebulagraph/
    maintainer: core
    example: |
      ```go
      cluster, err := nebulagraph.RunCluster(ctx,
          "vesoft/nebula-graphd:v3.8.0", []testcontainers.ContainerCustomizer{},
          "vesoft/nebula-storaged:v3.8.0", []testcontainers.ContainerCustomizer{},
          "vesoft/nebula-metad:v3.8.0", []testcontainers.ContainerCustomizer{},
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/nebulagraph
      ```
description: |
  NebulaGraph is a distributed, scalable, and lightning-fast graph database.
---
