---
name: web-vuln-testing
description: >
  This skill covers web vulnerability testing, including XSS, HTML injection, SQL injection, file path traversal, and broken authentication. It provides a comprehensive approach to identifying and exploiting client-side injection flaws.
  Covers: web vuln testing, xss html injection, sql injection testing, html injection testing, file path traversal, idor testing, top web vulnerabilities, broken authentication.
merged_from:
  - xss-html-injection
  - sql-injection-testing
  - html-injection-testing
  - file-path-traversal
  - idor-testing
  - top-web-vulnerabilities
  - broken-authentication

# Overview
Web vulnerability testing is crucial for identifying and exploiting client-side injection flaws. This skill enables systematic detection and exploitation of XSS, HTML injection, and other web vulnerabilities. It provides a comprehensive approach to testing web applications for security weaknesses.

# When to Use / When NOT to Use
Use this skill when testing web applications for security vulnerabilities, such as XSS, HTML injection, and SQL injection. Do not use this skill for testing non-web applications or when the goal is to test for vulnerabilities that are not related to web applications.

# Core Workflow
The core workflow for web vulnerability testing involves the following essential steps:
1. Identify input reflection points in the web application.
2. Perform basic detection testing using test strings and scripts.
3. Conduct advanced testing using various techniques, such as DOM-based testing and event handler testing.
4. Analyze the results and identify potential vulnerabilities.
5. Exploit the identified vulnerabilities to demonstrate the impact.

# Vulnerability Categories
The following table summarizes the vulnerability categories and key techniques:
| Name | What it Tests | Key Technique |
| --- | --- | --- |
| XSS | Cross-site scripting | Injecting scripts into user input fields |
| HTML Injection | HTML injection flaws | Injecting HTML tags into user input fields |
| SQL Injection | SQL injection flaws | Injecting SQL code into user input fields |

# Quick Reference
The following are some of the most-used payloads and patterns:
* `<script>alert('XSS')</script>`
* `<img src=x onerror=alert('XSS')>`
* `<svg onload=alert('XSS')>`
* `body onload=alert('XSS')`

# Reference Files
The following files are recommended for extracting and referencing:
| File | Description |
| --- | --- |
| owasp-injections.md | OWASP injection testing guide |
| xss-techniques.md | XSS techniques and payloads |
| auth-testing.md | Authentication testing guide |
| scanner-usage.md | Web application scanner usage guide |