## Community Module Registry

1. Create a `<module-name>.md` file in the `modules` directory with the following content:

```
---
title: ArangoDB
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/GoodforGod/arangodb-testcontainers
    isThirdParty: true
    example: |
      ```java
      var arango = new ArangoContainer();
      arango.start();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/arangodb/
    example: |
      ```javascript
      const container = await new ArangoDBContainer().start();
      ```
description: |
  ArangoDB is a free and open-source native graph database system. It supports three data models; graphs, JSON documents, and key/value.
---
```
