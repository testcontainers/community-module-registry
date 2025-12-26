---
title: MSSQL
categories:
  - relational-database
docs:
  - id: java
    url: https://java.testcontainers.org/modules/databases/mssqlserver/
    maintainer: core
    example: |
      ```java
      var mssqlserver = new MSSQLServerContainer()
        .acceptLicense();
      mssqlserver.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-mssqlserver</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: go
    url: https://golang.testcontainers.org/modules/mssql/
    maintainer: core
    example: |
      ```go
      mssqlContainer, err := mssql.Run(context.Background(),
        "mcr.microsoft.com/mssql/server:2022-CU10-ubuntu-22.04",
        mssql.WithAcceptEULA(),
      )
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/mssql
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.MsSql
    maintainer: core
    example: |
      ```csharp
      var msSqlContainer = new MsSqlBuilder("mcr.microsoft.com/mssql/server:2022-CU10-ubuntu-22.04")
        .Build();
      await msSqlContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.MsSql
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/mssqlserver/
    maintainer: core
    example: |
      ```javascript
      const container = await new MSSQLServerContainer("mcr.microsoft.com/mssql/server:2022-CU13-ubuntu-22.04").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/mssqlserver --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/mssql/README.html
    maintainer: core
    example: |
      ```python
      with SqlServerContainer("mcr.microsoft.com/mssql/server:2022-CU12-ubuntu-22.04") as mssql:
          engine = sqlalchemy.create_engine(mssql.get_connection_url())
          with engine.begin() as connection:
              result = connection.execute(sqlalchemy.text("select @@VERSION"))
      ```
    installation: |
      ```bash
      pip install testcontainers[mssql]
      ```
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/mssql_server/struct.MssqlServer.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::mssql_server::MssqlServer::default().with_accept_eula().start()
      ```
    installation: |
      ```bash
      cargo add -F mssql_server --dev testcontainers-modules
      ```
description: |
  Microsoft SQL Server is a relational database management system.
---
