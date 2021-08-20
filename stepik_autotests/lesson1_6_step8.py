#!/usr/bin/python3

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/find_xpath_form')
    input1 = browser.find_element_by_name('first_name')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('firstname')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    submit = browser.find_element_by_xpath('//button[@type="submit"]')
    submit.click()

finally:
    time.sleep(30)
    browser.quit()

