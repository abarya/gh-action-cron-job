import undetected_chromedriver as uc
import time

driver = uc.Chrome(headless=True,use_subprocess=False)
driver.get('https://nowsecure.nl')
time.sleep(10)
print(driver.page_source)
