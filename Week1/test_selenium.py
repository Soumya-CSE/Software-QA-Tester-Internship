from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open Flipkart
driver.get("https://www.flipkart.com")

time.sleep(2)  # let page load

# Close login popup if it appears
try:
    close_btn = driver.find_element(By.XPATH, "//button[contains(text(),'✕')]")
    close_btn.click()
except:
    pass

# Search for a product
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("laptop")
search_box.submit()

time.sleep(2)

# Inspect page title
print("Page title:", driver.title)

# Inspect first few product names
products = driver.find_elements(By.CSS_SELECTOR, "div._4rR01T")  # class may change over time
for p in products[:5]:
    print(p.text)

driver.quit()
