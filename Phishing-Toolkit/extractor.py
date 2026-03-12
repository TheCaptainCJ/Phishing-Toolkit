import re

def extract_urls(text):
    pattern = r'https?://[^\s"]+'
    return re.findall(pattern, text)
