from yourstore.POM.view_cart_page import view_cart_Page
from yourstore.library.library import Base


class Cart_page(Base):

    view_cart=("xpath","//a[.='View Cart']")
    checkout_page=("xpath","//a[.='Checkout']")

    no_stocks=("xpath","//div[@class='alert alert-danger alert-dismissible']")

    def click_on_view_cart(self):
        self.element_to_be_visible(self.view_cart)
        self.click_on_element(self.view_cart)

        view_page=view_cart_Page(self.driver)
        return view_page

    def display_the_info(self):
        self.print_text(self.no_stocks)
        self.display_msg(self.no_stocks)
