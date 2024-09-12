import requests

# Open the website to get cookies
url = "https://www.myvue.com"
resp = requests.get(url)
print("web response", resp.reason)
print(resp.cookies)

apiUrl = "https://www.myvue.com/api/microservice/showings/cinemas/10004" + "/films?filmId=" + "HO00019557" + "&minEmbargoLevel=1&includesSession=true&includeSessionAttributes=true"
resp = requests.get(apiUrl, cookies=resp.cookies)

if resp.status_code != 200:
    print(resp)

print(resp.json())

