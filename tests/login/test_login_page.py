from web_automation_framework.tests.login.login_base_test import LoginBaseTest


class TestLoginPage(LoginBaseTest):
    """
    Class to validate all the resources in LoginPage
    """
    def test_valid_login(self):
        """
        Method to test a valid login
        """
        self.navigate_login_page()
        assert self.login_page_ui.loaded, "Login Page is not loaded"
        self.set_username(self.VALID_USER)
        self.set_password(self.VALID_PWD)
        secure_ui = self.click_login()
        assert secure_ui.loaded, "Secure Page is not loaded"
        assert self.is_displayed(*self.login_page_ui.flash_message), "Flash message is not displayed"
        assert self.login_page_ui.LBL_LOGIN_SUCCESS in self.get_flash_message(), f"Error login {self.get_flash_message()}"


    def test_valid_login_and_logout(self):
        """
        Validate Login, Logout process
        """
        self.navigate_login_page()
        assert self.login_page_ui.loaded, "Login Page is not loaded"
        self.set_username(self.VALID_USER)
        self.set_password(self.VALID_PWD)
        secure_ui = self.click_login()
        assert secure_ui.loaded, "Secure Page is not loaded"
        assert self.is_displayed(*self.login_page_ui.flash_message), "Flash message is not displayed"
        assert self.login_page_ui.LBL_LOGIN_SUCCESS in self.get_flash_message(), f"Error login {self.get_flash_message()}"
        self.click(*secure_ui.button_locator)
        assert self.login_page_ui.loaded, "Login Page is not loaded"
        assert self.is_displayed(*self.login_page_ui.flash_message)
        assert self.login_page_ui.LBL_LOGOUT_SUCESS in self.get_flash_message(), f"Error logout {self.get_flash_message()}"