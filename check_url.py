import requests

def check_urls(url_list):
    results = {}

    for url in url_list:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results[url] = "Accessible"
            else:
                results[url] = f"Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            results[url] = f"Error: {str(e)}"
    
    return results

urls = ["http://google.com", "http://adamalorna.com", "http://fake3544877363.com"]
results = check_urls(urls)

for url, result in results.items():
    print(f"{url}: {result}")
