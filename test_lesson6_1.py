from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "", 
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in form_data.items():
        driver.find_element(By.NAME, field_name).send_keys(value)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    submit_button.click()

    time.sleep(2)

    for field_name in form_data.keys():
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, field_name))
        )
        background_color = element.value_of_css_property("background-color")
        print(f"Элемент {field_name} имеет цвет: {background_color}")

        if background_color == "rgba(209, 231, 221, 1)":
            print(f"Элемент {field_name} имеет цвет: зеленый")
        elif background_color == "rgba(248, 215, 218, 1)":
            print(f"Элемент {field_name} имеет цвет: красный")
        else:
            print(f"Элемент {field_name} имеет неизвестный цвет")

finally:
    driver.quit()
