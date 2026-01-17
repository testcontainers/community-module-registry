## Community Module Registry [![Netlify Status](https://api.netlify.com/api/v1/badges/bec91239-ecd9-4f28-8908-ee63623ac60a/deploy-status)](https://app.netlify.com/sites/testcontainers-site/deploys)

To add a new module create a new folder with the structure:

```yaml
modules
- <module-name>
  - index.md
  - logo.svg (optional)
```

### index.md

The content of the file should be markdown frontmatter using the following template:

```yaml
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

The project uses `yamllint` to format the modules, so make sure the file is correctly formatted. Please run the following command to check the files:

```bash
docker run --rm -t -v $(pwd):/data cytopia/yamllint:latest --no-warnings -d .yamllint .
```

- Current ID field values: 
  
  `java`, `go`, `dotnet`, `nodejs`, `python`, `rust`, `haskell`, `ruby`, `r`

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
