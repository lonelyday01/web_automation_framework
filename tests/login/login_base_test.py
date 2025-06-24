import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from web_automation_framework.tests.base_test import BaseTest
from web_automation_framework.ui_pages.ui_pages.login_page_ui import LoginPageUi
from web_automation_framework.ui_pages.ui_pages.secure_page_ui import SecurePageUi


class LoginBaseTest(BaseTest):
    """
    Class for login page
    """
    INVALID_USER = "asd@123"
    INVALID_PWD = "asd@123"
    VALID_USER = "tomsmith"
    VALID_PWD = "SuperSecretPassword!"

    @pytest.fixture(autouse=True)
    def setup_login(self, driver):
        self.login_page_ui = LoginPageUi(driver)

    def navigate_login_page(self) -> LoginPageUi:
        """
        Method to navigate login screen
        :return: None
        """
        self.driver.get("https://the-internet.herokuapp.com/login")

    def set_username(self, username) -> None:
        """
        Method to find the username box and set the username
        :param username: str
        :return: None
        """
        self.find(*self.login_page_ui.username_locator).send_keys(username)

    def set_password(self, password) -> None:
        """
        Method to find the password box and set the password
        :param password: str
        :return: None
        """
        self.find(*self.login_page_ui.password_locator).send_keys(password)

    def click_login(self):
        """
        Method to find and click in login button
        :return: None
        """
        self.click(*self.login_page_ui.button_locator)
        return SecurePageUi(self.driver)

    def get_flash_message(self) -> str:
        """
        Method to find and get the flash message displayed after click on login button
        :return: str with the text of flash message
        """
        return self.find(*self.login_page_ui.flash_message).text
