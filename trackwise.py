from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get('https://trackwise.url') 

username = browser.find_element_by_name("username") 
password = browser.find_element_by_name("password")
submit   = browser.find_element_by_class_name("btn-success")

username.send_keys("Blah")
password.send_keys("BlahBlah")
submit.click()

browser.quit()
    

