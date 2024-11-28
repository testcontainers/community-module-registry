---
title: CockroachDB
categories:
  - relational-database
officialPartner:
  name: Cockroach Labs
  url: https://cockroachlabs.com
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/cockroachdb/
    maintainer: official
    example: |
      ```java
      var cockroach = new new CockroachContainer(DockerImageName.parse("cockroachdb/cockroach:v22.2.3"));
      cockroach.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>cockroachdb</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/databases/cockroachdb/
    maintainer: core
    example: |
      ```go
      cockroachdbContainer, err := cockroachdb.Run(ctx, "cockroachdb/cockroach:v22.2.3")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/cockroachdb
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/cockroachdb/README.html
    maintainer: community
    example: |
      ```python
      with CockroachDBContainer('cockroachdb/cockroach:v24.1.1') as crdb:
        engine = sqlalchemy.create_engine(crdb.get_connection_url())
        with engine.begin() as connection:
          result = connection.execute(sqlalchemy.text("select version()"))
          version, = result.fetchone()
      ```
    installation: |
      ```bash
      pip install testcontainers[cockroachdb]
      ```
description: |
  CockroachDB is an open-source, cloud-native, resilient, distributed SQL database.
---
