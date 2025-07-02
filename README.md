# 🛡️ Python Static Code Security Scanner

A lightweight Python tool to scan source files for common security vulnerabilities using regex-based rules. Inspired by **OWASP Top 10** practices.

---

## 📁 Project Structure

.
├── app.py # Scanner script
├── rules/Owasp.json # Rule definitions (JSON format)
├── test_vulnerable_app.py # Sample vulnerable test file

---

## 🚀 How to Use

1. **Run the Scanner:**

```bash
python app.py scan test_vulnerable_app.py
Sample Output:

pgsql
Copy
Edit
[!] Line 9 | Critical | A07-001
→ Hardcoded Password
→ Code: password = "supersecret123"
→ Fix:  Use environment variables instead
🧪 Test File
test_vulnerable_app.py includes:

Hardcoded passwords/API keys

Command injection

Missing authentication decorators

Weak hashing (MD5, SHA1)

Insecure deserialization (pickle)

Debug mode enabled

Use it to validate rule detection.

✅ Features
Regex & context-aware rule matching

OWASP-style vulnerability coverage

Clear CLI output

Easily customizable via rules/Owasp.json
