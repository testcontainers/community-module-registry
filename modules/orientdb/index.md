---
title: OrientDB
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/orientdb/
    maintainer: core
    example: |
      ```java
      var orient = new OrientDBContainer(DockerImageName.parse("orientdb:3.2.0-tp3"));
      orient.start();
      ```
description: |
  OrientDB is an open source NoSQL database management system. It is a Multi-model database, supporting graph, document, key/value, and object models, but the relationships are managed as in graph databases with direct connections between records.
---