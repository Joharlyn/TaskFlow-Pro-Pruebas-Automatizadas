from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("file:///C:/Users/Joharlyn/OneDrive/Documentos/ITLA/Sexto%20cuatrimestre/Programación%20III/Proyecto%20final/TaskFlow%20Pro/register.html")

    username = driver.find_element(By.ID, "registerUsername")
    password = driver.find_element(By.ID, "registerPassword")
    confirm_password = driver.find_element(By.ID, "confirmPassword")
    register_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    username.send_keys("testuser")
    password.send_keys("password123")
    confirm_password.send_keys("password123")
    register_button.click()

    time.sleep(3)
    modal_message = driver.find_element(By.ID, "modalMessage").text
    print(f"Mensaje recibido: {modal_message}")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    time.sleep(3)
    driver.quit()
