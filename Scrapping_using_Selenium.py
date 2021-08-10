from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://findslot.in")
search = driver.find_element_by_id("pincode")
search.send_keys("400097")
sec = driver.find_element_by_id("filter-by-pincode")
sec.click()
try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"vaccine_details"))
        )
    driver.implicitly_wait(20)
    trs = table.find_elements_by_class_name("sorting_1")
    
        
    odds = table.find_elements_by_class_name("odd")
    for odd in odds:
        print odd.text
    
    evens = table.find_elements_by_class_name("even")
    for even in evens:
        print even.text
    
        
except:
    driver.close()


