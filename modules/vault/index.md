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
      vaultContainer, err := vault.Run(context.Background(),
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
  - id: nodejs
    url: https://node.testcontainers.org/modules/vault/
    maintainer: core
    example: |
      ```javascript
      const container = await new VaultContainer("hashicorp/vault:1.20.1").withVaultToken(VAULT_TOKEN).start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/vault --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/vault/README.html
    maintainer: core
    example: |
      ```python
      with VaultContainer("hashicorp/vault:1.16.1") as vault_container:
          connection_url = vault_container.get_connection_url()
          client = hvac.Client(url=connection_url, token=vault_container.root_token)
      ```
    installation: |
      ```bash
      pip install testcontainers[vault]
      ```
description: |
  HashiCorp Vault is an identity-based secrets and encryption management system for storing API encryption keys, passwords, and certificates.
---
