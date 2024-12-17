
from yourstore.library.library import Base


class Enquiry_page(Base):
    text_area_locator=("name","enquiry")
    name=("name","name")
    email=("name","email")
    submit_btn=("xpath","//input[@value='Submit']")
    continue_btn3=("xpath","//a[.='Continue']")


    def enquiry(self,text):
        self.send_text_to_textfield(self.text_area_locator,text)
        self.click_on_element(self.submit_btn)
        self.click_on_element(self.continue_btn3)