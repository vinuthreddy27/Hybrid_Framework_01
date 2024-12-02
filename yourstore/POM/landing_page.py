from yourstore.POM.address_page import Address_page_locators
from yourstore.POM.changepassword_page import Password_change_page
from yourstore.POM.edit_affiliatePage import Edit_affiliate
from yourstore.POM.modify_accountpage import Modify_account
from yourstore.POM.subscription_page import Subscription_page
from yourstore.library.library import Base



class Landing_page(Base):
    edit_link = ("xpath", "//a[.='Edit your account information']")
    change_password_locator = ("xpath", "//ul[@class='list-unstyled']/..//a[.='Change your password']")
    A_account_link = ("xpath", "//a[.='Edit your affiliate information']")
    address_link=("link text","Address Book")
    new_address_link=("link text","New Address")
    subscription=("link text", "Newsletter")

    success_pass_changed=("xpath","//*[.='Success: Your password has been successfully updated.']")

    def edit_account_info(self):
        self.click_on_element(self.edit_link)

        modify_account_page=Modify_account(self.driver)
        return modify_account_page

    def change_password(self):
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