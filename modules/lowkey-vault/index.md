---
title: Lowkey Vault
categories:
  - other
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.LowkeyVault
    maintainer: core
    example: |
      ```csharp
      var lowkeyVaultContainer = new LowkeyVaultBuilder()
        .WithImage("nagyesta/lowkey-vault:2.7.1-ubi9-minimal")
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
