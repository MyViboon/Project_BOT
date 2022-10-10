from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

######### รัน แบบเบื้องหลัง ไม่เปิดเว็ป ######################
op = webdriver.ChromeOptions()
op.add_argument('headless') #ไม่เปิดหน้าเว็ป

path = Service(r'C:\Users\bakpu\Desktop\Auto-Web\chromedriver_win32\chromedriver.exe')
driver  = webdriver.Chrome(service=path, options=op)

#------------------------------------------------------

url = 'http://www.uncle-machine.com/login/'
driver.get(url)

driver.maximize_window()

########### LOGIN ##################
username = driver.find_element(By.ID, "username")
username.send_keys('loong7777@gmail.com')

password = driver.find_element(By.ID, "password")
password.send_keys('12345')

buttom = driver.find_element(By.XPATH,'/html/body/div[2]/form/button')
buttom.click()

time.sleep(2)

url2 = 'http://www.uncle-machine.com/sensor'
driver.get(url2)

sensor_id = driver.find_element(By.ID, "sid")
sensor_id.send_keys('ID 1001')
sensor_id.send_keys(Keys.RETURN)

time.sleep(1)

# temp = driver.find_element("class name", "temp")
temp = driver.find_element(By.CLASS_NAME, "temp" )
humid = driver.find_element(By.CLASS_NAME, "humid")

print(temp.text, humid.text)

driver.close()