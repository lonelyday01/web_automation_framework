from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from web_automation_framework.ui_pages.ui_pages.base_page_ui import BasePageUi
from selenium.webdriver.common.by import By

class LoggedInSuccessfullyPageUi(BasePageUi):
    """
    Class with all page items
    """
    LBL_LOGGED_IN_HEADER = "Logged In Successfully"
    LBL_LOGGED_MESASGE = "Congratulations student. You successfully logged in!"
    def __init__(self, driver):
        super().__init__(driver)
        self.logout_locator = (By.LINK_TEXT, "Log out")
        self.header_locator = (By.CSS_SELECTOR, "div.post-header > h1.post-title")
        self.logged_in_message_locator = (By.CSS_SELECTOR, "div.post-content p.has-text-align-center")
    @property
    def loaded(self):
        try:
            return self.LBL_LOGGED_IN_HEADER == self.title_text
        except NoSuchElementException:
            return False

    @property
    def title_text(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.header_locator)).text
        except (NoSuchElementException, ElementNotVisibleException):
            return None