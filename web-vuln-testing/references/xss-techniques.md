# Cross-Site Scripting (XSS) and Broken Authentication Testing
## XSS Testing

### Payloads
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
### Techniques
#### Identify Input Reflection Points
Locate areas where user input is reflected in responses:
- Search boxes and query parameters
- User profile fields (name, bio, comments)
- URL fragments and hash values
- Error messages displaying user input
- Form fields with client-side validation only
- Hidden form fields and parameters
- HTTP headers (User-Agent, Referer)

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

### Test Cases
1. **Stored XSS**: Test user input fields that store data, such as comment sections, user profiles, and product reviews.
2. **Reflected XSS**: Test user input fields that reflect data, such as search boxes, error messages, and URL parameters.
3. **DOM-Based XSS**: Test client-side JavaScript code that processes user input.

## Broken Authentication Testing

### Techniques
1. **Session Hijacking**: Test for vulnerabilities that allow an attacker to hijack a user's session.
2. **Password Guessing**: Test for vulnerabilities that allow an attacker to guess a user's password.
3. **Session Fixation**: Test for vulnerabilities that allow an attacker to fixate a user's session.

### Test Cases
1. **Login Functionality**: Test login functionality to ensure that it is secure and doesn't allow attackers to guess or hijack user sessions.
2. **Session Management**: Test session management to ensure that it is secure and doesn't allow attackers to fixate or hijack user sessions.
3. **Password Storage**: Test password storage to ensure that it is secure and doesn't allow attackers to obtain user passwords.

### Examples
1. **SQL Injection**: Test for SQL injection vulnerabilities that allow an attacker to access user data.
2. **Cross-Site Request Forgery (CSRF)**: Test for CSRF vulnerabilities that allow an attacker to perform actions on behalf of a user.
3. **Insecure Direct Object References (IDOR)**: Test for IDOR vulnerabilities that allow an attacker to access user data.