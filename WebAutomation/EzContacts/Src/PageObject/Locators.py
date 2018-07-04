
class Locator(object):
    #sign in page locator
    signIn_username = "UserEmail"
    signIn_password = "UserPassword"
    signIn_button = "//button[contains(text(), 'Sign In')]"
    
    
    #System setup link
    system_setup_link = "//span[contains(text(), 'System Setup')]"
    
    #vendors
    vendors_link = "(//a[@href='/admin-manage/business/vendors'])[1]"
    add_vendor = "//a[contains(text(), 'Add New Vendor')]"
    vendor_name = "BusinessName"
    save_new_vendor = "(//input[@class='btn btn-primary'])[1]"
    
    #manufacturer
    manufacturer_link = "(//a[@href='/admin-manage/manufacturers'])[1]"
    add_manufacturer = "//a[contains(text(), 'Add New Manufacturer')]"
    manufacturer_name = "ManufacturerName"
    save_new_manufacturer = "(//input[@class='btn btn-primary'])[1]"
    
    #Product link
    product_link = "//span[contains(text(), 'Products')]"
    
    #products
  
