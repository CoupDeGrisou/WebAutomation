from selenium.webdriver.common.by import By
from EzContacts.Src.PageObject.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from EzContacts.Src.TestBase.MainUserInformation import MainUserInfo


class MainSignIn(object):


    def __init__(self, driver):
        self.driver = driver
        driver.get("https://staging.ezcontacts.com")

        self.mainLogIn = driver.find_element(By.XPATH, Locator.main_log_In)
     
    def MainLogIn(self):
        self.mainLogIn.click() 

    def setMainEmail(self, mainUser_email):
        driver = self.driver
        self.Locator.main_email.clean()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.main_email))).send_keys(MainUserInfo.mainUser_email)
       
    def setMainReturningCustomer(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.main_returning_user)))
                
    def setMainPassword(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, Locator.main_password))).send_keys(MainUserInfo.mainUser_pass)
       
    def MainSubmit(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, Locator.main_sign_in_button)))
    
    def MainSunglassesLink(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.main_sunglasses_link)))
    
    def MainSunglassesFilter(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.main_sunglasses_filter)))
    
    def MainSunglassesPrice(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.main_sunglasses_price)))
    
    def MainSunglassesItem(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.main_sunglasses_item)))

    def MainSunglassesAddToCart(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.main_sunglasses_add_cart)))
        
    def MainSunglassesCheckOut(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, Locator.main_sunglasses_checkout_button))).click()

    def MainSunglassesAddress(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, Locator.main_address_button)))




    
    def PopUpTT(self):  
        driver = self.driver  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'TTSubWindowClose')))
