from urllib.parse import urlparse
import re

SUSPICIOUS_WORDS = [
    "login", "verify", "verification",
    "secure", "account", "update",
    "bank", "password", "confirm",
    "signin", "wallet"
]


def analyze_url(url):
    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)
    hostname = parsed.hostname or ""

    score = 0
    reasons = []

    if parsed.scheme != "https":
        score += 20
        reasons.append("Website does not use HTTPS.")

    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", hostname):
        score += 30
        reasons.append(
            "URL uses an IP address instead of a domain name."
        )

    if len(url) > 100:
        score += 15
        reasons.append("URL is unusually long.")

    found_words = [
        word for word in SUSPICIOUS_WORDS
        if word in url.lower()
    ]

    if found_words:
        score += min(len(found_words) * 5, 20)
        reasons.append(
            "Suspicious keywords found: "
            + ", ".join(found_words)
        )

    if hostname.count(".") >= 3:
        score += 15
        reasons.append(
            "URL contains an unusually high number of subdomains."
        )

    if score >= 50:
        risk = "HIGH RISK"
    elif score >= 25:
        risk = "SUSPICIOUS"
    else:
        risk = "LOW RISK"

    return {
        "url": url,
        "score": min(score, 100),
        "risk": risk,
        "reasons": reasons
    }
