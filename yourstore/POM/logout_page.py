from yourstore.library.library import Base


class Logout_page(Base):

    logout_msg=("xpath","//h1[.='Account Logout']")


    def account_logout(self):
        self.print_text(self.logout_msg)
        return self.display_msg(self.logout_msg)