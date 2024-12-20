from yourstore.POM.landing_page import Landing_page
from yourstore.POM.registersuccess_page import Account_success
from yourstore.POM.subscription_page import Subscription_page
from yourstore.library.library import Base


class Registerpage(Base):

    login_link=("link text","login page")

    first_name_locator = ("id", "input-firstname")
    last_name_locator = ("id", "input-lastname")
    email_locator = ("id", "input-email")
    telephone_locator = ("id", "input-telephone")
    password_locator = ("id", "input-password")
    conform_password_locator = ("id", "input-confirm")
    radio_btn = ("xpath", "//label[@class='radio-inline']/input[@value = '1']")
    no_btn=("xpath", "//label[@class='radio-inline']/input[@value = '2']")
    privacy_policy_check_box_btn = ("xpath", "//input[@type='checkbox']")
    register_btn = ("xpath", "//input[@value='Continue']")

    first_name_error_msg=("xpath","//div[.='First Name must be between 1 and 32 characters!']")
    last_name_error_msg=("xpath","//div[.='Last Name must be between 1 and 32 characters!']")
    telephone_error_msg=("xpath","//div[.='Telephone must be between 3 and 32 characters!']")
    invalid_email_error_msg=("xpath","//div[.='E-Mail Address does not appear to be valid!']")
    same_email_error_msg=("xpath", "//div[.='Warning: E-Mail Address is already registered!']")
    password_error_msg=("xpath","//div[.='Password must be between 4 and 20 characters!']")
    conform_password_Error_msg=("xpath","//div[.='Password confirmation does not match password!']")


    def register_form(self,fn,ln,ph_no,password,c_password):
        self.send_text_to_textfield(self.first_name_locator,fn)
        self.send_text_to_textfield(self.last_name_locator,ln)
        self.send_text_to_textfield(self.email_locator,self.generate_random_email())
        self.send_text_to_textfield(self.telephone_locator,ph_no)
        self.send_text_to_textfield(self.password_locator,password)
        self.send_text_to_textfield(self.conform_password_locator,c_password)
        self.click_on_element(self.radio_btn)
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)


        account_success_page=Account_success(self.driver)
        return account_success_page


    def register_form_mandator_Fields(self,fn,ln,ph_no,password,c_password):
        self.send_text_to_textfield(self.first_name_locator,fn)
        self.send_text_to_textfield(self.last_name_locator,ln)
        self.send_text_to_textfield(self.email_locator,self.generate_random_email())
        self.send_text_to_textfield(self.telephone_locator,ph_no)
        self.send_text_to_textfield(self.password_locator,password)
        self.send_text_to_textfield(self.conform_password_locator,c_password)
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

        account_success_page = Account_success(self.driver)
        return account_success_page



    def register_with_no_fn(self):
        self.send_text_to_textfield(self.first_name_locator,"")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with__invalid_fn(self):
        self.send_text_to_textfield(self.first_name_locator, "vinuth71")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_fn_32(self):
        self.send_text_to_textfield(self.first_name_locator, "abcdefghijklmnopqrstuuvwxyzaabbccdd")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def fn_error_msg(self):
        self.print_text(self.first_name_error_msg)
        self.display_msg(self.first_name_error_msg)

    def register_with_fn_with_special_charater(self):
        self.send_text_to_textfield(self.first_name_locator, "$martin")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_ln(self):
        self.send_text_to_textfield(self.last_name_locator, "")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_email(self):
        self.send_text_to_textfield(self.email_locator, "reddyvinuth27gmail.com")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_sameEmail(self):
        self.send_text_to_textfield(self.first_name_locator, "reddyvinuth27@gmail.com")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_password(self):
        self.send_text_to_textfield(self.password_locator, "")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)


    def error_msg(self):
        self.print_text(self.first_name_error_msg)
        self.display_msg(self.first_name_error_msg)

    def phno_error_msg(self):
        self.print_text(self.telephone_error_msg)
        self.display_msg(self.telephone_error_msg)

    def register_with_wrong_telephone_number(self):
        self.send_text_to_textfield(self.telephone_locator,"898989898.9")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_wrong_telephone_number2(self):
        self.send_text_to_textfield(self.telephone_locator,"67788998000")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_wrong_telephone_number3(self):
        self.send_text_to_textfield(self.telephone_locator,"rv9980766669")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_no_telephone_number3(self):
        self.send_text_to_textfield(self.telephone_locator,"")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register_with_invalid_telephone_number3(self):
        self.send_text_to_textfield(self.telephone_locator, "78767$8669")
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register(self):
        self.send_text_to_textfield(self.first_name_locator,"martin")
        self.send_text_to_textfield(self.last_name_locator,"chris")
        self.send_text_to_textfield(self.email_locator,"mortein11@gmail.com")
        self.send_text_to_textfield(self.telephone_locator,"8889997776")
        self.send_text_to_textfield(self.password_locator,"selenium")
        self.send_text_to_textfield(self.conform_password_locator,"framework")
        self.click_on_element(self.radio_btn)
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

    def register2(self,fn,ln,ph_no,password,c_password):
        self.send_text_to_textfield(self.first_name_locator,fn)
        self.send_text_to_textfield(self.last_name_locator,ln)
        self.send_text_to_textfield(self.email_locator,self.generate_random_email())
        self.send_text_to_textfield(self.telephone_locator,ph_no)
        self.send_text_to_textfield(self.password_locator,password)
        self.send_text_to_textfield(self.conform_password_locator,c_password)
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

        landing_page=Landing_page(self.driver)
        return landing_page

    def register3(self,fn,ln,ph_no,password,c_password):
        self.send_text_to_textfield(self.first_name_locator,fn)
        self.send_text_to_textfield(self.last_name_locator,ln)
        self.send_text_to_textfield(self.email_locator,self.generate_random_email())
        self.send_text_to_textfield(self.telephone_locator,ph_no)
        self.send_text_to_textfield(self.password_locator,password)
        self.send_text_to_textfield(self.conform_password_locator,c_password)
        self.click_on_element(self.radio_btn)
        self.click_on_element(self.privacy_policy_check_box_btn)
        self.click_on_element(self.register_btn)

        landing_page=Landing_page(self.driver)
        return landing_page

    def password_warning_msg(self):
        self.print_text(self.password_error_msg)

    def con_password_error_msg(self):
        self.element_to_be_visible(self.conform_password_Error_msg)
        self.print_text(self.conform_password_Error_msg)
        self.display_msg(self.conform_password_Error_msg)


    def click_on_login(self):
        self.click_on_element(self.login_link)
