from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from web_automation_framework.ui_pages.ui_pages.base_page_ui import BasePageUi


class LoginPageUi(BasePageUi):
    """
    Class for Login Page UI
    """
    LBL_LOGIN_TITLE_PAGE = "Login Page"
    LBL_LOGIN_BTN = "Login"
    LBL_INVALID_USER_MESSAGE = "Your username is invalid!"
    LBL_INVALID_PASSWORD_MESSAGE = "Your password is invalid!"
    LBL_LOGIN_SUCCESS = "You logged into a secure area!"
    LBL_LOGOUT_SUCESS = "You logged out of the secure area!"

    def __init__(self, driver):
        self.username_locator = (By.ID, "username")
        self.password_locator = (By.ID, "password")
        self.button_locator = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.CSS_SELECTOR, "div[id='flash'].flash")
        super().__init__(driver)

    @property
    def loaded(self) -> bool:
        """
        Use to check if login page is loaded
        :return: bool
        """
        try:
            return self.LBL_LOGIN_TITLE_PAGE == self.title_text
        except NoSuchElementException:
            return False
