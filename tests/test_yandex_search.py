from pages.Base import *
import pytest


def test_check_search():
    browser = web_browser('http://yandex.ru', webdriver.Chrome())
    browser.enter_text('//input[@name="text"]', 'Тензор', 'mini-suggest__overlay_visible')
    browser.link_check('https://tensor.ru', 'Link_theme_outer', 2)
    browser.quit()

