#!/usr/bin/python3
from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')
try:
    el = browser.find_element_by_css_selector('[type="submit"]')
    el.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    el = browser.find_element_by_id('answer')
    el.send_keys(y)
    el = browser.find_element_by_css_selector('[type="submit"]')
    el.click()
finally:
    time.sleep(15)
    browser.quit()

