import requests

def scan_website(url):
    results = []  # List to store detected vulnerabilities

    try:
        # Fetch the webpage
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error if site is unreachable

        # Check for security headers
        headers = response.headers
        missing_headers = []
        security_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security",
        ]
        for header in security_headers:
            if header not in headers:
                missing_headers.append(header)

        if missing_headers:
            results.append(f"⚠️ Missing security headers: {', '.join(missing_headers)}")

        # Check for open directory listing
        if "<title>Index of" in response.text:
            results.append("⚠️ Open directory listing detected!")

    except requests.exceptions.RequestException:
        return ["❌ Error: Unable to scan the website."]

    if not results:
        return ["✅ No vulnerabilities found!"]

    return results
