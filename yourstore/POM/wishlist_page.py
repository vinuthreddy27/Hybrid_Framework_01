from yourstore.library.library import Base


class wishlist_page(Base):
    remove_btn=("xpath","//a[@data-original-title='Remove']")

    add_2_cart_btn=("xpath","//button[@data-original-title='Add to Cart']")
    alert_msg=("xpath","//div[contains(@class,'alert')]")

    def click_on_remove_btn(self):
        self.click_on_element(self.remove_btn)

    def cart_btn_click(self):
        self.click_on_element(self.add_2_cart_btn)

    def dispaly_msg(self):
        self.print_text(self.alert_msg)
        self.display_msg(self.alert_msg)