from yourstore.POM.registersuccess_page import Account_success
from yourstore.library.library import Base


class Registerpage(Base):
    first_name_locator = ("id", "input-firstname")
    last_name_locator = ("id", "input-lastname")
    email_locator = ("id", "input-email")
    telephone_locator = ("id", "input-telephone")
    password_locator = ("id", "input-password")
    conform_password_locator = ("id", "input-confirm")
    radio_btn = ("xpath", "//label[@class='radio-inline']/input[@value = '1']")
    privacy_policy_check_box_btn = ("xpath", "//input[@type='checkbox']")
    register_btn = ("xpath", "//input[@value='Continue']")


    first_name_error_msg=()
    last_name_error_msg=("xpath","//div[.='Last Name must be between 1 and 32 characters!']")
    telephone_error_msg=("xpath","//div[.='Telephone must be between 3 and 32 characters!']")
    invalid_email_error_msg=("xpath","//div[.='E-Mail Address does not appear to be valid!']")
    same_email_error_msg=("xpath", "//div[.='Warning: E-Mail Address is already registered!']")
    password_error_msg=()
    c_password_error_msg=()


    def register_form(self,fn,ln,email,ph_no,password,c_password):
        self.send_text_to_textfield(self.first_name_locator,fn)
        self.send_text_to_textfield(self.last_name_locator,ln)
        self.send_text_to_textfield(self.email_locator,email)
        self.send_text_to_textfield(self.telephone_locator,ph_no)
        self.send_text_to_textfield(self.password_locator,password)
        self.send_text_to_textfield(self.conform_password_locator,c_password)
        self.click_on_element(self.radio_btn)
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

        return Account_success(self.driver)
