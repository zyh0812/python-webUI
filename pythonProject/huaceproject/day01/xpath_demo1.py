from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://novel.hctestedu.com/user/login.html")

# el = driver.find_element(By.XPATH,'//*[@id="searchKey"]')

# el = driver.find_element(By.XPATH,"//input[@class = 's_int']")

el = driver.find_element(By.XPATH,"")


driver.execute_script(
    "arguments[0].setAttribute('style',arguments[1]);",
    el,
    "border:1px solid red;"
)
