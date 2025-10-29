---
title: Solr
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/solr/
    maintainer: core
    example: |
      ```java
      var solr = new SolrContainer(DockerImageName.parse("solr:8.3.0"));
      solr.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-solr</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/solr/struct.Solr.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::solr::Solr::default().start()
      ```
    installation: |
      ```bash
      cargo add -F solr --dev testcontainers-modules
      ```
description: |
  Solr is an open-source enterprise-search platform that features full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, database integration, NoSQL features and rich document handling.
---
