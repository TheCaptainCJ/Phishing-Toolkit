def generate_report(results):
    lines = ["Phishing Analysis Report", "------------------------", ""]

    for item in results:
        lines.append(f"URL: {item['url']}")
        lines.append(f"Status: {item['status']}")
        if item["status"] == "malicious":
            lines.append(f"Threat: {item.get('threat')}")
            lines.append(f"Date Added: {item.get('date_added')}")
        lines.append("")

    return "\n".join(lines)
