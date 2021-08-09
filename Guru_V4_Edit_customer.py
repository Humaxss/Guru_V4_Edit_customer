from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import pandas as pd
import lxml

driver=webdriver.Chrome('C:\Python\chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.guru99.com/V4/")
driver.implicitly_wait(10)

#User_id
User_id = driver.find_element_by_name("uid")
User_id.click()
User_id.send_keys("mngr346602")
time.sleep(1)

#password
password = driver.find_element_by_name("password")
password.click()
password.send_keys("YgupEze")
time.sleep(1)

#login
login = driver.find_element_by_name("btnLogin")
login.click()
time.sleep(1)


#Edit_Customer

Edit_Customer = driver.find_element_by_partial_link_text("Edit Customer")
Edit_Customer.click()

#customer_id
customer_id = driver.find_element_by_xpath("//input[@name='cusid']")
customer_id.send_keys("7")

#Submit
Submit = driver.find_element_by_xpath("//input[@value='Submit']")
Submit.click()

#Adress
Adress = driver.find_element_by_xpath("//textarea[@name='addr']")
Adress.clear()
time.sleep(1)
Adress.send_keys("Mala Calomija, calomija")

#City
City = driver.find_element_by_xpath("//input[@name='city']")
City.clear()
time.sleep(1)
City.send_keys("Mala Calomija calomija")

#Reset
Reset = driver.find_element_by_xpath("//input[@name='res']")
Reset.click()

#Mobil_number
Mobil_number = driver.find_element_by_xpath("//input[@name='telephoneno']")
Mobil_number.clear()
time.sleep(1)
Mobil_number.send_keys("09035486547")

#Submit
Submit = driver.find_element_by_xpath("//input[@name='sub']")
Submit.click()
time.sleep(4)