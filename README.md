# 🛡️ PhishGuard

### URL Security Analyzer

PhishGuard is a Python-based cybersecurity project that analyzes website URLs for common phishing indicators and provides a simple risk assessment.

## 🎯 Objective

The goal of PhishGuard is to help users identify potentially suspicious URLs before visiting them.

## ⚙️ How It Works

1. User enters a website URL.
2. PhishGuard analyzes the URL.
3. The system checks for common suspicious characteristics.
4. A risk score is calculated.
5. The detected security indicators are displayed to the user.

## 🔍 Detection Checks

PhishGuard currently checks for:

- Missing HTTPS
- IP addresses used instead of domain names
- Unusually long URLs
- Suspicious keywords
- Excessive subdomains

## 🧰 Technologies Used

- Python
- Flask
- HTML
- CSS
- URL Parsing
- Regular Expressions

## 📁 Project Structure

```text
PhishGuard/
├── app.py
├── detector.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── style.css
