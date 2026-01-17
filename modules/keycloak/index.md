---
title: Keycloak
categories:
  - other
docs:
  - id: java
    url: https://github.com/dasniko/testcontainers-keycloak
    maintainer: community
    example: |
      ```java
      var keycloak = new KeycloakContainer();
      keycloak.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>com.github.dasniko</groupId>
          <artifactId>testcontainers-keycloak</artifactId>
          <version>3.4.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://github.com/stillya/testcontainers-keycloak
    maintainer: community
    example: |
      ```go
      keycloakContainer, err := keycloak.RunContainer(context.Background(),
        testcontainers.WithImage("quay.io/keycloak/keycloak:21.1"),
        testcontainers.WithWaitStrategy(wait.ForListeningPort("8080/tcp")),
        keycloak.WithContextPath("/auth"),
        keycloak.WithRealmImportFile("../testdata/realm-export.json"),
        keycloak.WithAdminUsername("admin"),
        keycloak.WithAdminPassword("admin"),
      )
      ```
    installation: |
      ```bash
      go get github.com/stillya/testcontainers-keycloak
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Keycloak
    maintainer: core
    example: |
      ```csharp
      var keycloakContainer = new KeycloakBuilder("quay.io/keycloak/keycloak:21.1")
        .Build();
      await keycloakContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Keycloak
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/keycloak/README.html
    maintainer: core
    example: |
      ```python
      with KeycloakContainer() as keycloak:
          client = keycloak.get_client()
      ```
    installation: |
      ```bash
      pip install testcontainers[keycloak]
      ```
description: |
  Keycloak is an open source identity and access management application that provides user federation, strong authentication, user management, fine-grained authorization, and more.
---
