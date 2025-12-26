---
title: Valkey
categories:
  - nosql-database
  - vector-database
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/valkey/
    maintainer: core
    example: |
      ```go
      valkeyContainer, err := valkey.Run(context.Background(), "docker.io/valkey/valkey:7.2.5")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/valkey
      ```
  - id: java
    url: https://github.com/ss-bhatt/testcontainers-java-valkey
    maintainer: community
    example: |
      ```java
      try (ValkeyContainer valkey = new ValkeyContainer(DockerImageName.parse("valkey/valkey:8"))) {
          valkey.start();
          // use valkey.getConnectionString()
      }
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.github.ss-bhatt</groupId>
          <artifactId>testcontainers-valkey</artifactId>
          <version>1.0.0-SNAPSHOT</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/valkey/
    maintainer: core
    example: |
      ```javascript
      const container = await new ValkeyContainer("valkey/valkey:8.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/valkey --save-dev
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/valkey/struct.Valkey.html
    maintainer: community
    example: |
      ```rust
      use redis::Commands;
      testcontainers_modules::valkey::Valkey::default().start()
      ```
    installation: |
      ```bash
      cargo add -F valkey --dev testcontainers-modules
      ```
description: |
  Valkey is an open source (BSD) high-performance key/value datastore that supports a variety of workloads such as caching, message queues, and can act as a primary database. Valkey can run as either a standalone daemon or in a cluster, with options for replication and high availability.
---