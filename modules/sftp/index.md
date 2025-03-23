---
title: SFTP
categories:
  - other
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Sftp
    maintainer: core
    example: |
      ```csharp
      var sftpContainer = new SftpBuilder()
        .WithImage("atmoz/sftp:alpine")
        .Build();
      await sftpContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Sftp
      ```
description: |
  Easy to use SFTP (SSH File Transfer Protocol) server with OpenSSH.
---
