from yourstore.library.library import Base


class Gift_page(Base):

    receipient_locator=("id","input-to-name")
    receipient_email=("id","input-to-email")
    your_name=("id","input-from-name")
    your_email=("id","input-from-email")
    birthday_btn=("xpath","//input[@value='7']")
    message=("xpath","//textarea[@id='input-message']")
    amount=("xpath","//input[@name='amount']")
    agree_checkbox=("xpath","//input[@name='agree']")
    continue_btn=("xpath","//input[@value='Continue']")



    def gift(self,name,mail,yn,email,msg,amnt):
        self.send_text_to_textfield(self.receipient_locator,name)
        self.send_text_to_textfield(self.receipient_email,mail)
        self.send_text_to_textfield(self.your_name,yn)
        self.send_text_to_textfield(self.your_email,email)
        self.click_on_element(self.birthday_btn)
        self.send_text_to_textfield(self.message,msg)
        self.send_text_to_textfield(self.amount,amnt)
        self.click_on_element(self.agree_checkbox)
        # self.click_on_element(self.continue_btn)
