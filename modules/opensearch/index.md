---
title: OpenSearch
categories:
  - nosql-database
  - vector-database
docs:
  - id: java
    url: https://github.com/opensearch-project/opensearch-testcontainers
    maintainer: community
    example: |
      ```java
      var opensearch = new OpensearchContainer(DockerImageName.parse("opensearchproject/opensearch:2.0.0"));
      opensearch.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.opensearch</groupId>
          <artifactId>opensearch-testcontainers</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/opensearch/
    maintainer: core
    example: |
      ```go
      opensearchContainer, err := opensearch.Run(ctx, "opensearchproject/opensearch:2.11.1")
      ```
    installation: |
      ```bash
      go get github.com/opensearch-project/opensearch-testcontainers
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/opensearch/README.html
    maintainer: core
    example: |
      ```python
      with OpenSearchContainer() as opensearch:
          client = opensearch.get_client()
      ```
    installation: |
      ```bash
      pip install testcontainers[opensearch]
      ```
description: |
  OpenSearch is a scalable, flexible, and extensible open-source software suite for search, analytics, and observability applications licensed under Apache 2.0 and powered by Apache Lucene.
---
