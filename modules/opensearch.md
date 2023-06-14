---
title: OpenSearch
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/opensearch-project/opensearch-testcontainers
    isThirdParty: true
    example: |
      ```java
      var opensearch = new OpensearchContainer(DockerImageName.parse("opensearchproject/opensearch:2.0.0"));
      opensearch.start();
      ```
description: |
  OpenSearch is a scalable, flexible, and extensible open-source software suite for search, analytics, and observability applications licensed under Apache 2.0 and powered by Apache Lucene.
---