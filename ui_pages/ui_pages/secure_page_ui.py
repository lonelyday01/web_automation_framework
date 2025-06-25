from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from web_automation_framework.ui_pages.ui_pages.base_page_ui import BasePageUi


class SecurePageUi(BasePageUi):
    """
    Class for Secure Page UI
    """
    LBL_SECURE_TITLE_PAGE = "Secure Area"
    LBL_LOGOUT_BTN = "Logout"
    
    def __init__(self, driver):
        super().__init__(driver)
        self.button_locator = (By.CSS_SELECTOR, "a.button.secondary")


    @property
    def loaded(self):
        """
        Use to check if secure page is loaded
        :return: bool
        """
        try:
            return self.LBL_SECURE_TITLE_PAGE == self.title_text
        except NoSuchElementException:
            return False