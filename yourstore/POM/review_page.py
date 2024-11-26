from yourstore.library.library import Base


class Review_page(Base):
    yourname_tf = ("id", "input-name")
    text_area = ("name", "text")
    rating_rb = ("xpath", "//input[@value='5']")
    continue_btn = ("id", "button-review")


    def add_a_review(self,yourname,text):
        self.send_text_to_textfield(self.yourname_tf,yourname)
        self.send_text_to_textfield(self.text_area,text)
        self.click_on_element(self.rating_rb)
        # self.click_on_element(self.continue_btn)

