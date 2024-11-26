from yourstore.library.library import Base


class Compare_page(Base):

    product_locator4=("xpath","//img[contains(@src,'palm_treo_pro_1-228x228.jpg')]")
    product_locator2=("xpath","//a[.='Sony VAIO']")
    compare_btn=("xpath","//button[@data-original-title='Compare this Product']")
    compare_link=("id","compare-total")
    remove_btn4=("xpath","//a[contains(@href,'compare&remove=46')]/..//a")
    add_to_cart_btn4=("xpath","//a[contains(@href,'compare&remove=29')]/..//input")

    remove_btn2 = ("xpath","//button[@title='Remove']")
