#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as E
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')
browser.implicitly_wait(10)
try:
    el = 100
    while el != '$100':
        time.sleep(1)
        el = browser.find_element_by_id('price').text
    el = browser.find_element_by_id('book')
    el.click()
    x_el = browser.find_element_by_id('input_value').text
    x = calc(x_el)
    el = browser.find_element_by_id('answer')
    el.send_keys(x)
    el = browser.find_element_by_id('solve')
    el.click()
finally:
    time.sleep(10)
    browser.quit()

