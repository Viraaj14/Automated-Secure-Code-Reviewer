import re
import json
import sys
import os

class Rule:
    def __init__(self, rule_id, vulnerability, pattern, severity, suggestion, condition=None):
        self.rule_id = rule_id
        self.vulnerability = vulnerability
        self.pattern = re.compile(pattern)
        self.severity = severity
        self.suggestion = suggestion
        self.condition = condition  # e.g., not_contains: @login_required

class Scanner:
    def __init__(self, rules_path):
        self.rules = self.load_rules(rules_path)

    def load_rules(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                rules_data = json.load(f)
            return [Rule(**rule) for rule in rules_data]
        except FileNotFoundError:
            print(f"[ERROR] Rules file not found: {path}")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"[ERROR] Failed to parse rules JSON file: {path}")
            sys.exit(1)

    def check_condition(self, context, condition):
        if not condition:
            return True
        if condition.startswith("not_contains:"):
            keyword = condition.split(":", 1)[1]
            return keyword not in context
        if condition.startswith("contains:"):
            keyword = condition.split(":", 1)[1]
            return keyword in context
        return True  # fallback

    def scan_file(self, filepath):
        findings = []
        if not os.path.isfile(filepath):
            print(f"[ERROR] File to scan not found: {filepath}")
            sys.exit(1)

        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if line.strip().startswith("#"):
                continue  # Skip comment lines
            context = ''.join(lines[max(0, i-2):min(len(lines), i+3)])
            for rule in self.rules:
                if rule.pattern.search(line) and self.check_condition(context, rule.condition):
                    findings.append({
                        'line': i + 1,
                        'rule_id': rule.rule_id,
                        'vulnerability': rule.vulnerability,
                        'severity': rule.severity,
                        'code': line.strip(),
                        'suggestion': rule.suggestion
                    })
        return findings

def main():
    if len(sys.argv) != 3 or sys.argv[1] != 'scan':
        print("Usage: python app.py scan <filename.py>")
        return

    command, filename = sys.argv[1], sys.argv[2]
    scanner = Scanner('rules/Owasp.json')  # Update path if needed
    results = scanner.scan_file(filename)

    if results:
        print(f"\n=== Scan Results for {filename} ===\n")
        for finding in results:
            print(f"[!] Line {finding['line']} | {finding['severity']} | {finding['rule_id']}")
            print(f"    → {finding['vulnerability']}")
            print(f"    → Code: {finding['code']}")
            print(f"    → Fix:  {finding['suggestion']}\n")
    else:
        print("✅ No vulnerabilities found.")

if __name__ == '__main__':
    main()
