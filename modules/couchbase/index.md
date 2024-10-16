---
title: Couchbase
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/couchbase/
    maintainer: core
    example: |
      ```java
      var couchbase = new CouchbaseContainer(DockerImageName.parse(
        "couchbase/server:community-7.0.2"
      ));
      couchbase.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>couchbase</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/couchbase/
    maintainer: core
    example: |
      ```go
      couchbaseContainer, err := couchbase.Run(ctx,
        "couchbase/server:community-7.0.2",
        couchbase.WithBucket(couchbase.NewBucket("bucketName")),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/couchbase
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Couchbase
    maintainer: core
    example: |
      ```csharp
      var couchbaseContainer = new CouchbaseBuilder()
        .WithImage("couchbase:community-7.0.2")
        .Build();
      await couchbaseContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Couchbase --version 3.9.0
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/couchbase/
    maintainer: core
    example: |
      ```javascript
      const container = await new CouchbaseContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/couchbase --save-dev
      ```
description: |
  Couchbase is an open-source, distributed, multi-model, document oriented, NoSQL database.
---
