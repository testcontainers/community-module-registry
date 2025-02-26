---
title: Meilisearch
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/junghoon-vans/testcontainers-meilisearch
    maintainer: community
    example: |
      ```java
      var meilisearch = new MeilisearchContainer(DockerImageName.parse("getmeili/meilisearch:latest"))
        .withMasterKey("masterKey");
      meilisearch.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>io.vanslog</groupId>
          <artifactId>testcontainers-meilisearch</artifactId>
          <version>1.0.5</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/etcd/
    maintainer: core
    example: |
      ```go
      meiliContainer, err := meilisearch.Run(context.Background(), "getmeili/meilisearch:v1.10.3")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/meilisearch
      ```
description: |
  Meilisearch is a flexible and powerful user-focused search engine that can be added to any website or application.
---
