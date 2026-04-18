# 🎣 Phishing Analysis Toolkit

A Python-based phishing investigation tool that extracts URLs from suspicious email text, checks each URL's reputation against the VirusTotal API, and generates a clean structured investigation report.

Built to simulate real SOC analyst workflows for email threat triage and URL reputation analysis.

---

## 🎯 What This Tool Does

Phishing emails are one of the most common attack vectors in real-world incidents. When a suspicious email lands in a SOC queue, analysts need to quickly extract embedded URLs and determine whether they are malicious. This toolkit automates that process:

- Parses raw email text and extracts all embedded URLs using regex
- Submits each URL to the VirusTotal API for reputation analysis
- Polls the API until the analysis is complete
- Generates a clean, readable investigation report showing each URL's status: **clean**, **suspicious**, or **malicious**

---

## 🗂️ Project Structure

```
Phishing-Toolkit/
├── main.py              # Entry point — orchestrates the full analysis pipeline
├── extractor.py         # URL extraction using regex pattern matching
├── reputation.py        # VirusTotal API integration and polling logic
├── report.py            # Report generation — formats results for analyst review
├── requirements.txt     # Python dependencies
├── sample_email.txt     # Sample phishing email for testing
└── test/
    └── test_extractor.py  # Unit tests for URL extraction
```

---

## ⚙️ Setup and Installation

**Requirements:** Python 3.8+

```bash
# Clone the repository
git clone https://github.com/TheCaptainCJ/Phishing-Toolkit.git
cd Phishing-Toolkit/Phishing-Toolkit

# Install dependencies
pip install -r requirements.txt
```

---

## 🔑 API Key Configuration

This tool uses the [VirusTotal API](https://www.virustotal.com/gui/home/upload). You will need a free VirusTotal account to get your own API key.

**Do not hardcode your API key in the source code.** Set it as an environment variable instead:

**Windows (Command Prompt):**
```cmd
set VT_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:VT_API_KEY = "your_api_key_here"
```

**Linux / macOS:**
```bash
export VT_API_KEY=your_api_key_here
```

Then update `reputation.py` to read from the environment:
```python
import os
API_KEY = os.environ.get("VT_API_KEY")
```

---

## 🚀 How to Run

```bash
python main.py
```

The tool will analyze `sample_email.txt` by default. To analyze a different email, update the file path in `main.py`.

**Sample output:**
```
Phishing Analysis Report
------------------------

URL: http://186.169.43.64/a.exe
Status: malicious

URL: https://example.com
Status: clean
```

---

## 📋 Sample Email Format

The tool accepts plain text email files:

```
Hello,

Please review your invoice: http://186.169.43.64/a.exe
Also check our website: https://example.com

Thanks,
Support Team
```

---

## 🧪 Running Tests

```bash
pip install pytest
pytest
```

---

## 🛠️ Skills Demonstrated

- Python scripting and modular code design
- Regex-based URL extraction from unstructured text
- REST API integration with polling logic (VirusTotal v3 API)
- Email threat triage workflow
- Security report generation
- SOC analyst fundamentals: extract → analyze → report

---

## 🔗 How This Connects to Real SOC Work

This toolkit mirrors the workflow documented in my [Email Phishing Alert Investigation Case Study](https://github.com/TheCaptainCJ), where I triaged a live phishing alert in a SIEM environment, extracted and analyzed a suspicious URL, and classified the alert as a false positive using structured investigation methodology.

---

## 🔮 Planned Enhancements

- [ ] Read environment variable for API key automatically
- [ ] Add support for parsing .eml email file format
- [ ] Export report to PDF or CSV
- [ ] Add sender domain reputation check
- [ ] Flag lookalike domains and URL shorteners

---

## 👨‍💻 Author

**Christopher O'Keefe**
IT Professional | Cybersecurity BAS | CompTIA A+ | ISC2 CC
[LinkedIn](https://linkedin.com/in/christopherokeefe93) | [GitHub](https://github.com/TheCaptainCJ)

> ⚠️ This tool is for educational and authorized use only. Only analyze emails and URLs from systems or accounts you own or have explicit permission to investigate.
