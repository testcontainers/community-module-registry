---
title: ScyllaDB
categories:
  - nosql-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/scylladb/
    maintainer: core
    example: |
      ```java
      var container = new ScyllaDBContainer(DockerImageName.parse("scylladb/scylla:6.2"));
      container.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>scylladb</artifactId>
          <version>1.20.5</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/scylladb/
    maintainer: core
    example: |
      ```go
      container, err := scylla.Run(context.Background(), "scylladb/scylla:6.2");
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/scylla
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/scylla/README.html
    maintainer: core
    example: |
      ```python
      with ScyllaContainer(image = "scylladb/scylla:6.2") as scylla:
          cluster = scylla.get_cluster()
      ```
    installation: |
      ```bash
      pip install testcontainers[scylla]
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/scylladb/
    maintainer: core
    example: |
      ```javascript
      const container = await new ScyllaContainer("scylladb/scylla:6.2.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/scylladb --save-dev
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/scylladb/struct.ScyllaDB.html
    maintainer: community
    example: |
      ```rust
      use scylla::client::{session::Session, session_builder::SessionBuilder};
      use testcontainers_modules::{scylladb::ScyllaDB, testcontainers::runners::AsyncRunner};

      #[tokio::test]
      async fn default_scylladb() -> Result<(), Box<dyn std::error::Error + 'static>> {
          let image = ScyllaDB::default();
          let instance = image.start().await?;
          let host = instance.get_host().await?;
          let port = instance.get_host_port_ipv4(9042).await?;
          let hostname = format!("{host}:{port}");
          let session: Session = SessionBuilder::new().known_node(hostname).build().await?;

          let prepared_statement = session
              .prepare("SELECT release_version FROM system.local")
              .await?;
          let rows = session
              .execute_unpaged(&prepared_statement, &[])
              .await?
              .into_rows_result()?;
          let (version,) = rows.single_row::<(String,)>()?;
          assert_eq!(version, "3.0.8");
          Ok(())
      }
      ```
    installation: |
      ```bash
      cargo add -F scylladb --dev testcontainers-modules
      ```
description: |
  ScyllaDB is a distributed NoSQL wide-column database for data-intensive apps that require high performance and low latency.
---
