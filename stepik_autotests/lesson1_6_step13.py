#!/usr/bin/python3

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    text = browser.find_element_by_css_selector('[class="form-control first"]')
    text.send_keys('Yes')
    text = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    text.send_keys('Yes')
    text = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
    text.send_keys('Yes')
    time.sleep(3)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

finally:
    time.sleep(10)
    browser.quit()


