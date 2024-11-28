---
title: MinIO
categories:
  - other
docs:
  - id: java
    url: https://java.testcontainers.org/modules/minio/
    maintainer: core
    example: |
      ```java
      var minio = new MinIOContainer("minio/minio:RELEASE.2023-09-04T19-57-37Z");
      minio.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>minio</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/minio/
    maintainer: core
    example: |
      ```go
      minioContainer, err := minio.Run(ctx, "minio/minio:RELEASE.2024-01-16T16-07-38Z")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/minio
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Minio
    maintainer: core
    example: |
      ```csharp
      var minioContainer = new MinioBuilder()
        .WithImage("minio/minio:RELEASE.2023-01-31T02-24-19Z")
        .Build();
      await minioContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Minio --version 3.9.0
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/minio/README.html
    maintainer: core
    example: |
      ```python
      with MinioContainer() as minio:
          client = minio.get_client()
      ```
    installation: |
      ```bash
      pip install testcontainers[minio]
      ```
description: |
  MinIO is a high performance object storage solution. It is API compatible with the Amazon S3 cloud storage service and can handle unstructured data such as photos, videos, log files, backups, and container images with a current maximum supported object size of 5TB.
---
