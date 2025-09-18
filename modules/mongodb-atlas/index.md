---
title: MongoDB Atlas
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/mongodb/#mongodbatlaslocalcontainer
    maintainer: core
    example: |
      ```java
      var container = new MongoDBAtlasLocalContainer(DockerImageName.parse("mongodb/mongodb-atlas-local:7.0.9"));
      container.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>mongodb</artifactId>
          <version>1.20.4</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mongodb-atlaslocal
    maintainer: core
    example: |
      ```go
      atlaslocalContainer, err := atlaslocal.Run(ctx, "mongodb/mongodb-atlas-local:latest")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/mongodb/atlaslocal
      ```
description: |
  MongoDB Atlas Local offers features like Atlas Search and Atlas Vector Search.
---
