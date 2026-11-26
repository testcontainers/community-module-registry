---
title: RustFS
categories:
  - other
docs:
  - id: java
    url: https://github.com/Vloeiolzlr/testcontainers-rustfs
    maintainer: community
    example: |
      ```java
      var rustfs = new RustFSContainer("rustfs/rustfs:1.0.1");
      rustfs.start();
      String endpoint = rustfs.getS3Url();
      ```
    installation: |
      ```kotlin
      repositories {
          mavenCentral()
          maven("https://jitpack.io")
      }
      dependencies {
          testImplementation("com.github.Vloeiolzlr:testcontainers-rustfs:v0.1.0")
      }
      ```
description: |
  RustFS is an open-source, S3-compatible object storage written in Rust.
  It can stand in for AWS S3, Cloudflare R2 or MinIO in tests.
---
