---
title: DB2
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/db2/
    maintainer: core
    example: |
      ```java
      var db2 = new Db2Container(DockerImageName.parse("ibmcom/db2:11.5.0.0a"))
        .acceptLicense();
      db2.start();
      ```
description: |
  IBM Db2 is a family of data management products, including database servers.
---