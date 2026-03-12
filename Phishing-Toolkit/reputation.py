import requests
import time

API_KEY = "aaacab3699bc87a9a5cef0921735d73339fada23fbfd8bdc7af88dd13f0f65f8"

def check_url_reputation(url):
    headers = {
        "x-apikey": API_KEY
    }

    # Step 1: Submit URL for analysis
    submit_url = "https://www.virustotal.com/api/v3/urls"
    response = requests.post(submit_url, headers=headers, data={"url": url})

    if response.status_code != 200:
        return {"url": url, "status": "error"}

    analysis_id = response.json()["data"]["id"]

    # Step 2: Retrieve analysis results
    analysis_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"

    # Poll until analysis is ready
    while True:
        result = requests.get(analysis_url, headers=headers).json()
        status = result["data"]["attributes"]["status"]

        if status == "completed":
            break

        time.sleep(1)

    stats = result["data"]["attributes"]["stats"]
    malicious = stats.get("malicious", 0)
    suspicious = stats.get("suspicious", 0)

    if malicious > 0:
        return {"url": url, "status": "malicious", "malicious_count": malicious}

    if suspicious > 0:
        return {"url": url, "status": "suspicious", "suspicious_count": suspicious}

    return {"url": url, "status": "clean"}


