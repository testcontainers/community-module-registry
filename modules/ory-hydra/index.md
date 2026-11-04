---
title: Ory Hydra
categories:
  - authentication
  - authorization
docs:
  - id: java
    url: https://github.com/ardetrick/testcontainers-ory-hydra
    maintainer: community
    example: |
      ```java
      var hydra = OryHydraContainer.builder().build();
      hydra.start();
      ```
    installation: |
      ```groovy
      testImplementation 'com.ardetrick.testcontainers:testcontainers-ory-hydra:0.0.5'
      ```
description: |
  Ory Hydra is an OpenID Certified OAuth 2.0 and OpenID Connect provider. This module runs a real Hydra instance for Java integration tests, with sensible defaults and an in-container SQLite database so no external infrastructure is required.
---
