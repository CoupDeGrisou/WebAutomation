from selenium.webdriver.common.by import By
from EzContacts.Src.PageObject.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import random


class Vendors(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.vendorsLink = driver.find_element(By.XPATH, Locator.vendors_link)

        
    def setVendorLink(self):
        self.vendorsLink.click()
        
    def setAddNewVendor(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.add_vendor))).click()
    
    def setVendorName(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, Locator.vendor_name))).send_keys("Autotest_Vendor_"+str(random()))
    
    def setSaveNewVendor(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.save_new_vendor))).click()
        



