import pytest

from web_automation_framework.tests.base_test import BaseTest
from web_automation_framework.tests.login.logged_in_successfully_ui import LoggedInSuccessfullyPageUi
from web_automation_framework.ui_pages.ui_pages.login_page2_ui import LoginPage2Ui


class Login2BaseTest(BaseTest):
    """
    Class with common methods for login2 test cases
    """
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login2_ui = LoginPage2Ui(driver)

    def navigate_to_login2_page(self):
        """
        Method to navigate to login2 page
        """
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def insert_username(self, username: str = None):
        """
        Method to insert username
        :param username: str with valid or invalid username
        """
        return self.find(*self.login2_ui.username_box).send_keys(username)

    def insert_password(self, password: str = None):
        """
        Method to insert password
        :param password: str with valid or invalid password
        """
        return self.find(*self.login2_ui.password_box).send_keys(password)


    def click_on_submit(self):
        """
        Method to click on submit button
        :return: LoggedInSuccessfullyPageUi
        """
        self.click(*self.login2_ui.submit_btn)
        return LoggedInSuccessfullyPageUi(self.driver)