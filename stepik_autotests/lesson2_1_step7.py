#!/usr/bin/python3
from selenium import webdriver
browser = webdriver.Chrome()
import math
import time
link = 'http://suninjuly.github.io/get_attribute.html'
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser.get(link)
    x_element = browser.find_element_by_id('treasure')
    x_element_check = x_element.get_attribute('valuex')
    y = calc(x_element_check)
    element = browser.find_element_by_id('answer')
    element.send_keys(y)
    element = browser.find_element_by_id('robotCheckbox')
    element.click()
    element = browser.find_element_by_id('robotsRule')
    element.click()
    element = browser.find_element_by_css_selector('[type="submit"]')
    element.click()
finally:
    time.sleep(15)
    browser.quit()

