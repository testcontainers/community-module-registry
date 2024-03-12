---
title: Dynalite
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/dynalite/
    maintainer: core
    example: |
      ```java
      var dynamoDB = new DynaliteContainer(DockerImageName.parse(
        "quay.io/testcontainers/dynalite:v1.2.1-1"
      ));
      dynamoDB.start();
      ```
description: |
  Dynalite is an implementation of Amazon's DynamoDB built on LevelDB that aims to match live DynamoDB instances as closely as possible, including all limits and error messages.
---