🛡️ Python Static Code Security Scanner
A lightweight Python tool to scan source files for common security vulnerabilities using regex-based rules. Inspired by OWASP Top 10 practices.

📁 Structure
bash
Copy
Edit
.
├── app.py                 # Scanner script
├── rules/Owasp.json       # Rule definitions (JSON)
├── test_vulnerable_app.py # Sample vulnerable test file
🚀 Usage
Run the Scanner

bash
Copy
Edit
python app.py scan test_vulnerable_app.py
Expected Output

Shows line number, rule ID, severity, and fix:

pgsql
Copy
Edit
[!] Line 9 | Critical | A07-001
→ Hardcoded Password
→ Code: password = "supersecret123"
→ Fix:  Use env vars instead
🧪 Test File
test_vulnerable_app.py includes:

Hardcoded secrets

Missing auth decorators

Command injection

Insecure deserialization

Weak hashes (MD5, SHA1)

Debug mode

✅ Features
Regex & context-based matching

OWASP-style rule definitions

Easily extensible

Clear CLI results
