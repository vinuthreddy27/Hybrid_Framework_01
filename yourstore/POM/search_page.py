from yourstore.POM.review_page import Review_page
from yourstore.library.library import Base


class Search_page(Base):
    product = ("link text", "iMac")
    product__=("link text","HP LP3065")
    review_link = ("xpath", "//a[.='Write a review']")
    product_link=("xpath","//p[@class='price']/..//a[.='Samsung Galaxy Tab 10.1']")
    product_link2= ("link text","iPod Touch")

    image1 = ("xpath", "//img[contains(@src,'ipod_touch_1-228x228.jpg')]")
    next_btn = ("xpath", "//button[@title='Next (Right arrow key)']")
    prev_btn = ("xpath", "//button[@title='Previous (Left arrow key)']")
    close_btn =("xpath","//button[@title='Close (Esc)']")
    cart_btn=("xpath","//button[.='Add to Cart']")
    quantity_locator = ("name", "quantity")


    wishlist_bt= ("xpath", "//span[.='Add to Cart']/../..//i[@class='fa fa-heart']")


    wishlist_btn = ("xpath", "//button[@data-original-title='Add to Wish List']")
    success_msg=("xpath","//div[contains(@class,'alert')]/a[.='shopping cart']")

    def add_wishlist(self):
        self.click_on_element(self.wishlist_btn)

    def added_to_wishlist(self):
       return self.display_msg(self.success_msg)

    def product_info(self):
        self.click_on_element(self.product_link)

    def product1(self):
        self.click_on_element(self.product)
        self.click_on_element(self.review_link)

        return Review_page(self.driver)

    def product_(self):
        self.click_on_element(self.product_link2)
        self.click_on_element(self.image1)
        self.click_on_element(self.next_btn)
        self.click_on_element(self.next_btn)
        self.click_on_element(self.prev_btn)
        self.click_on_element(self.next_btn)
        self.click_on_element(self.next_btn)
        self.click_on_element(self.close_btn)
        self.click_on_element(self.cart_btn)

    def product2(self):
        self.click_on_element(self.product_link2)
        self.send_text_to_textfield(self.quantity_locator,2)
        self.click_on_element(self.cart_btn)

    def click_link(self):
        self.click_on_element(self.product__)

    def success_Msg(self):
      self.display_msg(self.success_msg)
