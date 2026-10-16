---
title: Seq
categories:
  - other
docs:
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Seq
    maintainer: core
    example: |
      ```csharp
      var seqContainer = new SeqBuilder("datalust/seq:2025.2")
        .Build();
      await seqContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Seq
      ```
description: |
  Seq is a self-hosted search, analysis, and alerting server for structured logs and traces. It ingests events over HTTP and the OpenTelemetry Protocol (OTLP) and provides a web interface to query them.
---
