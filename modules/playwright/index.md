---
title: Playwright
categories:
  - web
docs:
  - id: nodejs
    url: https://github.com/javierlopezdeancos/testcontainers-node-playwright
    maintainer: community
    example: |
      ```javascript
      import path from "path";
      import { PlaywrightContainer } from "@testcontainers/playwright";

      const PLAYWRIGHT_PROJECT_TESTS_TO_RUN_INTO_THE_CONTAINER = path.resolve(__dirname, "..", "example-project");

      const startedPlaywrightContainer = await new PlaywrightContainer(
        "mcr.microsoft.com/playwright:v1.44.0-jammy",
        PLAYWRIGHT_PROJECT_TESTS_TO_RUN_INTO_THE_CONTAINER,
      ).start();

      const { output, exitCode } = await startedPlaywrightContainer.exec(["npx", "playwright", "test"]);
      ```
description: |
  Playwright enables reliable end-to-end testing for modern web apps.
---
