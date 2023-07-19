---
title: Meilisearch
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/junghoon-vans/testcontainers-meilisearch
    isThirdParty: true
    example: |
      ```java
      var meilisearch = new MeilisearchContainer(DockerImageName.parse("getmeili/meilisearch:latest"))
        .withMasterKey("masterKey");
      meilisearch.start();
      ```
description: |
  Meilisearch is a flexible and powerful user-focused search engine that can be added to any website or application.
---