---
title: Google Cloud
categories:
  - cloud
docs:
  - id: java
    url: https://java.testcontainers.org/modules/gcloud/
    maintainer: core
    example: |
      ```java
      var bigtable = new BigtableEmulatorContainer(
        DockerImageName.parse("gcr.io/google.com/cloudsdktool/google-cloud-cli:380.0.0-emulators")
      );
      bigtable.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>gcloud</artifactId>
          <version>1.19.8</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/gcloud/
    maintainer: core
    example: |
      ```go
      bigTableContainer, err := gcloud.RunBigTableContainer(
        ctx,
        testcontainers.WithImage("gcr.io/google.com/cloudsdktool/cloud-sdk:380.0.0-emulators"),
        gcloud.WithProjectID("bigtable-project"),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/gcloud
      ```
description: |
  Google's Cloud SDK provides a platform to work with the services provided through their Cloud Platform.
  Currently, this module supports Bigtable, Datastore, Firestore, Spanner, and Pub/Sub emulators.
---