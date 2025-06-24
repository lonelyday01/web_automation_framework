from selenium.common import NoSuchElementException
from web_automation_framework.ui_pages.activities.base_page_activity import BasePageActivity


class LoginPageActivity(BasePageActivity):
    """
    Class for Login Page Activity
    """
    def __init__(self, driver):
        self.LBL_LOGIN_TITLE_PAGE = "Login Page"
        self.LBL_LOGIN_BTN = "Login"
        self.LBL_INVALID_USER_MESSAGE = "Your username is invalid!"
        self.LBL_INVALID_PASSWORD_MESSAGE = "Your password is invalid!"
        self.lbl_LOGIN_SUCCESS = "You logged into a secure area!"
        super().__init__(driver=driver)

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
