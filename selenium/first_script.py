from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Firefox()

driver.get('file:///D:/Users/re90603z/Documents/Testes/Web/class2/index.html')

pass_input = driver.find_element_by_id('passwd-id')
pass_input.clear()
pass_input.send_keys('deu?')
driver.close()
