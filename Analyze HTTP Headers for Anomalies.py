import requests

def analyze_http_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        print("HTTP Headers Analysis:")
        for header, value in headers.items():
            print(f"{header}: {value}")
    except Exception as e:
        print(f"Failed to analyze HTTP headers: {str(e)}")

# Example usage
analyze_http_headers("https://example.com")