#!/usr/bin/python3
from selenium import webdriver
import time
import math
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
try:
    a = browser.find_element_by_id('num1').text
    b = browser.find_element_by_id('num2').text
    c = browser.find_element_by_css_selector('span:nth-child(3)').text
    if c == '+':
        x = int(a) + int(b)
    elif c == '-':
        x = int(a) - int(b)
    elif c == '*':
        x = int(a) * int(b)
    elif c == '/':
        x = int(a) / int(b)
    elif c == '**':
        x = int(a) ** int(b)
    elif c == '%':
        x = int(a) % int(b)
    el = browser.find_element_by_id('dropdown')
    el.click
    el = browser.find_element_by_css_selector('[value="' + str(x) + '"]')
    el.click()
    el = browser.find_element_by_css_selector('[type="submit"]')
    el.click()
finally:
    time.sleep(10)
    browser.quit()


