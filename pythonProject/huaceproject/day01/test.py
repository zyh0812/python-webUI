
from selenium import webdriver
from selenium.webdriver.common.by import By

#打开浏览器
driver = webdriver.Chrome()
driver.get("http://novel.hctestedu.com/user/login.html/")

# el = driver.find_element(By.ID,"searchKey")
# el = driver.find_element(By.NAME,"searchKey")
# el = driver.find_element(By.CLASS_NAME, "s_int")
# el = driver.find_element(By.TAG_NAME,"input")
# el = driver.find_elements(By.TAG_NAME,"input")
# el = el[0]

# el = driver.find_element(By.LINK_TEXT,"首页")
# el = driver.find_element(By.PARTIAL_LINK_TEXT,"首")

# el = driver.find_element(By.CSS_SELECTOR,"#searchKey")
# el = driver.find_element(By.CSS_SELECTOR,".s_int")
# el = driver.find_element(By.CSS_SELECTOR,"input.s_int")
# el = driver.find_element(By.CSS_SELECTOR,"input[class = 's_int']")
# el = driver.find_element(By.CSS_SELECTOR,"div.search input")

el = driver.find_element(By.XPATH,'//*[@name = "searchKey" and @class = "s_int"]')

driver.execute_script(
    "arguments[0].setAttribute('style',arguments[1]);",
    el,
    "border:1px solid red;"
)