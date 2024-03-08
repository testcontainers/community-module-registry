## Community Module Registry

To add a new module create a new folder with the structure:

```
modules
- <module-name>
  - index.md
  - logo.svg (optional)
```

### index.md

The content of the file should be markdown frontmatter using the following template:

```
---
title: ArangoDB
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/GoodforGod/arangodb-testcontainers
    maintainer: community
    example: |
      ```java
      var arango = new ArangoContainer();
      arango.start();
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/arangodb/
    maintainer: core
    example: |
      ```javascript
      const container = await new ArangoDBContainer().start();
      ```
description: |
  ArangoDB is a free and open-source native graph database system. It supports three data models; graphs, JSON documents, and key/value.
---
```

#### Format notes: 
- Current ID field values: 
  
  `java`, `go`, `dotnet`, `nodejs`, `python`, `rust`, `haskell`, `ruby`

- Current categories: 

  `cloud`, `message-broker`, `nosql-database`, `other`, `relational-database`, `vector-database`, `web`

- Current maintainer values:

  `core`, `community`, `official`

- The description field supports Markdown

- The example fields for each technology stack are injected into Markdown, and should use its language specification

---

### logo.svg

This optional file will be displayed next to the module's name in the catalogue. Logo files should be:

* a square SVG version of the module logo with no additional background
* prefer 60x60 for consistency

If no logo is provided a default image will be used instead:

<img src="https://testcontainers.com/images/modules/none.svg">