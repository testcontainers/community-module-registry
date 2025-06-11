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
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/solr/struct.Solr.html
    maintainer: community
    example: |
      ```rust
      use testcontainers_modules::{solr, testcontainers::runners::SyncRunner};

      let solr_instance = solr::Solr::default().start().unwrap();
      let host_port = solr_instance.get_host_port_ipv4(solr::SOLR_PORT).unwrap();

      let solr_url = format!("http://127.0.0.1:{}", host_port);

      // use HTTP client to interact with the solr API
      ```
    installation: |
      ```bash
      cargo add -F solr --dev testcontainers-modules
      ```
description: |
  Solr is an open-source enterprise-search platform that features full-text search, hit highlighting, faceted search, real-time indexing, dynamic clustering, database integration, NoSQL features and rich document handling.
---
