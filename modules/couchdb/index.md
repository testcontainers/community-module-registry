---
title: CouchDB
categories:
  - nosql-database
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.CouchDb
    example: |
      ```csharp
      var couchDbContainer = new CouchDbBuilder()
        .WithImage("couchdb:3.3")
        .Build();
      await couchDbContainer.StartAsync();
      ```
description: |
  CouchDB is an open-source document-oriented NoSQL clustered database that allows you to run a single logical database server on any number of servers or VM.
---