from yourstore.library.library import Base


class view_cart_Page(Base):
    quantity_locator=("xpath","//input[starts-with(@name,'quantity')]")

    update_btn=("css selector","button[data-original-title='Update']")

    def change_quantity(self):
        self.send_text_to_textfield(self.quantity_locator,"5")
        self.click_on_element(self.update_btn)
