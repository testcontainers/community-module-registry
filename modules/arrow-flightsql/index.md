---
title: Apache Arrow FlightSQL server
categories:
  - other
docs:
  - id: rust
    url: https://docs.rs/testcontainers-modules/latest/testcontainers_modules/index.html
    maintainer: community
    example: |
      ```rust
      testcontainers_modules::arrow_flightsql::ArrowFlightSQL::default().start()
      ```
    installation: |
      ```bash
      cargo add -F arrow_flightsql --dev testcontainers-modules
      ```
description: |
  Apache Arrow FlightSQL is a high-performance RPC service that exposes SQL query execution and result streaming over Apache Arrow to clients, backed by an existing database or query engine.
---
