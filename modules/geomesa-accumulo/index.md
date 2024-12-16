---
title: GeoMesa Accumulo
categories:
  - nosql-database
docs:
  - id: java
    url: https://github.com/geomesa/accumulo-uno
    maintainer: community
    example: |
      ```java
      var image = DockerImageName.parse("ghcr.io/geomesa/accumulo-uno:2.1.3");
      var accumulo = new new AccumuloContainer(image).withGeoMesaDistributedRuntime();
      accumulo.start();
      ```
    installation: |
      ```xml
      <dependency>
        <groupId>org.geomesa.testcontainers</groupId>
        <artifactId>testcontainers-accumulo</artifactId>
        <version>1.4.1</version>
        <scope>test</scope>
      </dependency>
      <dependency>
        <groupId>org.locationtech.geomesa</groupId>
        <artifactId>geomesa-accumulo-distributed-runtime_2.12</artifactId>
        <version>5.1.0</version>
        <scope>test</scope>
      </dependency>
      ```
description: |
  GeoMesa is a suite of tools that enables large-scale geospatial querying and analytics on distributed computing systems.
  Apache Accumulo® is a sorted, distributed key/value store that provides robust, scalable data storage and retrieval.
---
