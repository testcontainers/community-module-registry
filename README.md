## Community Module Registry

1. Create `<module-name>.md` file in the `modules` directory with the following content:

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

Format notes:

- Current ID field values: `java`, `go`, `dotnet`, `nodejs`, `python`, `rust`, `haskell`, `ruby`
- Current categories: `cloud`, `message-broker`, `nosql-database`, `other`, `relational-database`, `vector-database`, `web`.
- The descripttion field supports Markdown
- The example fields for each technology stack are injected into Markdown, and should use its language specification

2. Add module logo `[module-name]-mark.svg` to `assets` directory. The logo should be:
* a square SVG version of the module logo with no additional background
* prefer 30x30 for consistency

3. Add `[module-name]-share.png` to `assets` directory. 
* use the square module logo svg scaled to `229x229px` and center it on the blank cube in the share image template, 
use the example `my-module-share-example.png` as a guide
