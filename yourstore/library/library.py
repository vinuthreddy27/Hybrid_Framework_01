import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable, \
    alert_is_present, element_located_to_be_selected, presence_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,6)
        self.actions=ActionChains(self.driver)

    def click_on_element(self,locator):
        element=self.wait.until(visibility_of_element_located(locator))
        element.click()

    def send_text_to_textfield(self, locator, text):
        element = self.wait.until(presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def select_a_option(self, locator1, text):
        select_element = self.search_for_element(locator1)
        s1 = Select(select_element)
        s1.select_by_visible_text(text)

    def select_a_option_by_value(self, locator1, value):
        select_element = self.search_for_element(locator1)
        s1 = Select(select_element)
        s1.select_by_value(value)

    def select_a_option_by_index(self, locator1, index):
        select_element = self.search_for_element(locator1)
        s1 = Select(select_element)
        s1.select_by_index(index)

    def accept_alert(self):
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()

    def display_msg(self, locator):
        element = self.search_for_element(locator)
        return element.is_displayed()

    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(locator)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent()

    def navigational_command_back(self):
        self.driver.back()

    def navigational_command_forward(self):
        self.driver.forward()

    def navigational_command_refresh(self):
        self.driver.refresh()

    def take_screenshot(self):
        self.driver.save_screenshot("..//screenshot" + '.png')

    def generate_random_email(self):
            timestamp = time.ctime().split()[3]
            timestamp1 = timestamp.replace(":", "")
            return "vinuth" + timestamp1 + "@gmail.com"

    def element_to_be_visible(self,locator):
        wait=self.wait.until(visibility_of_element_located(locator))
        return wait

    def element_to_be_clickable(self, locator):
        wait=self.wait.until(element_to_be_clickable(locator))
        return wait

    def wait_for_alert(self, locator):
        alert=self.wait.until(alert_is_present())
        return alert

    def waiT(self,locator):
        wait=self.wait.until(element_located_to_be_selected(locator))
        return wait


    def right_click(self,locator):
        element=self.search_for_element(locator)
        self.actions.context_click(element).perform()

    def click(self,locator):
        element=self.search_for_element(locator)
        self.actions.click(element).perform()

    def send_keys(self,locator,text):
        element=self.search_for_element(locator)
        self.actions.send_keys_to_element(element,text).perform()

    def send_keyS(self,text):
        self.actions.send_keys(text).perform()
        
    def hover(self,locator):
        element = self.search_for_element(locator)
        self.actions.move_to_element(element).perform()

    def scroll_by_am(self,x,y):
        self.actions.scroll_by_amount(x,y).perform()

    def scroll_by(self,element):
        self.actions.scroll_to_element(element).perform()

    def search_for_element(self,locator):
        element=self.driver.find_element(*locator)
        return element

    def Submit(self,locator):
        element=self.search_for_element(locator)
        element.submit()

    def verify_radiobtn(self,locator):
        element=self.search_for_element(locator)
        print(element.is_selected())
        return element.is_selected()

    def verify_checkbox(self, locator):
        element = self.search_for_element(locator)
        print(element.is_selected())
        return element.is_selected()

    def print_text(self,locator):
        element=self.search_for_element(locator)
        print(element.text)






    def select_date(self,month_year):
        self.driver.find_element("xpath","//i[@class='fa fa-calendar']").click()
        current=self.driver.find_element("xpath","//th[@class='picker-switch']").text

        while not (current.__eq__(month_year)):
            next_btn = self.driver.find_element("xpath", "//th[@class='next']")
            next_btn.click()
            current = self.driver.find_element("xpath", "//th[@class='picker-switch']").text

        self.driver.find_element("xpath","//td[.='11']").click()

    def previous_date(self, month_year):
        self.driver.find_element("xpath", "//i[@class='fa fa-calendar']").click()
        current = self.driver.find_element("xpath", "//th[@class='picker-switch']").text

        while not (current.__eq__(month_year)):
            next_btn = self.driver.find_element("xpath", "//th[@class='prev']")
            next_btn.click()
            current = self.driver.find_element("xpath", "//th[@class='picker-switch']").text

        self.driver.find_element("xpath", "//td[.='11']").click()


    def switch_window(self):
        parent_window = self.driver.current_window_handle
        all_handles = self.driver.window_handles

        for handle in all_handles:
            if handle != parent_window:
                self.driver.switch_to.window(handle)
                break
        self.driver.switch_to.window(parent_window)

