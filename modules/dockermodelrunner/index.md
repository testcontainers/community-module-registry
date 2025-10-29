---
title: Docker Model Runner
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/docker_model_runner/
    maintainer: core
    example: |
      ```java
      DockerModelRunnerContainer dmr = new DockerModelRunnerContainer("alpine/socat:1.7.4.3-r0");

      dmr.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/dockermodelrunner/
    maintainer: core
    example: |
      ```go
      dmrContainer, err := dockermodelrunner.Run(context.Background())
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/dockermodelrunner
      ```
description: |
    Docker Model Runner is a faster, simpler way to run and test AI models locally, right from your existing workflow.
---
