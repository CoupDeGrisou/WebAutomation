from selenium.webdriver.common.by import By
from EzContacts.Src.PageObject.Locators import Locator


class SignIn(object):


    def __init__(self, driver):
        self.driver = driver
        driver.get("http://staging.ezcontacts.com/admin-manage")

        self.userName = driver.find_element(By.ID, Locator.signIn_username)
        self.password = driver.find_element(By.ID, Locator.signIn_password)
        self.signIn = driver.find_element(By.XPATH, Locator.signIn_button)

    def setUser(self):
        self.userName.send_keys("leobartleo@gmail.com")
        
    def setPass(self):
        self.password.send_keys("Test123")
        
    def submit(self):
        self.signIn.click()


    
class NavigationPanel(object):
    
    
    def __init__(self, driver):
        self.driver = driver

        self.systemSetup = driver.find_element(By.XPATH, Locator.system_setup_link)
        self.products_link = driver.find_element(By.XPATH, Locator.product_link)
    
    def setSystemSetup(self):
        self.systemSetup.click()
                
    def setProductLink(self):
        self.products_link.click()