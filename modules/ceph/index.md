---
title: Ceph
categories:
  - other
docs:
  - id: java
    url: https://github.com/jarlah/testcontainers-ceph
    maintainer: community
    example: |
      ```java
      CephContainer cephServer = new CephContainer();
      cephServer.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>com.github.jarlah</groupId>
          <artifactId>testcontainers-ceph</artifactId>
          <version>2.0.0</version>
          <scope>test</scope>
      </dependency>
      ```
description: |
  This module allows provisioning the Ceph server as a standalone container within your tests based on [Ceph Demo Container](https://github.com/ceph/ceph-container).

  Ceph, also known as Ceph Storage, is an open-source storage platform designed to provide
  highly scalable object, block, and file storage in a unified system.
  Developed by Inktank Storage (which was acquired by Red Hat in 2014),
  it is intended to help organizations manage vast amounts of data with a high level of fault tolerance and seamless scalability.
  Ceph allows enterprises and service providers to install a distributed storage infrastructure with both performance and resilience.

  Read more:
  - [Ceph Documentation](https://docs.ceph.com/en/latest/start/intro/)
  - [Ceph Container Documentation](https://github.com/ceph/ceph-container/)
---
