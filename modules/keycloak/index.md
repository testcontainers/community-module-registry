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
  - id: go
    url: https://github.com/stillya/testcontainers-keycloak
    maintainer: community
    example: |
      ```go
      keycloakContainer, err := keycloak.RunContainer(ctx,
        testcontainers.WithImage("quay.io/keycloak/keycloak:21.1"),
        testcontainers.WithWaitStrategy(wait.ForListeningPort("8080/tcp")),
        keycloak.WithContextPath("/auth"),
        keycloak.WithRealmImportFile("../testdata/realm-export.json"),
        keycloak.WithAdminUsername("admin"),
        keycloak.WithAdminPassword("admin"),
      )
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Keycloak
    maintainer: core
    example: |
      ```csharp
      var keycloakContainer = new KeycloakBuilder()
        .WithImage("quay.io/keycloak/keycloak:21.1")
        .Build();
      await keycloakContainer.StartAsync();
      ```
description: |
  Keycloak is an open source identity and access management application that provides user federation, strong authentication, user management, fine-grained authorization, and more.
---
