---
title: SpiceDB
categories:
  - other
docs:
  - id: go
    url: https://github.com/Mariscal6/testcontainers-spicedb-go
    maintainer: community
    example: |
      ```go
        spiceDBContainer, err := spicedb.Run(context.Background(), "authzed/spicedb:v1.33.0")
      ```
    installation: |
      ```bash
      go get github.com/Mariscal6/testcontainers-spicedb-go
      ```
  - id: python
    url: https://github.com/sohanmaheshwar/testcontainers-spicedb-py
    maintainer: community
    example: |
      ```python
        from testcontainers_spicedb import SpiceDBContainer
        # Using context manager (recommended)
        with SpiceDBContainer(image="authzed/spicedb:v1.47.1") as spicedb:
          endpoint = spicedb.get_endpoint()
          secret_key = spicedb.get_secret_key()

          # Use endpoint and secret_key with your SpiceDB client
          # ...
      ```
    installation: |
      ```bash
      pip install testcontainers-spicedb
      ```    
description: |
  SpiceDB is an Open Source, Google Zanzibar-inspired database for scalably storing and querying fine-grained authorization data. 
---
