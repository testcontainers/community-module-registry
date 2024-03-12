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
  - id: go
    url: https://golang.testcontainers.org/modules/elasticsearch/
    maintainer: core
    example: |
      ```go
      elasticsearchContainer, err := elasticsearch.RunContainer(ctx, testcontainers.WithImage("docker.elastic.co/elasticsearch/elasticsearch:8.9.0"))
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
  - id: nodejs
    url: https://node.testcontainers.org/modules/elasticsearch/
    maintainer: core
    example: |
      ```javascript
      const container = await new ElasticsearchContainer().start();
      ```
description: |
  Elasticsearch is a search and analytics engine based on Apache Lucene. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents.
---