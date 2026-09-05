"""
QA Automation Suite - SauceDemo Web Application
Tool: Selenium WebDriver (Python) + PyTest
Target: https://www.saucedemo.com

Covers 15 critical automated scenarios across:
  - Authentication (TC-AUTO-01 to 05)
  - Product / Inventory (TC-AUTO-06 to 09)
  - Cart (TC-AUTO-10 to 12)
  - Checkout (TC-AUTO-13 to 15)

Run:
    pip install selenium pytest webdriver-manager
    pytest test_saucedemo.py -v --html=report.html --self-contained-html
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException

BASE_URL = "https://www.saucedemo.com"

VALID_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PROBLEM_USER = "problem_user"
PASSWORD = "secret_sauce"


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1366,768")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    drv = webdriver.Chrome(options=options)
    drv.implicitly_wait(5)
    yield drv
    drv.quit()


def login(driver, username=VALID_USER, password=PASSWORD):
    driver.get(BASE_URL)
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def wait_for(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))


# ---------------------------------------------------------------------------
# AUTHENTICATION (TC-AUTO-01 to 05)
# ---------------------------------------------------------------------------

def test_tc_auto_01_valid_login(driver):
    """Valid credentials should land the user on the inventory page."""
    login(driver)
    wait_for(driver, By.CLASS_NAME, "inventory_list")
    assert "/inventory.html" in driver.current_url


def test_tc_auto_02_invalid_password(driver):
    """Wrong password should show an error and block navigation."""
    login(driver, VALID_USER, "wrong_password")
    error = wait_for(driver, By.CSS_SELECTOR, "[data-test='error']")
    assert "do not match" in error.text.lower()
    assert "/inventory.html" not in driver.current_url


def test_tc_auto_03_locked_out_user(driver):
    """Locked out user must be blocked with the correct error message."""
    login(driver, LOCKED_USER, PASSWORD)
    error = wait_for(driver, By.CSS_SELECTOR, "[data-test='error']")
    assert "locked out" in error.text.lower()


def test_tc_auto_04_empty_credentials(driver):
    """Submitting the login form empty should require a username."""
    driver.get(BASE_URL)
    driver.find_element(By.ID, "login-button").click()
    error = wait_for(driver, By.CSS_SELECTOR, "[data-test='error']")
    assert "username is required" in error.text.lower()


def test_tc_auto_05_logout_flow(driver):
    """Logout via the burger menu should return the user to the login page."""
    login(driver)
    wait_for(driver, By.ID, "react-burger-menu-btn").click()
    wait_for(driver, By.ID, "logout_sidebar_link").click()
    wait_for(driver, By.ID, "login-button")
    assert driver.current_url.rstrip("/") == BASE_URL


# ---------------------------------------------------------------------------
# PRODUCT / INVENTORY (TC-AUTO-06 to 09)
# ---------------------------------------------------------------------------

def test_tc_auto_06_inventory_loads_six_items(driver):
    """Inventory page should list exactly 6 products for the standard user."""
    login(driver)
    items = wait_for(driver, By.CLASS_NAME, "inventory_list")
    products = items.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) == 6


def test_tc_auto_07_sort_price_low_to_high(driver):
    """Sorting by 'Price (low to high)' should render an ascending price list."""
    login(driver)
    wait_for(driver, By.CLASS_NAME, "product_sort_container")
    from selenium.webdriver.support.ui import Select
    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    values = [float(p.text.replace("$", "")) for p in prices]
    assert values == sorted(values)


def test_tc_auto_08_product_detail_navigation(driver):
    """Clicking a product name should open its detail page with matching title."""
    login(driver)
    name_el = wait_for(driver, By.CLASS_NAME, "inventory_item_name")
    product_name = name_el.text
    name_el.click()
    detail_name = wait_for(driver, By.CLASS_NAME, "inventory_details_name")
    assert detail_name.text == product_name


def test_tc_auto_09_add_to_cart_updates_badge(driver):
    """Adding a product should update the cart badge count to 1."""
    login(driver)
    wait_for(driver, By.CSS_SELECTOR, "button[data-test^='add-to-cart']").click()
    badge = wait_for(driver, By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"


# ---------------------------------------------------------------------------
# CART (TC-AUTO-10 to 12)
# ---------------------------------------------------------------------------

def test_tc_auto_10_remove_from_cart(driver):
    """Removing an item from the cart should clear the cart badge."""
    login(driver)
    add_btn = wait_for(driver, By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    add_btn.click()
    remove_btn = wait_for(driver, By.CSS_SELECTOR, "button[data-test^='remove']")
    remove_btn.click()
    with pytest.raises((NoSuchElementException, TimeoutException)):
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )


def test_tc_auto_11_cart_persists_item_details(driver):
    """Item added from inventory should appear with the same name in the cart page."""
    login(driver)
    name_el = wait_for(driver, By.CLASS_NAME, "inventory_item_name")
    product_name = name_el.text
    driver.find_element(By.CSS_SELECTOR, "button[data-test^='add-to-cart']").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_item_name = wait_for(driver, By.CLASS_NAME, "inventory_item_name")
    assert cart_item_name.text == product_name


def test_tc_auto_12_continue_shopping_returns_to_inventory(driver):
    """'Continue Shopping' from the cart should return to the inventory page."""
    login(driver)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait_for(driver, By.ID, "continue-shopping").click()
    wait_for(driver, By.CLASS_NAME, "inventory_list")
    assert "/inventory.html" in driver.current_url


# ---------------------------------------------------------------------------
# CHECKOUT (TC-AUTO-13 to 15)
# ---------------------------------------------------------------------------

def test_tc_auto_13_checkout_requires_fields(driver):
    """Submitting checkout info blank should raise a validation error."""
    login(driver)
    driver.find_element(By.CSS_SELECTOR, "button[data-test^='add-to-cart']").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait_for(driver, By.ID, "checkout").click()
    driver.find_element(By.ID, "continue").click()
    error = wait_for(driver, By.CSS_SELECTOR, "[data-test='error']")
    assert "first name is required" in error.text.lower()


def test_tc_auto_14_checkout_happy_path(driver):
    """A full happy-path checkout should reach the order confirmation screen."""
    login(driver)
    driver.find_element(By.CSS_SELECTOR, "button[data-test^='add-to-cart']").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait_for(driver, By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Soumya")
    driver.find_element(By.ID, "last-name").send_keys("Hazra")
    driver.find_element(By.ID, "postal-code").send_keys("711101")
    driver.find_element(By.ID, "continue").click()
    wait_for(driver, By.ID, "finish").click()
    complete_header = wait_for(driver, By.CLASS_NAME, "complete-header")
    assert "thank you" in complete_header.text.lower()


def test_tc_auto_15_order_total_matches_sum_plus_tax(driver):
    """Checkout overview total should equal subtotal + tax."""
    login(driver)
    driver.find_element(By.CSS_SELECTOR, "button[data-test^='add-to-cart']").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait_for(driver, By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Soumya")
    driver.find_element(By.ID, "last-name").send_keys("Hazra")
    driver.find_element(By.ID, "postal-code").send_keys("711101")
    driver.find_element(By.ID, "continue").click()

    subtotal = float(
        wait_for(driver, By.CLASS_NAME, "summary_subtotal_label").text.split("$")[1]
    )
    tax = float(driver.find_element(By.CLASS_NAME, "summary_tax_label").text.split("$")[1])
    total = float(driver.find_element(By.CLASS_NAME, "summary_total_label").text.split("$")[1])
    assert round(subtotal + tax, 2) == round(total, 2)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
