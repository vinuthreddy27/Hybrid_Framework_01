from yourstore.library.library import Base


class Password_change_page(Base):

    password = ("name", "password")
    c_password = ("name", "confirm")
    conform_btn = ("xpath", "//input[@value='Continue']")
    password_error_msg = ("xpath", "//div[.='Password must be between 4 and 20 characters!']")
    error_msg=("xpath","//div[.='Password confirmation does not match password!']")

    def change(self,password,c_pass):
        self.element_to_be_visible(self.password)
        self.send_text_to_textfield(self.password,password)
        self.send_text_to_textfield(self.c_password,c_pass)
        self.click_on_element(self.conform_btn)

    def display_error_msg(self):
        self.print_text(self.error_msg)
        self.display_msg(self.error_msg)

    def display_error_msg2(self):
        self.print_text(self.password_error_msg)
        self.display_msg(self.password_error_msg)
