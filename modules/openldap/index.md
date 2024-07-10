---
title: OpenLDAP
categories:
  - other
docs:
  - id: go
    url: https://golang.testcontainers.org/modules/openldap/
    maintainer: core
    example: |
      ```go
      openldapContainer, err := openldap.Run(ctx, "bitnami/openldap:2.6.6")
      ```
    installation: |
      ```bash
      go get github.com/testcontainers/testcontainers-go/modules/openldap
      ```
description: |
  OpenLDAP Software is an open source implementation of the Lightweight Directory Access Protocol (LDAP).
---