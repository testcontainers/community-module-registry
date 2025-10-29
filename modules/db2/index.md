---
title: DB2
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/db2/
    maintainer: core
    example: |
      ```java
      var db2 = new Db2Container(DockerImageName.parse("ibmcom/db2:11.5.0.0a"))
        .acceptLicense();
      db2.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-db2</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.Db2
    maintainer: core
    example: |
      ```csharp
      var db2Container = new Db2Builder()
        .WithImage("icr.io/db2_community/db2:12.1.0.0")
        .Build();
      await db2Container.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.Db2
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/db2/README.html
    maintainer: core
    example: |
      ```python
      with Db2Container("icr.io/db2_community/db2:latest") as db2:
        engine = sqlalchemy.create_engine(db2.get_connection_url())
        with engine.begin() as connection:
          result = connection.execute(sqlalchemy.text("select service_level from sysibmadm.env_inst_info"))
      ```
    installation: |
      ```bash
      pip install testcontainers[db2]
      ```
description: |
  IBM Db2 is a family of data management products, including database servers.
---
