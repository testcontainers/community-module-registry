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
      openldapContainer, err := openldap.RunContainer(ctx, testcontainers.WithImage("bitnami/openldap:2.6.6"))
      ```
description: |
  OpenLDAP Software is an open source implementation of the Lightweight Directory Access Protocol (LDAP).
---