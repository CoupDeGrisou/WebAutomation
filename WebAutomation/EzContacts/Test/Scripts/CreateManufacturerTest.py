from EzContacts.Src.PageObject.Pages.StartPage import SignIn, NavigationPanel
from EzContacts.Src.TestBase.WebDriverUtility import EnvironmentSetup
from time import sleep
from EzContacts.Src.PageObject.Pages.ManufacturersPage import Manufacturer
import unittest



class ezContacts_manufacturer(EnvironmentSetup):

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

        new_Manufacturer = Manufacturer(driver)
        new_Manufacturer.setManufacturerLink()
        new_Manufacturer.setAddNewManufacturer()
        sleep(3)  
        new_Manufacturer.setManufacturerName()
        sleep(3)
        new_Manufacturer.setSaveNewManufacturer()
        
        driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()