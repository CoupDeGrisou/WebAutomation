from EzContacts.Src.PageObject.Pages.StartPage import SignIn, NavigationPanel
from EzContacts.Src.PageObject.Pages.VendorPage import Vendors
from EzContacts.Src.TestBase.WebDriverUtility import EnvironmentSetup
from time import sleep
import unittest

class ezContacts_vendors(EnvironmentSetup):

    #(threadCount=10)
    def test_create_vendor(self):
            
        driver = self.driver
        
        login = SignIn(driver)
        try:
            login.setUser()
            login.setPass()
            login.submit()
        except Exception as e:
            print("Exception occurred "+e)
        sleep(3)

        system_setupLink = NavigationPanel(driver)
        try:
            system_setupLink.setSystemSetup()
        except Exception as e:
            print("Exception occurred "+e)
        sleep(3)

        new_vendor = Vendors(driver)
        new_vendor.setVendorLink()
        new_vendor.setAddNewVendor()
        sleep(3)  
        new_vendor.setVendorName()
        sleep(3)
        new_vendor.setSaveNewVendor()
        
        driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()