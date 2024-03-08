---
title: Dex
categories:
  - other
docs:
  - id: java
    url: https://github.com/Kehrlann/testcontainers-dex
    maintainer: community
    example: |
      ```java
      var container = new DexContainer(DexContainer.DEFAULT_IMAGE_NAME.withTag(DexContainer.DEFAULT_TAG))
            .withClient(new DexContainer.Client("client-1", "client-1-secret", "https://one.example.com/authorized"))
            .withUser(new DexContainer.User("alice", "alice@example.com", "alice-password"));
      container.start();
      ```
description: |
  Dex is an identity service that uses OpenID Connect to drive authentication for other apps.

  Read more:
  - [Official website](https://dexidp.io)
  - [Documentation](https://dexidp.io/docs/)
  - [Github project](https://github.com/dexidp/dex)
---
