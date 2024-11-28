---
title: Trino
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/trino/
    maintainer: core
    example: |
      ```java
      var trino = new TrinoContainer(DockerImageName.parse("trinodb/trino:352"));
      trino.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>trino</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/trino/README.html
    maintainer: community
    example: |
      ```python
      with TrinoContainer("trinodb/trino:451") as trino:
        conn = connect(
          host=trino.get_container_host_ip(),
          port=trino.get_exposed_port(trino.port),
          user="test",
        )
      ```
    installation: |
      ```bash
      pip install testcontainers[trino]
      ```
description: |
  Trino is an open-source distributed SQL query engine designed to query large data sets distributed over one or more heterogeneous data sources.
---
