from yourstore.library.library import Base


class Review_page(Base):
    yourname_tf = ("id", "input-name")
    text_area = ("name", "text")
    rating_rb = ("xpath", "//input[@value='5']")
    continue_btn = ("id", "button-review")

    proper_msg=("xpath","//*[.=' Thank you for your review. It has been submitted to the webmaster for approval.']")
    rating_warning=("xpath","//div[.=' Warning: Please select a review rating!']")
    review_msg_warning=("xpath","//div[.=' Warning: Review Text must be between 25 and 1000 characters!']")
    review_name_error=("xpath","//div[.=' Warning: Review Name must be between 3 and 25 characters!']")

    def add_a_review(self,yourname,text):
        self.send_text_to_textfield(self.yourname_tf,yourname)
        self.send_text_to_textfield(self.text_area,text)
        self.click_on_element(self.rating_rb)
        self.click_on_element(self.continue_btn)

    def add_review_2(self):
        self.send_text_to_textfield(self.yourname_tf,"vi")
        self.send_text_to_textfield(self.text_area,"hello i am revewing your product")
        self.click_on_element(self.rating_rb)
        self.click_on_element(self.continue_btn)

    def add_review_3(self):
        self.send_text_to_textfield(self.yourname_tf, "abcdefghijklmnopqrstuvwxyzabcdefghgkj")
        self.send_text_to_textfield(self.text_area, "hello i am revewing your product")
        self.click_on_element(self.rating_rb)
        self.click_on_element(self.continue_btn)

    def add_review_4(self):
        self.send_text_to_textfield(self.yourname_tf, "abcdefghijklmnopqrstuvwxyzabcdefghgkj")
        self.send_text_to_textfield(self.text_area, "hello i am revewing your product")
        self.click_on_element(self.continue_btn)

    def add_review_5(self):
        self.send_text_to_textfield(self.yourname_tf, "abcdefghijklmnopqrstuvwxyzabcdefghgkj")
        self.send_text_to_textfield(self.text_area, "hello i")
        self.click_on_element(self.rating_rb)
        self.click_on_element(self.continue_btn)

    def add_review_6(self):
        self.send_text_to_textfield(self.yourname_tf, "")
        self.send_text_to_textfield(self.text_area, "")
        self.click_on_element(self.continue_btn)

    def error_msg(self):
        self.print_text(self.review_name_error)
        self.display_msg(self.review_name_error)

    def rating_error_msg(self):
        self.print_text(self.rating_warning)
        self.display_msg(self.rating_warning)

    def error_review_text(self):
        self.print_text(self.review_msg_warning)
        self.display_msg(self.review_msg_warning)

    def success_msg(self):
        self.print_text(self.proper_msg)
        self.display_msg(self.proper_msg)