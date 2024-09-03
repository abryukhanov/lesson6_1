from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").send_keys("")  # Пустое значение для zip-code
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()

    time.sleep(2)

    elements_to_check = ["first-name", "last-name", "address", "zip-code", "city", "country", "e-mail", "phone", "job-position", "company"]
    
    for element_id in elements_to_check:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, element_id))
        )
        background_color = element.value_of_css_property("background-color")
        print(f"Элемент {element_id} имеет цвет: {background_color}")

        if background_color == "rgba(209, 231, 221, 1)":
            print(f"Элемент {element_id} имеет цвет: зеленый")
        elif background_color == "rgba(248, 215, 218, 1)":
            print(f"Элемент {element_id} имеет цвет: красный")
        else:
            print(f"Элемент {element_id} имеет неизвестный цвет")
finally:

    driver.quit()
