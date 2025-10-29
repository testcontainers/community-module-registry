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
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-orientdb</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/orientdb/struct.OrientDb.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::orientdb::OrientDb::default().start()
      ```
    installation: |
      ```bash
      cargo add -F orientdb --dev testcontainers-modules
      ```
description: |
  OrientDB is an open source NoSQL database management system. It is a Multi-model database, supporting graph, document, key/value, and object models, but the relationships are managed as in graph databases with direct connections between records.
---
