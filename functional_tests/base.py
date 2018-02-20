<<<<<<< HEAD
#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip

class FunctionalTest(StaticLiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        pass

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')

        rows = table.find_elements_by_tag_name('tr')
=======
#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from unittest import skip

class FunctionalTest(StaticLiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        pass

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')


    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')

        rows = table.find_elements_by_tag_name('tr')
>>>>>>> 8e1ed09cc2ce56ec4163fa9a79f9dcf0c912d4d7
        self.assertIn(row_text, [row.text for row in rows])