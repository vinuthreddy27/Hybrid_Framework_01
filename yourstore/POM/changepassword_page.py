from yourstore.library.library import Base


class Password_change_page(Base):
    password = ("name", "password")
    c_password = ("name", "confirm")
    conform_btn = ("xpath", "//input[@value='Continue']")


    def change(self,password,c_pass):
        self.send_text_to_textfield(self.password,password)
        self.send_text_to_textfield(self.c_password,c_pass)
        self.click_on_element(self.conform_btn)

