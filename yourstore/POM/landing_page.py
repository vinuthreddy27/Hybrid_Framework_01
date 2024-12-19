from yourstore.POM.address_page import Address_page_locators
from yourstore.POM.changepassword_page import Password_change_page
from yourstore.POM.edit_affiliatePage import Edit_affiliate
from yourstore.POM.logout_page import Logout_page
from yourstore.POM.modify_accountpage import Modify_account
from yourstore.POM.subscription_page import Subscription_page
from yourstore.library.library import Base



class Landing_page(Base):
    logout_link=("link text","Logout")
    edit_link = ("xpath", "//a[.='Edit your account information']")
    change_password_locator = ("xpath", "//ul[@class='list-unstyled']/..//a[.='Change your password']")
    A_account_link = ("xpath", "//a[.='Edit your affiliate information']")
    address_link=("link text","Address Book")
    new_address_link=("link text","New Address")
    subscription=("link text", "Newsletter")
    password=("link text","Password")

    success_pass_changed=("xpath","//*[.='Success: Your password has been successfully updated.']")

    def proper_msg(self):
        self.display_msg(self.edit_link)

    def edit_account_info(self):
        self.click_on_element(self.edit_link)

        modify_account_page=Modify_account(self.driver)
        return modify_account_page

    def change_password(self):
        self.element_to_be_visible(self.change_password_locator)
        self.click_on_element(self.change_password_locator)

        password_page=Password_change_page(self.driver)
        return   password_page

    def edit_affiliate_account(self):
        self.click_on_element(self.A_account_link)

        affiliate_page=Edit_affiliate(self.driver)
        return affiliate_page

    def click_address(self):
        self.click_on_element(self.address_link)
        self.click_on_element(self.new_address_link)

        address_page=Address_page_locators(self.driver)
        return address_page

    def newsletter_link(self):
        self.click_on_element(self.subscription)

        subscription_page=Subscription_page(self.driver)
        return subscription_page

    def password_changed(self):
        self.print_text(self.success_pass_changed)
        return self.display_msg(self.success_pass_changed)

    def click_on_logout(self):
        self.click_on_element(self.logout_link)

        logout_page = Logout_page(self.driver)
        return logout_page

    def click_password_link(self):
        self.element_to_be_visible(self.password)
        self.click_on_element(self.password)