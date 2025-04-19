import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import HtmlTestRunner  

class TestRegistro(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        service = Service(ChromeDriverManager().install())  # ✅ solución aquí
        cls.driver = webdriver.Chrome(service=service)

        # Crear carpeta para capturas
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def take_screenshot(self, name):
        """Toma capturas de pantalla con un nombre dado"""
        self.driver.save_screenshot(f"screenshots/{name}.png")

    def test_registro_login_tarea(self):
        driver = self.driver
        try:
            # Paso 1: Abrir la página de registro
            driver.get("file:///C:/Users/Joharlyn/OneDrive/Documentos/ITLA/Sexto%20cuatrimestre/Programación%20III/Proyecto%20final/TaskFlow%20Pro/register.html")
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "registerUsername")))

            self.take_screenshot("registro_pagina")

            # Rellenar formulario de registro
            driver.find_element(By.ID, "registerUsername").send_keys("usuario_de_prueba")
            driver.find_element(By.ID, "registerPassword").send_keys("contraseña123")
            driver.find_element(By.ID, "confirmPassword").send_keys("contraseña123")
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            self.take_screenshot("registro_completado")

            # Paso 2: Iniciar sesión
            driver.get("file:///C:/Users/Joharlyn/OneDrive/Documentos/ITLA/Sexto%20cuatrimestre/Programación%20III/Proyecto%20final/TaskFlow%20Pro/login.html")
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginUsername")))

            driver.find_element(By.ID, "loginUsername").send_keys("usuario_de_prueba")
            driver.find_element(By.ID, "loginPassword").send_keys("contraseña123")
            driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
            self.take_screenshot("login_exitoso")

            # Paso 3: Crear una nueva tarea
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "showFormButton"))).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "taskModal")))

            driver.find_element(By.ID, "taskTitle").send_keys("Tarea Selenium")
            driver.find_element(By.ID, "taskDate").send_keys("2024-12-15")
            driver.find_element(By.ID, "taskDescription").send_keys("Descripción de tarea Selenium")
            driver.find_element(By.ID, "taskPriority").send_keys("3")
            driver.find_element(By.CSS_SELECTOR, "#taskForm button[type='submit']").click()
            self.take_screenshot("tarea_creada")

        finally:
            self.take_screenshot("final")
            print("Prueba finalizada.")
            time.sleep(5)
            driver.quit()
        
if __name__ == "__main__":
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestRegistro)
    with open("reports/test_report.html", "w") as report_file:
        runner = HtmlTestRunner.HTMLTestRunner(stream=report_file)
        runner.run(test_suite)
