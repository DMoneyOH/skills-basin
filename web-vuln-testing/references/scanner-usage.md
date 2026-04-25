# Vulnerability Scanner Usage
## Scanning Techniques
* Identify input reflection points: search boxes, query parameters, user profile fields, URL fragments, error messages
* Basic detection testing: insert test strings to observe application behavior
* Monitor for raw HTML reflection, partial encoding, JavaScript execution, DOM modifications

## Scanning Tools
* Burp Suite: for request analysis, vulnerability detection, and exploitation
* Browser developer tools: for request analysis, JavaScript console, and DOM inspection
* Vulnerability scanners: for automated detection of XSS, SQL injection, and other vulnerabilities

## Scanning Examples
* Scan for XSS vulnerabilities using Burp Suite's Intruder tool
* Use browser developer tools to analyze request and response headers, cookies, and JavaScript execution
* Run automated vulnerability scans using tools like OWASP ZAP, Nessus, or Qualys

# Burp Suite
## Burp Suite Tools
* **Intruder**: for vulnerability detection and exploitation
* **Repeater**: for modifying and re-sending requests
* **Sequencer**: for analyzing session token randomness
* **Decoder**: for decoding and encoding data

## Burp Suite Techniques
* **Request analysis**: analyze request and response headers, cookies, and body
* **Vulnerability detection**: use Intruder tool to detect XSS, SQL injection, and other vulnerabilities
* **Exploitation**: use Repeater tool to modify and re-send requests, exploit vulnerabilities

## Burp Suite Examples
* Use Intruder tool to detect XSS vulnerabilities in a web application
* Use Repeater tool to exploit a SQL injection vulnerability
* Use Sequencer tool to analyze session token randomness

# Automated Testing Tools
## Automated Testing Techniques
* **Fuzz testing**: provide invalid, unexpected, or random data to a web application
* **Penetration testing**: simulate real-world attacks on a web application
* **Vulnerability scanning**: use automated tools to detect vulnerabilities

## Automated Testing Tools
* **OWASP ZAP**: for vulnerability detection and exploitation
* **Selenium**: for automating web browser interactions
* **Cucumber**: for behavior-driven development and testing

## Automated Testing Examples
* Use OWASP ZAP to detect XSS vulnerabilities in a web application
* Use Selenium to automate web browser interactions, test web application functionality
* Use Cucumber to write behavior-driven tests for a web application

# Payloads and Test Cases
## XSS Payloads
* `<script>alert('XSS')</script>`
* `<img src=x onerror=alert('XSS')>`
* `<svg onload=alert('XSS')>`
* `<body onload=alert('XSS')>`

## SQL Injection Payloads
* `OR 1=1`
* `UNION SELECT * FROM users`
* `DROP TABLE users`

## Test Cases
* Test for XSS vulnerabilities in user input fields
* Test for SQL injection vulnerabilities in query parameters
* Test for file inclusion vulnerabilities in URL parameters

# Techniques
## Input Validation
* Validate user input data to prevent XSS and SQL injection attacks
* Use whitelisting to allow only expected input data

## Output Encoding
* Encode output data to prevent XSS attacks
* Use HTML encoding to prevent JavaScript execution

## Session Management
* Use secure session management practices to prevent session hijacking
* Use secure cookie attributes to prevent cookie theft

# Examples
* Example of a stored XSS vulnerability: a web application stores user input data in a database, and an attacker injects malicious JavaScript code
* Example of a reflected XSS vulnerability: a web application reflects user input data in a response, and an attacker injects malicious JavaScript code
* Example of a DOM-based XSS vulnerability: a web application uses client-side JavaScript to process user input data, and an attacker injects malicious JavaScript code