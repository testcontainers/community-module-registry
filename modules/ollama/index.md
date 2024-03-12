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
  - id: go
    url: https://golang.testcontainers.org/modules/ollama/
    maintainer: core
    example: |
      ```go
      ollamaContainer, err := ollama.RunContainer(ctx,
              testcontainers.WithImage("ollama/ollama:0.1.26"))
      if err != nil {
            log.Fatalf("failed to start container: %s", err)
      }
      _, _, err = ollamaContainer.Exec(ctx, []string{"ollama", "pull", "all-minilm"})
      ```
description: |
  Ollama makes it easy to get up and running with large language models locally.
---