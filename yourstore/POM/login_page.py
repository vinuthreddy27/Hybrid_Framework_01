from yourstore.POM.landing_page import Landing_page
from yourstore.library.library import Base


class Loginpage(Base):
    email_locator = ("id", "input-email")
    password_locator = ("id", "input-password")
    login_btn = ("xpath", "//input[@value='Login']")
    warning_message = ("xpath", "//div[.='Warning: No match for E-Mail Address and/or Password.']")

    def login_into_application(self,email,password):
        self.send_text_to_textfield(self.email_locator,email)
        self.send_text_to_textfield(self.password_locator,password)
        self.Submit(self.password_locator)

        return Landing_page(self.driver)
