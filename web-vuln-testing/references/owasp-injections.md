## SQL Injection
### Introduction
SQL injection is a type of web application security vulnerability that allows an attacker to inject malicious SQL code into a web application's database in order to extract or modify sensitive data.

### Payloads
' OR 1=1 --
' UNION SELECT * FROM users --
' DROP TABLE users --
### Techniques
* **Error-based injection**: Injecting SQL code that causes the database to throw an error, revealing sensitive information about the database structure.
* **Union-based injection**: Injecting SQL code that combines the results of two or more SELECT statements, allowing the attacker to extract data from multiple tables.
* **Blind injection**: Injecting SQL code that does not return any data, but instead uses conditional statements to determine the structure of the database.

### Test Cases
* **Login form injection**: Injecting SQL code into a login form to bypass authentication or extract user credentials.
* **Search form injection**: Injecting SQL code into a search form to extract sensitive data or modify database records.
* **Comment form injection**: Injecting SQL code into a comment form to extract sensitive data or modify database records.

### Examples
* **Extracting database version**: Injecting the following SQL code to extract the database version: `SELECT @@VERSION`
* **Extracting user credentials**: Injecting the following SQL code to extract user credentials: `SELECT username, password FROM users`

## HTML Injection
### Introduction
HTML injection is a type of web application security vulnerability that allows an attacker to inject malicious HTML code into a web application, potentially leading to cross-site scripting (XSS) attacks.

### Payloads
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
### Techniques
* **Stored HTML injection**: Injecting HTML code into a web application's database, which is then reflected back to the user.
* **Reflected HTML injection**: Injecting HTML code into a web application's response, which is then executed by the user's browser.
* **DOM-based HTML injection**: Injecting HTML code into a web application's DOM, which is then executed by the user's browser.

### Test Cases
* **Comment form injection**: Injecting HTML code into a comment form to execute malicious JavaScript code.
* **Search form injection**: Injecting HTML code into a search form to execute malicious JavaScript code.
* **User profile injection**: Injecting HTML code into a user profile field to execute malicious JavaScript code.

### Examples
* **Executing JavaScript code**: Injecting the following HTML code to execute malicious JavaScript code: `<script>alert('XSS')</script>`
* **Defacing a website**: Injecting the following HTML code to deface a website: `<h1>Defaced!</h1>`

## Path Traversal
### Introduction
Path traversal is a type of web application security vulnerability that allows an attacker to access files or directories outside of the intended directory structure.

### Payloads
../../../etc/passwd
../../../../../windows/system32/drivers/etc/hosts
### Techniques
* **Directory traversal**: Injecting malicious input to traverse the directory structure and access sensitive files or directories.
* **File inclusion**: Injecting malicious input to include sensitive files or directories in the web application's response.

### Test Cases
* **File upload vulnerability**: Injecting malicious input into a file upload form to access sensitive files or directories.
* **Download vulnerability**: Injecting malicious input into a download form to access sensitive files or directories.
* **Directory listing vulnerability**: Injecting malicious input into a directory listing page to access sensitive files or directories.

### Examples
* **Accessing sensitive files**: Injecting the following input to access sensitive files: `../../../etc/passwd`
* **Executing system commands**: Injecting the following input to execute system commands: `../../../../../windows/system32/cmd.exe`

## IDOR Testing
### Introduction
IDOR (Insecure Direct Object Reference) is a type of web application security vulnerability that allows an attacker to access or modify sensitive data by manipulating the object references in the URL.

### Payloads
http://example.com/user/1
http://example.com/order/123
### Techniques
* **Parameter manipulation**: Manipulating the parameters in the URL to access or modify sensitive data.
* **Object reference manipulation**: Manipulating the object references in the URL to access or modify sensitive data.

### Test Cases
* **User profile vulnerability**: Injecting malicious input into a user profile page to access or modify sensitive user data.
* **Order management vulnerability**: Injecting malicious input into an order management page to access or modify sensitive order data.
* **File management vulnerability**: Injecting malicious input into a file management page to access or modify sensitive files.

### Examples
* **Accessing sensitive user data**: Injecting the following input to access sensitive user data: `http://example.com/user/1`
* **Modifying sensitive order data**: Injecting the following input to modify sensitive order data: `http://example.com/order/123`