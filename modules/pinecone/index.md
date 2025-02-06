---
title: Pinecone
categories:
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/pinecone/
    maintainer: core
    example: |
      ```java
      var container = new PineconeContainer(DockerImageName.parse("ghcr.io/pinecone-io/pinecone-local:v0.7.0"));
      container.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>pinecone</artifactId>
          <version>1.20.5</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/pinecone/
    maintainer: core
    example: |
      ```go
      pineconeContainer, err := pinecone.Run(ctx, "ghcr.io/pinecone-io/pinecone-local:v0.7.0")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/pinecone
      ```
description: |
  Pinecone Local is an in-memory Pinecone Database emulator available as a Docker image. Pinecone is the leading AI infrastructure for building accurate, secure, and scalable AI applications. Use Pinecone Database to store and search vector data at scale.
---
