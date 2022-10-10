from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.google.com/'
url2 = 'https://www.jib.co.th'

path = r'C:\Users\bakpu\Desktop\Auto-Web\chromedriver_win32\chromedriver.exe'
driver  = webdriver.Chrome(path)
driver.get(url)

search = driver.find_element("name","q")
# search = driver.find_element("name","productTitle") # ของ url2
search.send_keys('ลำโพง')
search.send_keys(Keys.RETURN) # การกดปุ่ม enter

driver.maximize_window()
# driver.save_screenshot(r'test.png')
# driver.close()

for i in range(6):
    driver.execute_script('window.scrollTo(0, {})'.format(500*i))
    driver.save_screenshot('test-{}.png'.format(i))
    time.sleep(1)