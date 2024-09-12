from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")  # Applicable for older versions of Chrome
chrome_options.add_argument("--window-size=1920,1080")

# Initialize the WebDriver (using Chrome in this example)
driver = webdriver.Chrome(options=chrome_options)#executable_path='/home/abhishek/Downloads/chromedriver-linux64/chromedriver')

# Open the website
apiUrl = "https://www.myvue.com/api/microservice/showings/cinemas/10004" + "/films?filmId=" + "HO00019557" + "&minEmbargoLevel=1&includesSession=true&includeSessionAttributes=true"
url = "https://www.myvue.com"
driver.get(url)

# Optionally, wait for the page to load completely or perform actions like login
time.sleep(5)  # Adjust this based on loading time or add WebDriverWait for specific elements
print(driver.page_source)

# Retrieve all cookies from the browser
cookies = driver.get_cookies()
cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}
print(cookies_dict)

driver.get("https://www.example.com")
print("example.com", driver.page_source)

resp = requests.get(apiUrl, cookies=cookies_dict)
if resp.status_code != 200:
    print(resp)
print(resp.json())

# Close the browser
driver.quit()
