from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://pantip.com/forum/siliconvalley'

path = r'C:\Users\bakpu\Desktop\Auto-Web\chromedriver_win32\chromedriver.exe'
driver  = webdriver.Chrome(path)
driver.get(url)

driver.maximize_window()

#forword
for i in range(6):
    driver.execute_script('window.scrollTo(0, {})'.format(10000*i))
    time.sleep(2)

#backword    
for i in reversed(range(6)):
    driver.execute_script('window.scrollTo(0, {})'.format(10000*i))
    time.sleep(2)

#capture
for i in range(6):
    driver.execute_script('window.scrollTo(0, {})'.format(526*i))
    driver.save_screenshot('test-{}.png'.format(i))
    time.sleep(1)