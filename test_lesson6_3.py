from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout(driver):
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    sleep(5)
   
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    sleep(5)
    
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a").click()
    
    driver.find_element(By.ID, "checkout").click()
    
    driver.find_element(By.ID, "first-name").send_keys("Андрей")
    driver.find_element(By.ID, "last-name").send_keys("Брюханов")
    driver.find_element(By.ID, "postal-code").send_keys("660113")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()
    
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_info > .summary_total_label"))
    )
    total_text = driver.find_element(By.CSS_SELECTOR, ".summary_info > .summary_total_label").text
    assert "Total: $58.29" in total_text, f"Expected 'Total: $58.29', but got '{total_text}'"
   
    driver.quit()
