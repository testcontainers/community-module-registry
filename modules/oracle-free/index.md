---
title: Oracle Free
categories:
  - relational-database
  - vector-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/oraclefree/
    maintainer: core
    example: |
      ```java
      var oracle = new OracleContainer("gvenzl/oracle-free:23.4-slim-faststart");
      oracle.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>oracle-free</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/oracle-free/README.html
    maintainer: core
    example: |
      ```python
      with OracleDbContainer() as oracle:
          engine = sqlalchemy.create_engine(oracle.get_connection_url())
      ```
    installation: |
      ```bash
      pip install testcontainers[oracle-free]
      ```
description: |
  Oracle Database Free is a free edition of the world's leading database specifically designed for anybody to develop, learn, and run on Oracle Database for free.
---
