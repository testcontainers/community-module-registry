---
title: Cassandra
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/cassandra/
    maintainer: core
    example: |
      ```java
      var cassandra = new CassandraContainer<>(DockerImageName.parse("cassandra:3.11.2"));
      cassandra.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>cassandra</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/cassandra/
    maintainer: core
    example: |
      ```go
      cassandraContainer, err := cassandra.Run(ctx, "cassandra:4.1.3")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/cassandra
      ```
description: |
  Cassandra is a free and open source, distributed NoSQL database management system. It is designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.
---
