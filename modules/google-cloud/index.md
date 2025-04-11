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
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/gcloud/
    maintainer: core
    example: |
      ```go
      datastoreContainer, err := tcdatastore.Run(
          context.Background(),
          "gcr.io/google.com/cloudsdktool/cloud-sdk:380.0.0-emulators",
          tcdatastore.WithProjectID("datastore-project"),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/gcloud
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/gcloud/
    maintainer: core
    example: |
      ```javascript
      const datastoreEmulatorContainer = await new DatastoreEmulatorContainer(
        "gcr.io/google.com/cloudsdktool/cloud-sdk"
      ).start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/gcloud --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/google/README.html
    maintainer: core
    example: |
      ```python
      with DatastoreContainer() as datastore:
          datastore_client = datastore.get_datastore_client()
      ```
    installation: |
      ```bash
      pip install testcontainers[google]
      ```
description: |
  Google's Cloud SDK provides a platform to work with the services provided through their Cloud Platform.
  Currently, this module supports Bigtable, Datastore, Firestore, Spanner, and Pub/Sub emulators.
---
