---
title: Chroma
categories:
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/chromadb/
    maintainer: core
    example: |
      ```java
      var chromadb = new ChromaDBContainer("chromadb/chroma:0.4.22");
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>chromadb</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/chroma/
    maintainer: core
    example: |
      ```go
      chromaContainer, err := chroma.Run(ctx, "chromadb/chroma:0.4.22")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/chroma
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/chromadb/
    maintainer: core
    example: |
      ```javascript
      const container = await new ChromaDBContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/chromadb --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/chroma/README.html
    maintainer: community
    example: |
      ```python
      with ChromaContainer() as chroma:
          config = chroma.get_config()
          client = chromadb.HttpClient(host=config["host"], port=config["port"])
          collection = client.get_or_create_collection("test")
          print(collection.name)
      ```
    installation: |
      ```bash
      pip install testcontainers[chroma]
      ```
description: |
  Chroma is the AI-native open-source embedding database.
---
