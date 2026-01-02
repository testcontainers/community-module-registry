---
title: CouchDB
categories:
  - nosql-database
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.CouchDb
    example: |
      ```csharp
      var couchDbContainer = new CouchDbBuilder("couchdb:3.3")
        .Build();
      await couchDbContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.CouchDb
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/couchdb/
    maintainer: core
    example: |
      ```javascript
      const container = await new CouchDBContainer("couchdb:3.5").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/couchdb --save-dev
      ```
description: |
  CouchDB is an open-source document-oriented NoSQL clustered database that allows you to run a single logical database server on any number of servers or VM.
---
