from extractor import extract_urls

def test_extract_urls():
    text = "Visit https://example.com and http://test.com"
    urls = extract_urls(text)
    assert len(urls) == 2
    assert "https://example.com" in urls
    assert "http://test.com" in urls
