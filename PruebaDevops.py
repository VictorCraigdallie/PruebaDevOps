
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\Victor\\Desktop\\DevOps\\chromedriver.exe')
driver.get("http://192.168.37.129:8011")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.NAME, "pass")
elemento2.clear()
elemento2.send_keys("Password")

driver.find_element(By.ID, "login").click()

time.sleep(20)

driver.close()
