from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
contact="Mom"
say="take medicine"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://web.whatsapp.com")
print("Scan QR code and hit Enter")
input()
print("Logged in")
time.sleep(5)
search=driver.find_element_by_xpath("/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")
search.send_keys(contact)
search.send_keys(Keys.ENTER)
time.sleep(5)
msg=driver.find_element_by_class_name("_2_1wd copyable-text selectable-text")
msg.send_keys(say)
msg.send_keys(Keys.ENTER)
time.sleep(10)
driver.quite()
