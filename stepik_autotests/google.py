#!/usr/bin/python3
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.google.com/search?q=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+%D1%81+%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE+%D0%BD%D0%B0+%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9&oq=%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D1%87%D0%B8%D0%BA+&aqs=chrome.1.69i59l2j0i512l8.2159j0j9&sourceid=chrome&ie=UTF-8')
try:
    el = browser.find_element_by_css_selector('[id="tw-source-text-ta"]')
    el.send_keys('hello')
finally:
    time.sleep(3)
    browser.quit()
