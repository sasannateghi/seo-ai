import requests
from bs4 import BeautifulSoup

def analyze_site(url):
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    title = soup.title.string if soup.title else ""
    h1 = soup.find("h1")
    h1 = h1.text if h1 else ""

    images = soup.find_all("img")
    missing_alt = len([img for img in images if not img.get("alt")])

    score = 100
    issues = []

    if not title:
        score -= 20
        issues.append("Missing title")

    if not h1:
        score -= 15
        issues.append("Missing H1")

    if missing_alt > 0:
        score -= 10
        issues.append(f"{missing_alt} images missing alt")

    return {
        "score": score,
        "issues": issues
    }
