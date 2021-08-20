#!/usr/bin/python3
from selenium import webdriver
browser = webdriver.Chrome()
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = 'http://suninjuly.github.io/math.html'
browser.get(link)
try:
    x_element = browser.find_element_by_id('input_value')
    y = calc(x_element.text)
    element = browser.find_element_by_id('answer')
    element.send_keys(y)
    element = browser.find_element_by_id('robotCheckbox')
    element.click()
    element = browser.find_element_by_id('robotsRule')
    element.click()
    element = browser.find_element_by_css_selector('[type="submit"]')
    element.click()
finally:
    time.sleep(10)
    browser.quit()

