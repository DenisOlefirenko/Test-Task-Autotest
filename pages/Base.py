import logging
import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys


class web_browser:
    def __init__(self, url, driver):
        log_dir = r'./log_dir'
        print('logs are located in "log_dir"')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        log_filename = datetime.now().strftime('./log_dir/testTask_%H_%M_%S_%d_%m_%Y.txt')
        logging.basicConfig(handlers=[logging.FileHandler(log_filename, 'w', 'utf-8')], level=logging.INFO)

        log_time = (time.ctime())
        logging.info('\n _______________________________________________________\n')
        logging.info('Start Test {}'.format(log_time))

        self.driver = driver
        logging.info('Browser' + self.driver.name)
        self.driver.get(url)

    def search_by_id(self, element):
        try:
            self.search_form = self.driver.find_element("id", element)
            logging.info('Element ' + element + ' found')
            logging.info('Element displayed: {}'.format(self.search_form.is_displayed()))
            return self.search_form
        except NoSuchElementException:
            logging.exception('Element' + element + 'not found')

    def search_by_class(self, element):
        try:
            self.search_form = self.driver.find_element("class name", element)
            logging.info('Element ' + element + ' found')
            logging.info('Element displayed: {}'.format(self.search_form.is_displayed()))
            return self.search_form
        except NoSuchElementException:
            logging.exception('Element ' + element + ' not found')

    def search_by_xpath(self, element):
        try:
            self.search_form = self.driver.find_element("xpath", element)
            logging.info('Element ' + element + ' found')
            logging.info('Element displayed: {}'.format(self.search_form.is_displayed()))
            return self.search_form
        except NoSuchElementException:
            logging.exception('Element ' + element + ' not found')

    def enter_text(self, element, text, suggest):
        try:
            self.search_by_xpath(element).send_keys(text)
        except NoSuchElementException:
            logging.exception('Search bar ' + element + ' not found')

        try:
            suggest_app = self.driver.find_element("class name", suggest)
            logging.info('Element ' + suggest + ' found')
            logging.info('Suggestions displayed: {}'.format(suggest_app.is_displayed()))
        except NoSuchElementException:
            logging.exception('Element ' + suggest + ' not found')

        self.search_form.send_keys(Keys.RETURN)

    def link_check(self, url, try_elements, amount):

        links = self.driver.find_elements("class name", try_elements)
        result = []

        for link in links[:amount]:
            href = link.get_attribute("href")
            result.append(href)

        match = [i for i in result if url in i]

        if len(match) > 0:
            logging.info('URL ' + url + ' was found')
        else:
            logging.info('Current URL not found')

    def click_object(self, search_type, name):
        if search_type == 0:
            self.search_by_class(name).click()
        elif search_type == 1:
            self.search_by_xpath(name).click()
        time.sleep(2)

    def link_test(self, link):
        if len(self.driver.window_handles) == 1:
            if self.driver.current_url == link:
                logging.info('URL equals to {}'.format(link))
            else:
                logging.info('URL not equals to {}'.format(link))
        else:
            links = []
            for handle in self.driver.window_handles:
                self.driver.switch_to.window(handle)
                links.append(self.driver.current_url)
            if link in links:
                logging.info('URL equals to {}'.format(link))
            else:
                logging.info('URL not equals to {}'.format(link))

    def get_image(self, tag):
        try:
            link = self.driver.find_element("xpath", tag)
            src = link.get_attribute("src")
            logging.info('Image ' + tag + ' found')
            logging.info('Image displayed: {}'.format(self.search_form.is_displayed()))
        except NoSuchElementException:
            logging.exception('Image ' + tag + ' not found')

    def check_image(self, flag, tag):
        try:
            link = self.driver.find_element("xpath", tag)
            src = link.get_attribute("src")
            data = src
            if flag:
                link = self.driver.find_element("xpath", tag)
                src = link.get_attribute("src")
                data_check = src
                logging.info('{} \n {} \n'.format(data, data_check))
                if data == data_check:
                    logging.info('Correct first image chosen')
                else:
                    logging.info('Not a first image chosen')
        except NoSuchElementException:
            logging.exception('Image ' + tag + ' not found')

    def quit(self):
        self.driver.quit()
