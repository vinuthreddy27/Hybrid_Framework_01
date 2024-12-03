from yourstore.library.library import Base


class Cart_page(Base):

    view_cart=("xpath","//a[.='View Cart']")
    checkout_page=("xpath","//a[.='Checkout']")

    no_stocks=("xpath","//div[@class='alert alert-danger alert-dismissible']")

    def click_on_view_cart(self):
        self.click_on_element(self.view_cart)

    def display_the_info(self):
        self.print_text(self.no_stocks)
        self.display_msg(self.no_stocks)
