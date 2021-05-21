from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import  expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
botDriver=webdriver.Chrome(executable_path="C:\\Firefox\\chromedriver")
botDriver.get("https://web.whatsapp.com/")
chatname=input("Enter friend  name")
chatmsg=input("Enter msg  ")
noc=int(input("Enter count"))
input("enter anything/or press  any  key to continue")
user=botDriver.find_element_by_xpath('//span[@title="{}"]'.format(chatname))
user.click()
msg_box=botDriver.find_element_by_class_name('_3uMse')
for i in range(noc):
    button=botDriver.find_element_by_class_name("weEq5")
    button.click()