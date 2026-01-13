---
title: Docling
categories:
  - web
  - cloud
docs:
  - id: java
    url: https://docling-project.github.io/docling-java/current/testcontainers/
    maintainer: official
    example: |
      ```java
      var doclingContainer = new DoclingServeContainer(
        DoclingServeContainerConfig.builder()
          .image(DoclingServeContainerConfig.DOCLING_IMAGE)
          .enableUi(true)
          .build()
      );
      doclingContainer.start();
      ```
    installation: |
      ```xml
      <dependency>
        <groupId>ai.docling</groupId>
        <artifactId>docling-testcontainers</artifactId>
        <version>${docling.version}</version>
        <scope>test</scope>
      </dependency>
      ```
description: |
  The `docling-testcontainers` module provides a ready-to-use Testcontainers integration for running a [Docling Serve](https://github.com/docling-project/docling-serve) instance, wrapping the official container image and exposing a simple Java API.

  Use this module when:
  - You want end-to-end tests that run against a real Docling Serve instance.
  - You need a portable, reliable way to boot Docling Serve in your CI pipelines.
  - You want a conventient and familiar Java API to tweak the container image, environment variables, startup timeout, and optional UI.
---