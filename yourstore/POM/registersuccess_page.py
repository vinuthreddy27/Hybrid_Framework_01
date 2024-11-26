from yourstore.library.library import Base


class Account_success(Base):
    registered_msg=\
        ("xpath", "//div[@id='content']/.//p[.='Congratulations! Your new account has been successfully created!']")


    def msg__(self):
        return self.display_msg(self.registered_msg)
