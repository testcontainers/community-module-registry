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
description: |
  Solr is an open-source enterprise-search platform that features full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, database integration, NoSQL features and rich document handling.
---