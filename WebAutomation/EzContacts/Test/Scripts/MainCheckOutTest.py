from EzContacts.Src.PageObject.Pages.StartPageMain import MainSignIn
from EzContacts.Src.TestBase.WebDriverUtility import EnvironmentSetup
from time import sleep
import unittest



class ezContacts_checkout(EnvironmentSetup):
    def test_checkout_page(self):
            
        driver = self.driver
        
        mainLogin = MainSignIn(driver)
        try:
            mainLogin.MainLogIn()
            mainLogin.setMainEmail()
            mainLogin.setMainReturningCustomer().click()
            mainLogin.setMainPassword()
            mainLogin.MainSubmit().click()
            mainLogin.MainSunglassesLink().click()
            mainLogin.MainSunglassesFilter().click()
            sleep(4)
            mainLogin.MainSunglassesPrice().click()
            sleep(4)
            mainLogin.MainSunglassesItem().click()
            sleep(4)
            mainLogin.MainSunglassesAddToCart().click()
            sleep(4)
            mainLogin.MainSunglassesCheckOut().click()
            sleep(4)
            mainLogin.MainSunglassesAddress().click()
        except Exception as e:
            print("Exception occurred "+e)
        sleep(3)
          
        
#         if mainLogin.PopUpTT().is_displayed():
#             mainLogin.PopUpTT().click()
#         else:
#             print ("Element not found")
       
        driver.quit()
        
        
if __name__ == '__main__':
    unittest.main()
