from yourstore.library.library import Base


class Modify_account(Base):
    telephone_locator = ("name", "telephone")
    continue_btn = ("xpath", "//input[@value='Continue']")


    def modify(self,phno):
     self.send_text_to_textfield(self.telephone_locator, phno)
     self.click_on_element(self.continue_btn)

