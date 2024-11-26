from time import sleep

from yourstore.library.library import Base

class Address_page_locators(Base):
    fn=("name","firstname")
    ln=("name","lastname")
    company=("name","company")
    address=("name","address_1")
    address2=("name","address_2")
    city=("name","city")
    post_code=("name","postcode")
    country_dropdown=("name","country_id")
    state=("name","zone_id")
    radio_btn=("css selector","input[value='1']")
    continue_btn=("css selector","input[value='Continue']")

    def default_Address(self,fn,ln,company,address,address2,city,postcode,option,state):
        self.send_text_to_textfield(self.fn,fn)
        self.send_text_to_textfield(self.ln, ln)
        self.send_text_to_textfield(self.company, company)
        self.send_text_to_textfield(self.address, address)
        self.send_text_to_textfield(self.address2,address2)
        self.send_text_to_textfield(self.city,city)
        self.send_text_to_textfield(self.post_code,postcode)
        self.select_a_option(self.country_dropdown,option)
        sleep(2)
        self.select_a_option(self.state,state)
        self.click_on_element(self.radio_btn)
        self.click_on_element(self.continue_btn)

