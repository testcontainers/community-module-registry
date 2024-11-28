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
      var chrome = new BrowserWebDriverContainer<>()
        withCapabilities(new ChromeOptions())
      chrome.start();
      ```
    installation: |
      ```xml
      <dependency>
          <groupId>org.testcontainers</groupId>
          <artifactId>selenium</artifactId>
          <version>1.20.0</version>
          <scope>test</scope>
      </dependency>
      ```
  - id: dotnet
    url: https://www.nuget.org/packages/Testcontainers.WebDriver
    maintainer: core
    example: |
      ```csharp
      var WebDriverContainer = new WebDriverBuilder()
        .WithBrowser(WebDriverBrowser.Chrome)
        .Build();
      await WebDriverContainer.StartAsync();
      ```
    installation: |
      ```bash
      dotnet add package Testcontainers.WebDriver --version 3.9.0
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
    maintainer: community
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
