import unittest
from selenium import webdriver

class EnvironmentSetup(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='C:/geckodriver-v0.21.0-win64/geckodriver.exe')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.delete_all_cookies()