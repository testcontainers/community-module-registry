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
  - id: go
    url: https://golang.testcontainers.org/modules/couchbase/
    maintainer: core
    example: |
      ```go
      couchbaseContainer, err := couchbase.RunContainer(ctx,
        testcontainers.WithImage("couchbase/server:community-7.0.2"),
        couchbase.WithBucket(couchbase.NewBucket("bucketName")),
      )
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
  - id: nodejs
    url: https://node.testcontainers.org/modules/couchbase/
    maintainer: core
    example: |
      ```javascript
      const container = await new CouchbaseContainer().start();
      ```
description: |
  Couchbase is an open-source, distributed, multi-model, document oriented, NoSQL database.
---