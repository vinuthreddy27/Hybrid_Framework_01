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

        return Modify_account(self.driver)

    def change_password(self):
        self.click_on_element(self.change_password_locator)

        return Password_change_page(self.driver)

    def edit_affiliate_account(self):
        self.click_on_element(self.A_account_link)

        return Edit_affiliate(self.driver)

    def click_address(self):
        self.click_on_element(self.address_link)
        self.click_on_element(self.new_address_link)

        return Address_page_locators(self.driver)

    def newsletter_link(self):
        self.click_on_element(self.subscription)

        return Subscription_page(self.driver)

    def password_changed(self):
        self.print_text(self.success_pass_changed)
        return self.display_msg(self.success_pass_changed)