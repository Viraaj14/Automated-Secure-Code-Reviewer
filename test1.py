import os
import hashlib
import pickle
import requests
from flask import Flask, request

app = Flask(__name__)

# A07-001: Hardcoded password
password = "supersecret123"  # Hardcoded password

# A01-001 & A04-001: Missing authentication on /admin route
@app.route("/admin")
def admin_panel():
    return "Admin Panel Access"

# A03-001: Command injection via os.system
@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")
    os.system(cmd)  # Dangerous

# A08-001: Insecure deserialization using pickle
@app.route("/load_data")
def load_data():
    raw = request.args.get("data")
    return pickle.loads(raw)  # Vulnerable

# A02-001: Use of MD5 hash (weak)
@app.route("/hash_md5")
def hash_md5():
    data = request.args.get("input")
    return hashlib.md5(data.encode()).hexdigest()  # Weak hash

# A02-002: Use of SHA1 hash (still weak)
@app.route("/hash_sha1")
def hash_sha1():
    data = request.args.get("input")
    return hashlib.sha1(data.encode()).hexdigest()  # Still considered weak

# A05-001: Debug mode enabled
@app.route("/debug")
def debug():
    app.run(debug=True)

# A06-001: Simulated vulnerable dependency version in comment (can't really import 0.12 here)
# This simulates a vulnerable use that would be caught via dependency scanner.
# flask==0.12
