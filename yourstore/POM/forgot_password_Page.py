from yourstore.library.library import Base


class Forgot_password_page(Base):

    message=("xpath","//p[.='Enter the e-mail address associated with your account. Click submit to have a password reset link e-mailed to you.']")


    def me_ssage(self):
        self.print_text(self.message)
        self.display_msg(self.message)