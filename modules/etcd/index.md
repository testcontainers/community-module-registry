---
title: etcd
categories:
  - other
docs:
  - id: java
    url: https://github.com/etcd-io/jetcd/blob/ebf983b811f983e51e7d93f30478698c5c582d73/jetcd-launcher/src/main/java/io/etcd/jetcd/launcher/EtcdContainer.java
    maintainer: community
    example: |
      ```java
      var etcdContainer = new EtcdContainer();
      etcdContainer.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.etcd</groupId>
          <artifactId>jetcd-core</artifactId>
          <version>0.8.2</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/etcd/
    maintainer: core
    example: |
      ```go
      etcdContainer, err := etcd.Run(ctx, "gcr.io/etcd-development/etcd:v3.5.14")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/etcd
      ```
description: |
  etcd is a strongly consistent, distributed key-value store that provides a reliable way to store data that needs to be accessed by a distributed system or cluster of machines. It gracefully handles leader elections during network partitions and can tolerate machine failure, even in the leader node.
---
