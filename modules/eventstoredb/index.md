---
title: EventStoreDB
categories:
  - nosql-database
docs:
  - id: nodejs
    url: https://node.testcontainers.org/modules/eventstoredb/
    maintainer: core
    example: |
      ```javascript
      const container = await new EventStoreDBContainer("eventstore/eventstore:24.10").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/eventstoredb --save-dev
      ```
description: |
  EventStoreDB is an event sourcing database that stores data in streams of immutable events.
---
