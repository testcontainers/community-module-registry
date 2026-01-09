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
          <artifactId>testcontainers-minio</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/minio/
    maintainer: core
    example: |
      ```go
      minioContainer, err := minio.Run(context.Background(), "minio/minio:RELEASE.2024-01-16T16-07-38Z")
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
      var minioContainer = new MinioBuilder("minio/minio:RELEASE.2023-01-31T02-24-19Z")
        .Build();
      await minioContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Minio
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
  - id: nodejs
    url: https://node.testcontainers.org/modules/minio/
    maintainer: core
    example: |
      ```javascript
      const container = await new MinioContainer("minio/minio:RELEASE.2024-12-13T22-19-12Z").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/minio --save-dev
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/minio/struct.MinIO.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::minio::MinIO::default().start()
      ```
    installation: |
      ```bash
      cargo add -F minio --dev testcontainers-modules
      ```
description: |
  MinIO is a high performance object storage solution. It is API compatible with the Amazon S3 cloud storage service and can handle unstructured data such as photos, videos, log files, backups, and container images with a current maximum supported object size of 5TB.
---
