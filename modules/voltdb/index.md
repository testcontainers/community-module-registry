---
title: VoltDB
categories:
  - relational-database
docs:
  - id: java
    url: https://github.com/VoltDB/volt-testcontainer
    maintainer: official
    example: |
      Use the lone container directly:
      ```java
      var container = new VoltDBContainer(id, licensePath, "voltdb/voltdb-enterprise:14.3.2", hostCount, kfactor, VoltDBCluster.getStartCommand(hostCount), null);
      ```

      or start the whole containerised cluster:
      ```java
      var cluster = new VoltDBCluster(getLicensePath(), "voltdb/voltdb-enterprise:" + getImageVersion(), getExtraLibDirectory());
      ```

      You can also generate a maven project with sample schema, procedures, and tests using this maven archetype:
      ```shell
            mvn -B -ntp archetype:generate \
                  -DarchetypeGroupId=org.voltdb \
                  -DarchetypeArtifactId=voltdb-stored-procedures-maven-quickstart \
                  -DarchetypeVersion=1.6.0 \
                  -DgroupId=org.example.test \
                  -DartifactId=my-voltdb-procedures \
                  -Dpackage=org.example.procedures \
                  -Dversion=1.0-SNAPSHOT
      ```
    installation: |
      ```xml
      <dependency>
        <groupId>org.voltdb</groupId>
        <artifactId>volt-testcontainer</artifactId>
        <version>1.6.0</version>
        <scope>test</scope>
      </dependency>
      ```
description: |
  VoltDB is a commercial in-memory relational database that is scalable and ACID-compliant. Designed to work with mainly OLTP queries. It is designed to be a distributed database with sharding and data replication.
---
