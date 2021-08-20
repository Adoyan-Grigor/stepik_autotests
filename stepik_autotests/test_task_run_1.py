#!/usr/bin/python3
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage(object):
    # номер 1
    @pytest.mark.xfail
    @pytest.mark.smoke
    def test_1(self, browser):
        print(1)
        assert True

    # номер 2
    @pytest.mark.regression
    def test_2(self, browser):
        print(2)
        assert True


class TestBasket(object):
    # номер 3
    @pytest.mark.skip(reason="not implemented yet")
    @pytest.mark.smoke
    def test_3(self, browser):
        print(3)
        assert True

    # номер 4
    @pytest.mark.smoke
    def test_4(self, browser):
        print(4)
        assert True


@pytest.mark.skip
class TestBookPage():
    # номер 5
    @pytest.mark.smoke
    def test_5(self, browser):
        print(5)
        assert True

    # номер 6
    @pytest.mark.regression
    def test_6(self, browser):
        print(6)
        assert True


# номер 7
@pytest.mark.beta_users
@pytest.mark.smoke
def test_7(browser):
    print(7)
    assert True
