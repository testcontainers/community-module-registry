---
title: SFTP
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/sftp/
    maintainer: core
    example: |
      ```go
      sftpContainer, err := sftp.Run(context.Background(), "atmoz/sftp:latest")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/sftp
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Sftp
    maintainer: core
    example: |
      ```csharp
      var sftpContainer = new SftpBuilder("atmoz/sftp:alpine")
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
