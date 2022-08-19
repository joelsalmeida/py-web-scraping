import requests
import time

for _ in range(11):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(f"### RESPONSE: {response.status_code}")


for _ in range(11):
    response = requests.get("https://www.cloudflare.com/rate-limit-test/")
    print(f"### RESPONSE: {response.status_code}")
    time.sleep(15)