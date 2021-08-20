#!/usr/bin/python3

from selenium import webdriver
import time
import unittest
browser = webdriver.Chrome()
browser.implicitly_wait(5)
class test_class_name(unittest.TestCase):
    def test_1(self):
        browser.get('http://suninjuly.github.io/registration1.html')
        el = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        el.send_keys('First name')
        el = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        el.send_keys('Last name')
        el = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        el.send_keys('Email')
        el = browser.find_element_by_css_selector('[type="submit"]')
        el.click()
        tx = browser.find_element_by_css_selector('h1').text
        self.assertEqual('Congratulations! You have successfully registered!', tx, tx)
        time.sleep(1)
        browser.quit()
    def test_2(self):
        browser.get('http://suninjuly.github.io/registration2.html')
        el = browser.find_element_by_css_selector('[placeholder="Input your name"]')
        el.send_keys('First name')
        el = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        el.send_keys('Last name')
        el = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        el.send_keys('Email')
        el = browser.find_element_by_css_selector('[type="submit"]')
        el.click()
        h1 = browser.find_element_by_css_selector('h1').text
        self.assertEqual('Congratulations! You have successfully registered!', h1)
        time.sleep(1)
        browser.quit()

