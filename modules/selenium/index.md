---
title: Selenium
categories:
  - web
docs:
  - id: java
    url: https://java.testcontainers.org/modules/webdriver_containers/
    maintainer: core
    example: |
      ```java
      var chrome = new BrowserWebDriverContainer("selenium/standalone-chrome:4.13.0")
      chrome.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>testcontainers-selenium</artifactId>
          <version>2.0.1</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.WebDriver
    maintainer: core
    example: |
      ```csharp
      var WebDriverContainer = new WebDriverBuilder("selenium/standalone-chrome:110.0")
        .Build();
      await WebDriverContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.WebDriver
      ```
  - id: nodejs
    url: https://node.testcontainers.org/modules/selenium/
    maintainer: core
    example: |
      ```javascript
      const container = await new SeleniumContainer("selenium/standalone-chrome:112.0").start();
      ```
    installation: |
      ```bash
      npm install @testcontainers/selenium --save-dev
      ```
  - id: python
    url: https://testcontainers-python.readthedocs.io/en/latest/modules/selenium/README.html
    maintainer: core
    example: |
      ```python
      with BrowserWebDriverContainer(DesiredCapabilities.CHROME) as chrome:
          webdriver = chrome.get_driver()
      ```
    installation: |
      ```bash
      pip install testcontainers[selenium]
      ```
description: |
  Selenium is an umbrella project encapsulating a variety of tools and libraries enabling web browser automation. Selenium specifically provides an infrastructure for the W3C WebDriver specification — a platform and language-neutral coding interface compatible with all major web browsers.
---
