---
title: Presto
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/presto/
    maintainer: core
    example: |
      ```java
      var presto = new PrestoContainer(DockerImageName.parse("ghcr.io/trinodb/presto:344"));
      presto.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-presto</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/presto/
    maintainer: core
    example: |
      ```go
      prestoContainer, err := presto.Run(context.Background(), "prestodb/presto:0.289")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/presto
      ```

description: |
  Presto is a distributed query engine for big data using the SQL query language. Its architecture allows users to query data sources such as Hadoop, Cassandra, Kafka, AWS S3, Alluxio, MySQL, MongoDB and Teradata, and allows use of multiple data sources within a query.
---
