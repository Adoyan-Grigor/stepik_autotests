#!/usr/bin/python3
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')
try:
    el = browser.find_element_by_name('firstname')
    el.send_keys('name')
    el = browser.find_element_by_name('lastname')
    el.send_keys('lastname')
    el = browser.find_element_by_name('email')
    el.send_keys('email')
    el = browser.find_element_by_id('file')
    import os
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'hellp.txt')
    el.send_keys(file_path)
    el = browser.find_element_by_css_selector('[type="submit"]')
    el.click()
finally:
    time.sleep(15)
    browser.quit()

