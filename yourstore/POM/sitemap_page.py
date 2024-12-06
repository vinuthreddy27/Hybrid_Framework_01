from yourstore.library.library import Base


class sitemap_page(Base):
    password_link=("link text","Password")


    def click_on_password(self):
        self.click(self.password_link)