from yourstore.POM.brands_page import Brands_page
from yourstore.POM.cart_page import Cart_page
from yourstore.POM.enqiry_page import Enquiry_page
from yourstore.POM.gift_page import Gift_page
from yourstore.POM.login_page import Loginpage
from yourstore.POM.logout_page import Logout_page
from yourstore.POM.order_history_apge import Order_history_page
from yourstore.POM.register_page import  Registerpage
from yourstore.POM.returns_page import Returns_page
from yourstore.POM.search_page import Search_page
from yourstore.POM.sitemap_page import sitemap_page
from yourstore.POM.wishlist_page import wishlist_page
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

    wishlist=("xpath","//span[contains(text(),'Wish List')]")

    cart_total=("css selector","*[id='cart']")

    shopping_cart=("css selector","a[title='Shopping Cart']")

    dropdown_my_account=("link text","My Account")

    return_link=("xpath","//ul[@class='list-unstyled']//a[.='Returns']")

    downloads_link=("xpath","//li[@class='dropdown']//li[.='Downloads']")
    transactions_link=("xpath","//li[@class='dropdown']//li[.='Transactions']")
    order_history_link=("xpath","//li[@class='dropdown']//li[.='Order History']")
    logout_link= ("xpath","//ul[starts-with(@class,'dropdown')]//a[.='Logout']")

    footer_my_account=("link text","My Account")
    sitemap_link=("link text","Site Map")
    brands_link=("xpath","//a[.='Brands']")
    order_history=("xpath","//ul[@class='list-unstyled']//a[.='Order History']")

    def register(self):
        self.click_on_element(self.my_account_locator)
        self.click_on_element(self.register_locator)

        register_page=Registerpage(self.driver)
        return register_page

    def login_(self):
        self.click_on_element(self.my_account_locator)
        self.click_on_element(self.login_locator)

        login_page=Loginpage(self.driver)
        return login_page

    def send_product(self,product):
        self.send_text_to_textfield(self.search_locator,product)
        self.click_on_element(self.search_btn)

        search_page=Search_page(self.driver)
        return search_page

    def gift_link(self):
        self.click_on_element(self.gift_locator)

        gift_page=Gift_page(self.driver)
        return gift_page


    def contact_us(self):
        self.click_on_element(self.contact_us_locator)

        enquiry_page=Enquiry_page(self.driver)
        return enquiry_page

    def logout(self):
        self.click_on_element(self.my_account_locator)
        self.click_on_element(self.logout_link)

        logout_page=Logout_page(self.driver)
        return logout_page

    def total_cart(self):
        self.click_on_element(self.cart_total)

        cart_page = Cart_page(self.driver)
        return cart_page

    def click_footer_my_Account(self):
        self.click_on_element(self.footer_my_account)

    def click_my_account(self):
        self.click_on_element(self.my_account_locator)
        self.click_on_element(self.dropdown_my_account)

    def click_on_sitemap(self):
        self.click_on_element(self.sitemap_link)

        sitepage=sitemap_page(self.driver)
        return sitepage

    def click_wishlist(self):
        self.click_on_element(self.wishlist)

        wish_page=wishlist_page(self.driver)
        return wish_page

    def click_on_returns(self):
        self.click_on_element(self.return_link)

        returns_page=Returns_page(self.driver)
        return returns_page

    def click_order_history_link(self):
        self.click_on_element(self.order_history)

        o_history_page=Order_history_page(self.driver)
        return o_history_page

    def click_on_brands(self):
        self.click_on_element(self.brands_link)

        brands_page=Brands_page(self.driver)
        return brands_page

    def shopping_cart_click(self):
        self.click_on_element(self.shopping_cart)