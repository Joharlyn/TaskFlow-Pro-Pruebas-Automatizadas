from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    print("Cargando la página...")
    driver.get("file:///C:/Users/Joharlyn/OneDrive/Documentos/ITLA/Sexto%20cuatrimestre/Programación%20III/Proyecto%20final/TaskFlow%20Pro/login.html")

    print("Buscando elementos del formulario...")
    username = driver.find_element(By.ID, "loginUsername")
    password = driver.find_element(By.ID, "loginPassword")
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    print("Elementos encontrados, interactuando...") 
    username.send_keys("testuser")
    password.send_keys("password123")
    login_button.click()

    print("Esperando que aparezca el modal...")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "modalMessage"))
    )

    modal_message = driver.find_element(By.ID, "modalMessage").text
    print(f"Mensaje recibido: {modal_message}")

except Exception as e:
    print(f"Ocurrió un error: {e}")

finally:
    time.sleep(5)
    driver.quit()
