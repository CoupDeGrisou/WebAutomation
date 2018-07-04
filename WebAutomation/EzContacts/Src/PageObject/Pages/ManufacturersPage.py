from selenium.webdriver.common.by import By
from EzContacts.Src.PageObject.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from random import random


class Manufacturer(object):
    
    def __init__(self, driver):
        self.driver = driver
        self.manufacturerLink = driver.find_element(By.XPATH, Locator.manufacturer_link)

    def setManufacturerLink(self):
        self.manufacturerLink.click()
        
    def setAddNewManufacturer(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.add_manufacturer))).click()
    
    def setManufacturerName(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, Locator.manufacturer_name))).send_keys("Autotest_Manufacturer_"+str(random()))
    
    def setSaveNewManufacturer(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.save_new_manufacturer))).click()
        
