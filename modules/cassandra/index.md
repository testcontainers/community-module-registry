---
title: Cassandra
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/cassandra/
    maintainer: core
    example: |
      ```java
      var cassandra = new CassandraContainer<>(DockerImageName.parse("cassandra:3.11.2"));
      cassandra.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>cassandra</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/cassandra/
    maintainer: core
    example: |
      ```go
      cassandraContainer, err := cassandra.Run(context.Background(), "cassandra:4.1.3")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/cassandra
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Cassandra
    maintainer: core
    example: |
      ```csharp
      var cassandraContainer = new CassandraBuilder()
        .WithImage("cassandra:5.0")
        .Build();
      await cassandraContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Cassandra
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/cassandra/
    maintainer: core
    example: |
      ```javascript
      const container = await new CassandraContainer("cassandra:5.0.2").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/cassandra --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/cassandra/README.html
    maintainer: core
    example: |
      ```python
      with CassandraContainer("cassandra:4.1.4") as cassandra, Cluster(
          cassandra.get_contact_points(),
          load_balancing_policy=DCAwareRoundRobinPolicy(cassandra.get_local_datacenter()),
      ) as cluster:
          session = cluster.connect()
          result = session.execute("SELECT release_version FROM system.local;")
          result.one().release_version
      ```
    installation: |
      ```bash
      pip install testcontainers[cassandra]
      ```
description: |
  Cassandra is a free and open source, distributed NoSQL database management system. It is designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.
---
