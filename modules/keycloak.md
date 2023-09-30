---
title: Keycloak
categories:
  - other
docs:
  - id: go
    url: https://github.com/stillya/testcontainers-keycloak
    isThirdParty: true
    example: |
      ```golang
       ctx := context.Background()
       container, err := keycloak.RunContainer(ctx,
         testcontainers.WithWaitStrategy(wait.ForListeningPort("8080/tcp")),
         keycloak.WithContextPath("/auth"),
         keycloak.WithRealmImportFile("../testdata/realm-export.json"),
         keycloak.WithAdminUsername("admin"),
         keycloak.WithAdminPassword("admin"),
       )
       if err != nil {
         t.Fatal(err)
       }
       t.Cleanup(func() {
         if err := container.Terminate(ctx); err != nil {
         t.Fatalf("failed to terminate container: %s", err)
         }
       })
      ```
description: |
  Keycloak is an open source identity and access management application that provides user federation, strong authentication, user management, fine-grained authorization, and more.
---
