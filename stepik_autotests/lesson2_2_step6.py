#!/usr/bin/python3
from selenium import webdriver 
import math
import time
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    x_element = browser.find_element_by_id('input_value').text
    y = calc(x_element)
    el = browser.find_element_by_id('answer')
    el.send_keys(y)
    el = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", el)
    el.click()
    el = browser.find_element_by_id('robotsRule')
    el.click()
    el = browser.find_element_by_css_selector('[type="submit"]')
    el.click()
finally:
    time.sleep(15)
    browser.quit()

