# -*- coding: utf-8 -*-
# @Author  : 柚一
# @File    : demo_1.py
import time

# 打开浏览器  selenium--驱动器--浏览器  浏览器自动化关闭 time.sleep(20)
# 访问网址
# 找到输入框输入内容
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
driver=webdriver.Chrome()
# 访问网址
driver.get("http://novel.hctestedu.com/")
# id name xpath css link text  parital_link_text tagname classname

# id
# 找到输入框  飘红色的下划线 报错  id是唯一
# 可不可以用id 找元素  取决于你的F12这行代码有没有id属性
# 属性=值  属性不可变  值是可变的
# el=driver.find_element(By.ID,'searchKey')

# name
# el2=driver.find_element(By.NAME,'searchKey')

# class  一般不太单独应用  不是唯一的  很少有唯一的  怎么确定是不是唯一的 键盘上输入F12 找元素
# el=driver.find_element(By.CLASS_NAME,'s_int')

# tag_name 标签定位  单独应用的少 更容易重复
# el=driver.find_element(By.TAG_NAME,'input')
# el=driver.find_elements(By.TAG_NAME,'input')#从0开始找元素
# el=el[0]

# link_text 通过a标签定位  只作用于a标签  <a></a>
# el=driver.find_element(By.LINK_TEXT,'首')
# partial_link_text  只作用于a标签  <a></a>
# el=driver.find_element(By.PARTIAL_LINK_TEXT,'首')

# 区别：link_text要写完整的定位内容
# partial_link_text 不需要写完整的定位内容

# id name class 属性定位  这行代码必须要有这里面的属性
# tag_name 标签 <div> <span>
# link_text/partial_link_text  <a>

# css 和xpath 更加灵活
# css
# .代表是class  #代表id  >子元素（儿子）   空格 (后代元素 儿子 孙子)  +兄弟关系
# el=driver.find_element(By.CSS_SELECTOR,'#searchKey')
# el=driver.find_element(By.CSS_SELECTOR,'.s_int')
# 怎么确认表达式有没有问题  键盘上输入F12 找元素
# 找input标签，class为s_int的元素
# el=driver.find_element(By.CSS_SELECTOR,'input.s_int') 外面用单引号 里面用双引号  外面用双引号 里面用单引号
# el=driver.find_element(By.CSS_SELECTOR,'input[class="s_int"]')
# el=driver.find_element(By.CSS_SELECTOR,'div.search>input')
# el=driver.find_element(By.CSS_SELECTOR,'div.search input')
# el=driver.find_element(By.CSS_SELECTOR,'div.search input+label')

# xpath


# # id name xpath css link text  parital_link_text tagname classname
# 有id用id  没有id用name  没有id没有name采用xpath或者css的写法

# 效果 js代码  arguments[0]  el arguments[1] 'border:1px solid green;
# driver.execute_script(
#     "arguments[0].setAttribute('style',arguments[1]);",
#     el,
#     'border:1px solid red;'
# )
# 等待
time.sleep(3)
# 关闭浏览器
driver.quit()


# 打开浏览器 访问网址 进行输入内容 点击进行搜索操作
# 有问题1  没有问题2