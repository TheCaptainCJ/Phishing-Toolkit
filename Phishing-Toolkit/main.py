from extractor import extract_urls
from reputation import check_url_reputation
from report import generate_report

def analyze_email(file_path):
    with open(file_path, "r") as f:
        text = f.read()

    urls = extract_urls(text)
    results = [check_url_reputation(url) for url in urls]
    report = generate_report(results)

    print(report)

if __name__ == "__main__":
    analyze_email("sample_email.txt")
