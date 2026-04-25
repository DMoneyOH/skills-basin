## Authentication Bypass
### Techniques
* **Password Guessing**: Attempt to login with common passwords or variations of the username
* **Session Fixation**: Fixate a session ID on a user's browser, then use it to gain access after they login
* **Cookie Tampering**: Modify cookie values to bypass authentication or gain elevated privileges
* **Token-based Authentication Bypass**: Exploit vulnerabilities in token-based authentication systems to gain unauthorized access

### Payloads
* `username=admin&password=admin` (simple password guessing)
* `session_id=1234567890abcdef` (session fixation)
* `cookie: auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` (cookie tampering)
* `token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` (token-based authentication bypass)

### Test Cases
1. Attempt to login with a common password (e.g. "password123")
2. Fixate a session ID on a user's browser and attempt to use it to gain access after they login
3. Modify cookie values to bypass authentication or gain elevated privileges
4. Exploit vulnerabilities in token-based authentication systems to gain unauthorized access

## Session Management
### Techniques
* **Session Hijacking**: Steal or predict a valid session ID to gain access to a user's account
* **Session Fixation**: Fixate a session ID on a user's browser, then use it to gain access after they login
* **Cookie Tampering**: Modify cookie values to bypass authentication or gain elevated privileges
* **Session ID Prediction**: Predict a valid session ID to gain access to a user's account

### Payloads
* `session_id=1234567890abcdef` (session hijacking)
* `session_id=1234567890abcdef` (session fixation)
* `cookie: auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` (cookie tampering)
* `session_id= predictedsessionid` (session ID prediction)

### Test Cases
1. Attempt to hijack a valid session ID to gain access to a user's account
2. Fixate a session ID on a user's browser and attempt to use it to gain access after they login
3. Modify cookie values to bypass authentication or gain elevated privileges
4. Predict a valid session ID to gain access to a user's account

## Broken Auth Patterns
### Techniques
* **Weak Passwords**: Use weak passwords or variations of the username to gain access to an account
* **Password Spraying**: Attempt to login with a list of common passwords to gain access to an account
* **Session ID Brute Forcing**: Brute force a valid session ID to gain access to a user's account
* **Token-based Authentication Bypass**: Exploit vulnerabilities in token-based authentication systems to gain unauthorized access

### Payloads
* `username=admin&password=admin` (weak passwords)
* `username=admin&password=password123` (password spraying)
* `session_id=1234567890abcdef` (session ID brute forcing)
* `token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9` (token-based authentication bypass)

### Test Cases
1. Attempt to login with a weak password (e.g. "password123")
2. Attempt to login with a list of common passwords to gain access to an account
3. Brute force a valid session ID to gain access to a user's account
4. Exploit vulnerabilities in token-based authentication systems to gain unauthorized access

### Examples
* **Weak Passwords**: Using a password like "password123" to gain access to an account
* **Password Spraying**: Attempting to login with a list of common passwords like "password123", "qwerty", etc.
* **Session ID Brute Forcing**: Brute forcing a valid session ID like "1234567890abcdef" to gain access to a user's account
* **Token-based Authentication Bypass**: Exploiting vulnerabilities in token-based authentication systems to gain unauthorized access using a token like "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"