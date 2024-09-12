from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome()#executable_path='/home/abhishek/Downloads/chromedriver-linux64/chromedriver')

# Open the website
apiUrl = "https://www.myvue.com/api/microservice/showings/cinemas/10004" + "/films?filmId=" + "HO00019557" + "&minEmbargoLevel=1&includesSession=true&includeSessionAttributes=true"
url = "https://www.myvue.com"
driver.get(url)

# Optionally, wait for the page to load completely or perform actions like login
time.sleep(5)  # Adjust this based on loading time or add WebDriverWait for specific elements

# Retrieve all cookies from the browser
cookies = driver.get_cookies()
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

resp = requests.get(apiUrl, cookies=cookies_dict)
if resp.status_code != 200:
    print(resp)
print(resp.json())

# Close the browser
driver.quit()
