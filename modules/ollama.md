---
title: Ollama
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/ollama/
    example: |
      ```java
      var ollama = new OllamaContainer("ollama/ollama:0.1.26");
      ollama.start();
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/ollama/
    example: |
      ```go
      ollamaContainer, err := ollama.RunContainer(ctx, testcontainers.WithImage("ollama/ollama:0.1.26"))
      ```
description: |
  Ollama makes it easy to get up and running with large language models locally.
---