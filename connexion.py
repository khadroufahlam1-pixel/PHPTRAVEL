# connexion_phptravels.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://phptravels.net")

time.sleep(2)
driver.find_element(By.XPATH, "//a[contains(., 'Agent')]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(., 'Login')]").click()

time.sleep(2)
driver.find_element(By.NAME, "email").send_keys("agent@phptravels.com")
driver.find_element(By.NAME, "password").send_keys("demoagent")
driver.find_element(By.XPATH, "//button[text()='Login']").click()
    


time.sleep(3)


wait = WebDriverWait(driver, 10)

titre = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(), 'Your Trip Starts Here!')]")))


driver.save_screenshot("resultat.png")
time.sleep(2)
driver.quit()