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
          <artifactId>testcontainers-ollama</artifactId>
          <version>2.0.1</version>
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
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Ollama
    maintainer: core
    example: |
      ```csharp
      var ollamaContainer = new OllamaBuilder()
        .WithImage("ollama/ollama:0.6.6")
        .Build();
      await ollamaContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Ollama
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/ollama/
    maintainer: core
    example: |
      ```javascript
      const container = await new OllamaContainer("ollama/ollama:0.1.44").start();
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
