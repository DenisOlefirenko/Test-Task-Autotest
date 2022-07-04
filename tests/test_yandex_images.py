from pages.Base import *
import pytest


def test_check_images():
    browser = web_browser('http://yandex.ru', webdriver.Chrome())
    browser.click_object(1, '//a[@data-id="images"]')
    browser.link_test('https://yandex.ru/images/?utm_source=main_stripe_big')
    browser.click_object(0, 'PopularRequestList-Shadow')
    browser.click_object(0, 'serp-item_pos_0')
    browser.get_image('//img[@class="MMImage-Origin"]')
    browser.check_image(False, '//img[@class="MMImage-Origin"]')
    browser.click_object(0, 'CircleButton_type_next')
    browser.get_image('//img[@class="MMImage-Origin"]')
    browser.click_object(0, 'CircleButton_type_prev')
    browser.get_image('//img[@class="MMImage-Origin"]')
    browser.check_image(True, '//img[@class="MMImage-Origin"]')
    browser.quit()
