from yourstore.library.library import Base


class Edit_affiliate(Base):

    company_text_field = ("name", "company")
    website_textfield = ("name", "website")
    tax_textfield = ("name", "tax")
    payment_mode_btn = ("xpath", "//input[@value='paypal']")
    paypal_textfield = ("name", "paypal")
    continue_btn = ("xpath", "//input[@type='submit']")

    def edit_affiliate(self,company_name,website,tax,pay):
        self.send_text_to_textfield(self.company_text_field,company_name)
        self.send_text_to_textfield(self.website_textfield,website)
        self.send_text_to_textfield(self.tax_textfield,tax)
        self.click_on_element(self.payment_mode_btn)
        self.send_text_to_textfield(self.paypal_textfield,pay)
        self.click_on_element(self.continue_btn)



