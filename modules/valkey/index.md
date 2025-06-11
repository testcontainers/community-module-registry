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
      use testcontainers_modules::{
          testcontainers::runners::SyncRunner,
          valkey::{Valkey, VALKEY_PORT},
      };

      let valkey_instance = Valkey::default().start().unwrap();
      let host_ip = valkey_instance.get_host().unwrap();
      let host_port = valkey_instance.get_host_port_ipv4(VALKEY_PORT).unwrap();

      let url = format!("redis://{host_ip}:{host_port}");
      let client = redis::Client::open(url.as_ref()).unwrap();
      let mut con = client.get_connection().unwrap();

      con.set::<_, _, ()>("my_key", 42).unwrap();
      let result: i64 = con.get("my_key").unwrap();
      ```
    installation: |
      ```bash
      cargo add -F valkey --dev testcontainers-modules
      ```
description: |
  Valkey is an open source (BSD) high-performance key/value datastore that supports a variety of workloads such as caching, message queues, and can act as a primary database. Valkey can run as either a standalone daemon or in a cluster, with options for replication and high availability.
---
