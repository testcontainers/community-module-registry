---
title: Lowkey Vault
categories:
  - cloud
docs:
  - id: java
    url: https://github.com/nagyesta/lowkey-vault/tree/main/lowkey-vault-testcontainers
    maintainer: community
    example: |
      ```java
      var lowkeyVault = LowkeyVaultContainerBuilder
        .lowkeyVault("nagyesta/lowkey-vault:4.0.0-ubi9-minimal")
        .build();
      lowkeyVault.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>com.github.nagyesta.lowkey-vault</groupId>
          <artifactId>lowkey-vault-testcontainers</artifactId>
          <version>RELEASE</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.LowkeyVault
    maintainer: core
    example: |
      ```csharp
      var lowkeyVaultContainer = new LowkeyVaultBuilder()
        .WithImage("nagyesta/lowkey-vault:4.0.0-ubi9-minimal")
        .Build();
      await lowkeyVaultContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.LowkeyVault
      ```
description: |
  Lowkey Vault is a test double (fake object) aspiring to be compatible with Azure Key Vault REST APIs.
---
