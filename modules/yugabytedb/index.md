---
title: YugabyteDB
categories:
  - relational-database
officialPartner:
  name: Yugabyte
  url: https://www.yugabyte.com/
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/yugabytedb/
    maintainer: official
    example: |
      ```java
      var yugabyte = new YugabyteDBYSQLContainer(DockerImageName.parse("yugabytedb/yugabyte:2.14.4.0-b26"));
      yugabyte.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>yugabytedb</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/yugabytedb/
    maintainer: core
    example: |
      ```go
      yugabytedbContainer, err := yugabytedb.Run(ctx, "yugabytedb/yugabyte:2024.1.3.0-b105")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/yugabytedb
      ```
description: |
  YugabyteDB is a high-performance transactional distributed SQL database for cloud-native applications.
---
