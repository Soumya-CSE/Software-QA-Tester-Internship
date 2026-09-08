from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open Amazon
driver.get("https://www.amazon.in")

time.sleep(2)  # let page load

# Search for a product
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.submit()

time.sleep(2)

# Inspect page title
print("Page title:", driver.title)

# Inspect first few product names
products = driver.find_elements(By.CSS_SELECTOR, "h2 span")

for p in products[:5]:
    print(p.text)

driver.quit()
