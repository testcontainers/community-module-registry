---
title: Restate
categories:
  - other
docs:
  - id: nodejs
    url: https://github.com/restatedev/sdk-typescript/tree/main/packages/restate-sdk-testcontainers
    maintainer: community
    example: |
      ```javascript
      import { RestateTestEnvironment } from "@restatedev/restate-sdk-testcontainers";
      import * as clients from "@restatedev/restate-sdk-clients";

      restateTestEnvironment = await RestateTestEnvironment.start(
        (restateServer) => restateServer.bind(counter)
      );
      rs = clients.connect({ url: restateTestEnvironment.baseUrl() });
      ```
description: |
  Restate is the simplest way to write resilient workflows, event-driven applications, and async tasks.
---
