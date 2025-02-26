---
title: Ollama
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/ollama/
    maintainer: core
    example: |
      ```java
      var ollama = new OllamaContainer("ollama/ollama:0.1.26");
      ollama.start();
      ollama.execInContainer("ollama", "pull", "all-minilm");
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>ollama</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/ollama/
    maintainer: core
    example: |
      ```go
      ollamaContainer, err := ollama.Run(context.Background(), "ollama/ollama:0.1.26")
      if err != nil {
            log.Fatalf("failed to start container: %s", err)
      }
      _, _, err = ollamaContainer.Exec(context.Background(), []string{"ollama", "pull", "all-minilm"})
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/ollama
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/ollama/
    maintainer: core
    example: |
      ```javascript
      const container = await new OllamaContainer().start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/ollama --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/ollama/README.html
    maintainer: core
    example: |
      ```python
      with OllamaContainer() as ollama:
          endpoint = ollama.get_endpoint()
      ```
    installation: |
      ```bash
      pip install testcontainers[ollama]
      ```
description: |
  Ollama makes it easy to get up and running with large language models locally.
---
