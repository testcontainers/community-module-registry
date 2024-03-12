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
description: |
  YugabyteDB is a high-performance transactional distributed SQL database for cloud-native applications.
---