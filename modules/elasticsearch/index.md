---
title: Elasticsearch
categories:
  - nosql-database
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/elasticsearch/
    maintainer: core
    example: |
      ```java
      var elastic = new ElasticsearchContainer(DockerImageName.parse("docker.elastic.co/elasticsearch/elasticsearch:7.9.2"));
      elastic.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>elasticsearch</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/elasticsearch/
    maintainer: core
    example: |
      ```go
      elasticsearchContainer, err := elasticsearch.Run(ctx, "docker.elastic.co/elasticsearch/elasticsearch:8.9.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/elasticsearch
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Elasticsearch
    maintainer: core
    example: |
      ```csharp
      var elasticsearchContainer = new ElasticsearchBuilder()
        .WithImage("elasticsearch:8.6.1")
        .Build();
      await elasticsearchContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Elasticsearch --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/elasticsearch/
    maintainer: core
    example: |
      ```javascript
      const container = await new ElasticsearchContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/elasticsearch --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/elasticsearch/README.html
    maintainer: community
    example: |
      ```python
      with ElasticSearchContainer(f'elasticsearch:8.3.3', mem_limit='3G') as es:
          resp = urllib.request.urlopen(es.get_url())
      ```
    installation: |
      ```bash
      pip install testcontainers[elasticsearch]
      ```
description: |
  Elasticsearch is a search and analytics engine based on Apache Lucene. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.
---
