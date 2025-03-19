from django.shortcuts import render
from .scanner import scan_website  # Import scanning function

def scan_view(request):
    if request.method == "POST":
        url = request.POST.get("url")  # Get user-entered URL
        if url:
            issues = scan_website(url)  # Scan for vulnerabilities
            return render(request, "scan_results.html", {"url": url, "issues": issues})

    return render(request, "scanner_form.html")  # Show input form
