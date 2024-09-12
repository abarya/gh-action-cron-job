import requests

# Open the website to get cookies
url = "https://www.myvue.com"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
resp = requests.get(url, headers=headers)
print("web response", resp.reason)
print(resp.cookies)

apiUrl = "https://www.myvue.com/api/microservice/showings/cinemas/10004" + "/films?filmId=" + "HO00019557" + "&minEmbargoLevel=1&includesSession=true&includeSessionAttributes=true"
resp = requests.get(apiUrl, cookies=resp.cookies)

if resp.status_code != 200:
    print(resp)

print(resp.json())

