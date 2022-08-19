import requests

get_response = requests.get("http://books.toscrape.com")

print(f"### STATUS CODE: {get_response.status_code}")
print(f"### HEADERS: {get_response.headers}")
print(f"### CONTENT: {get_response.content}")

post_response = requests.post("http://httpbin.org/post", "xabab")
print(f"### STATUS CODE: {post_response.status_code}")
print(f"### HEADERS: {post_response.headers}")
print(f"### CONTENT: {post_response.content}")

post_response_with_header = requests.post("http://httpbin.org/post", headers={"Accept": "application/json"})
print(f"### WITH HEADERS: {post_response_with_header.headers}")

get_json = requests.get("http://httpbin.org/get")
print(f"### GET JSON: {get_json.json()}")

get_404 = requests.get("http://httpbin.org/status/404")
get_404.raise_for_status()