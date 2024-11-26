from yourstore.POM.enqiry_page import Enquiry_page
from yourstore.POM.gift_page import Gift_page
from yourstore.POM.login_page import Loginpage
from yourstore.POM.logout_page import Logout_page
from yourstore.POM.register_page import  Registerpage
from yourstore.POM.search_page import Search_page
from yourstore.library.library import Base

class Homepage(Base):

    my_account_locator = ("xpath", "//span[.='My Account']")
    register_locator = ("xpath", "//a[.='Register']")
    login_locator = ("xpath", "//a[.='Login']")

    search_locator = ("name", "search")
    search_btn = ("xpath", "//button[@class='btn btn-default btn-lg']")

    logout_btn = ("xpath", "//ul[@class='dropdown-menu dropdown-menu-right']/..//a[.='Logout']")

    gift_locator=("xpath","//a[.='Gift Certificates']")

    contact_us_locator = ("xpath", "//a[.='Contact Us']")

    wishlist_link=("id","wishlist-total")

    cart_total=("css selector","*[id='cart']")

    shopping_cart=("css selector","a[title='Shopping Cart']")

    downloads_link=("xpath","//li[@class='dropdown']//li[.='Downloads']")
    transactions_link=("xpath","//li[@class='dropdown']//li[.='Transactions']")
    order_history_link=("xpath","//li[@class='dropdown']//li[.='Order History']")
    logout_link= ("xpath","//ul[starts-with(@class,'dropdown')]//a[.='Logout']")

    def register(self):
        self.click_on_element(self.my_account_locator)
        self.click_on_element(self.register_locator)

        return Registerpage(self.driver)

    def login_(self):
        self.click_on_element(self.my_account_locator)
        self.click_on_element(self.login_locator)

        return Loginpage(self.driver)

    def send_product(self,product):
        self.send_text_to_textfield(self.search_locator,product)
        self.click_on_element(self.search_btn)

        return Search_page(self.driver)

    def gift_link(self):
        self.click_on_element(self.gift_locator)

        return Gift_page(self.driver)


    def contact_us(self):
        self.click_on_element(self.contact_us_locator)

        return Enquiry_page(self.driver)

    def logout(self):
        self.click_on_element(self.my_account_locator)
        self.click_on_element(self.logout_link)

        return Logout_page(self.driver)

    def total_cart(self):
        self.click_on_element(self.cart_total)
