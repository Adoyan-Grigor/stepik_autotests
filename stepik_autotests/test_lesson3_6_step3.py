#!/usr/bin/python3
from selenium import webdriver
browser = webdriver.Chrome()
import pytest
import time
import math

@pytest.mark.parametrize('number', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_stepik1(browser, number):
    browser.implicitly_wait(20)
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    el = browser.find_element_by_css_selector('[autocapitalize="none"]')
    x = math.log(int(time.time()))
    el.send_keys(str(x))
    button = browser.find_element_by_css_selector('[class="submit-submission"]')
    button.click()
    el = browser.find_element_by_css_selector('[class="smart-hints__hint"]').text
    assert el == 'Correct!'

