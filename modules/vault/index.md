---
title: Vault
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/vault/
    maintainer: core
    example: |
      ```java
      var vault = new VaultContainer<>(DockerImageName.parse("hashicorp/vault:1.13.0"));
      vault.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>vault</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/vault/
    maintainer: core
    example: |
      ```go
      vaultContainer, err := vault.Run(ctx,
        "hashicorp/vault:1.13.0",
        vault.WithToken("root-token"),
        vault.WithInitCommand("secrets enable transit", "write -f transit/keys/my-key"),
        vault.WithInitCommand("kv put secret/test1 foo1=bar1"),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/vault
      ```
description: |
  HashiCorp Vault is an identity-based secrets and encryption management system for storing API encryption keys, passwords, and certificates.
---
