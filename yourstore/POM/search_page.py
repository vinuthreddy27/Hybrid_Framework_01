from yourstore.POM.review_page import Review_page
from yourstore.library.library import Base


class Search_page(Base):

    product = ("link text", "iMac")
    product__=("link text","HP LP3065")
    review_link = ("xpath", "//a[.='Write a review']")
    product_link=("xpath","//p[@class='price']/..//a[.='Samsung Galaxy Tab 10.1']")
    product_link2= ("link text","iPod Touch")

    cart_=("xpath","//span[.='Add to Cart']")

    image1 = ("xpath", "//img[contains(@src,'ipod_touch_1-228x228.jpg')]")
    next_btn = ("xpath", "//button[@title='Next (Right arrow key)']")
    prev_btn = ("xpath", "//button[@title='Previous (Left arrow key)']")
    close_btn =("xpath","//button[@title='Close (Esc)']")

    cart_btn=("id","button-cart")
    quantity_locator = ("name", "quantity")

    no_product_msg=("xpath","//p[.='There is no product that matches the search criteria.']")

    wishlist_bt= ("xpath", "//span[.='Add to Cart']/../..//i[@class='fa fa-heart']")

    wishlist_btn = ("xpath", "//button[@data-original-title='Add to Wish List']")

    wishlist_success_msg=("xpath","//div[@class='alert alert-success alert-dismissible']")



    def added_to_wishlist(self):
        self.click_on_element(self.wishlist_btn)
        self.element_to_be_visible(self.wishlist_success_msg)
        self.print_text(self.wishlist_success_msg)
        self.display_msg(self.wishlist_success_msg)

    def product_info(self):
        self.click_on_element(self.product_link)

    def product1(self):
        self.click_on_element(self.product)
        self.click_on_element(self.review_link)

        review_page=Review_page(self.driver)
        return review_page

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

    def add_2_cart(self):
        self.click_on_element(self.cart_)


    def click_link(self):
        self.click_on_element(self.product__)

    def success_Msg(self):
      self.element_to_be_visible(self.wishlist_success_msg)
      self.print_text(self.wishlist_success_msg)
      self.display_msg(self.wishlist_success_msg)


    def product_Msg(self):

      self.print_text(self.no_product_msg)
      self.display_msg(self.no_product_msg)

