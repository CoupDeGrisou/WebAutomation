
class Locator(object):
    
    
    #sign in page locator (_admin_)
    signIn_username = "UserEmail"
    signIn_password = "UserPassword"
    signIn_button = "//button[contains(text(), 'Sign In')]"
    
    
    #################################
    #Main site
    main_log_In = "//a[contains(text(), 'Log in')]"
    main_email = "//input[@id='UserEmail']"
    main_returning_user = "//label[contains(text(), 'Returning Customer')]"
    main_password = "new-password"
    main_sign_in_button = "sign-in-submit-btn"
    
    main_sunglasses_link = "(//a[@href='/sunglasses'])[2]"
    main_sunglasses_filter = "(//label[contains(text(), 'Sunglasses for Men')])[2]"
    main_sunglasses_price = "(//span[contains(text(), '$150-$199')])[2]"
    main_sunglasses_item = "(//span[contains(text(), 'View Item')])[6]"
    main_sunglasses_add_cart = "(//a[contains(text(), 'Add to Cart')])[2]"
    main_sunglasses_checkout_button = "(//a[contains(text(), 'Checkout Now')])[1]"
    main_address_button = "add-shipping-address"
    main_credit_card = "AppProductCardNumber"
    main_cc_expiry_month = "AppProductExpiryMonth"
    main_cc_expiry_year = "AppProductExpiryYear"
    main_cc_CVC = "AppProductCvc"
    main_place_order_button = "add-billing-address"
    
   
    #################################
    
    #System setup link (_admin_)
    system_setup_link = "//span[contains(text(), 'System Setup')]"
    
    #vendors (_admin_)
    vendors_link = "(//a[@href='/admin-manage/business/vendors'])[1]"
    add_vendor = "//a[contains(text(), 'Add New Vendor')]"
    vendor_name = "BusinessName"
    save_new_vendor = "(//input[@class='btn btn-primary'])[1]"
    
    #manufacturer (_admin_)
    manufacturer_link = "(//a[@href='/admin-manage/manufacturers'])[1]"
    add_manufacturer = "//a[contains(text(), 'Add New Manufacturer')]"
    manufacturer_name = "ManufacturerName"
    save_new_manufacturer = "(//input[@class='btn btn-primary'])[1]"
    
    #Product link (_admin_)
    product_link = "//span[contains(text(), 'Products')]"
    
    #products (_admin_)
    eyeglasses_link = "(//a[@href='/admin-manage/products/eyeglasses'])[1]"
    contact_lenses_link = "(//a[@href='/admin-manage/products/contact-lenses'])[1]"
    
  
