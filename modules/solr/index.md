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
          <artifactId>solr</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
description: |
  Solr is an open-source enterprise-search platform that features full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, database integration, NoSQL features and rich document handling.
---
