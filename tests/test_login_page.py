import pytest
from web_automation_framework.pages.login_page import LoginPage


class TestLoginPage:
    """
    Class to validate all the resources in LoginPage
    """
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.login_page = LoginPage(driver)

    def test_valid_login(self):
        """
        Method to test a valid login
        """
        loging_act = self.login_page.navigate_login_page()
        assert loging_act.loaded, "Login Page is not loaded"
        self.login_page.set_username("tomsmith")
        self.login_page.set_password("SuperSecretPassword!")
        self.login_page.click_login()
        assert loging_act.lbl_LOGIN_SUCCESS in self.login_page.get_flash_message(), f"Error login {self.login_page.get_flash_message()}"
