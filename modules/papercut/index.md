---
title: Papercut SMTP
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/papercutsmtp/
    maintainer: core
    example: |
      ```go
      papercutContainer, err := papercutsmtp.Run(context.Background(), "changemakerstudiosus/papercut-smtp:latest")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/papercutsmtp
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Papercut
    maintainer: core
    example: |
      ```csharp
      var papercutContainer = new PapercutBuilder("changemakerstudiosus/papercut-smtp:7.0")
        .Build();
      await papercutContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Papercut
      ```
description: |
  Papercut SMTP is a 2-in-1 quick email viewer AND built-in SMTP server (designed to receive messages only). Papercut SMTP doesn't enforce any restrictions on how you prepare your email, but it allows you to view the whole email-chilada: body, HTML, headers, and attachment right down to the naughty raw encoded bits. Papercut can be configured to run on startup and sit quietly (minimized in the tray) only providing a notification when a new message has arrived.
---
