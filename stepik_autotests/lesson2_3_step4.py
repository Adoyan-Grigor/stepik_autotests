#!/usr/bin/python3
from selenium import webdriver
browser = webdriver.Chrome()
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser.get('http://suninjuly.github.io/alert_accept.html')
try:
    el = browser.find_element_by_css_selector('[type="submit"]')
    el.click()
    alert = browser.switch_to.alert
    alert.accept()
    el = browser.find_element_by_id('input_value').text
    x = calc(el)
    el = browser.find_element_by_id('answer')
    el.send_keys(x)
    el = browser.find_element_by_css_selector('[type="submit"]')
    el.click()
finally:
    time.sleep(15)
    browser.quit()


