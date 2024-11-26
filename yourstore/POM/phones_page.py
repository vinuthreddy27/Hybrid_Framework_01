from yourstore.library.library import Base


class Phone_page(Base):

    wishlist_btn=("xpath","//button[@data-original-title='Add to Wish List']")

    def add_wishlist(self):
        self.click_on_element(self.wishlist_btn)