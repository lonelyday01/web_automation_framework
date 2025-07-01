import pytest

from web_automation_framework.tests.login.login2_base_test import Login2BaseTest


class TestLogin2Page(Login2BaseTest):
    """
    Class with the test cases to validate the functionality of login2 page
    """
    def test_valid_login(self):
        """
        Validate a successfully login
        """
        self.navigate_to_login2_page()
        assert self.login2_ui.loaded, "Login2 page is not loaded"

        username = self.login2_ui.CORRECT_USER
        password = self.login2_ui.CORRECT_PASSWORD
        self.insert_username(username)
        self.insert_password(password)
        actual_username = self.get_text(*self.login2_ui.username_box).get_attribute("value")
        actual_password = self.get_text(*self.login2_ui.password_box).get_attribute("value")
        assert actual_username == username, f"Expected: {username}, Actual: {actual_username}"
        assert actual_password == password, f"Expected: {password}, Acutal: {actual_password}"

        logged_in = self.click_on_submit()
        assert logged_in.loaded, "Logged in page is not loaded"
        assert self.verify_url(self.get_url())
        assert self.is_displayed(*logged_in.logged_in_message_locator)
        assert self.is_displayed(*logged_in.logout_locator)


    def test_invalid_login(self):
        """
        Validate an unsuccessfully login
        """
        self.navigate_to_login2_page()
        assert self.login2_ui.loaded, "Login2 page is not loaded"

        username = self.login2_ui.INCORRECT_USER
        password = self.login2_ui.CORRECT_PASSWORD
        self.insert_username(username)
        self.insert_password(password)
        actual_username = self.get_text(*self.login2_ui.username_box).get_attribute("value")
        actual_password = self.get_text(*self.login2_ui.password_box).get_attribute("value")
        assert actual_username == username, f"Expected: {username}, Actual: {actual_username}"
        assert actual_password == password, f"Expected: {password}, Acutal: {actual_password}"

        self.click_on_submit()
        assert self.is_displayed(*self.login2_ui.login_message), "Login message is not displayed"
        assert self.login2_ui.INVALID_USER_MSG == self.get_text(*self.login2_ui.login_message).text

        username = self.login2_ui.CORRECT_USER
        password = self.login2_ui.INCORRECT_PASSWORD
        self.insert_username(username)
        self.insert_password(password)
        actual_username = self.get_text(*self.login2_ui.username_box).get_attribute("value")
        actual_password = self.get_text(*self.login2_ui.password_box).get_attribute("value")
        assert actual_username == username, f"Expected: {username}, Actual: {actual_username}"
        assert actual_password == password, f"Expected: {password}, Acutal: {actual_password}"

        self.click_on_submit()
        assert self.is_displayed(*self.login2_ui.login_message), "Login message is not displayed"
        assert self.login2_ui.INVALID_PASSWORD_MSG == self.get_text(*self.login2_ui.login_message).text

    def test_empty_login(self):
        """
        Validate an unsuccessful login with empty data
        """
        self.navigate_to_login2_page()
        assert self.login2_ui.loaded, "Login2 page is not loaded"

        username = ""
        password = ""
        self.insert_username(username)
        self.insert_password(password)
        actual_username = self.get_text(*self.login2_ui.username_box).get_attribute("value")
        actual_password = self.get_text(*self.login2_ui.password_box).get_attribute("value")
        assert actual_username == username, f"Expected: {username}, Actual: {actual_username}"
        assert actual_password == password, f"Expected: {password}, Acutal: {actual_password}"

        self.click_on_submit()
        assert self.is_displayed(*self.login2_ui.login_message), "Login message is not displayed"
        assert self.login2_ui.INVALID_USER_MSG == self.get_text(*self.login2_ui.login_message).text

    @pytest.mark.parametrize("username, password, expected, error_msg",
                             [
                                 ("student", "Password123", "success", None),
                                 ("teacher", "Password123", "fail", "Your username is invalid!"),
                                 ("student", "password", "fail", "Your password is invalid!"),
                                 ("", "", "fail", "Your username is invalid!"),
                             ])
    def test_login_parametrized(self, username, password, expected, error_msg):
        """
        Validate different scenaries
        """
        self.navigate_to_login2_page()
        assert self.login2_ui.loaded, "Login2 page is not loaded"

        self.insert_username(username)
        self.insert_password(password)

        actual_username = self.get_text(*self.login2_ui.username_box).get_attribute("value")
        actual_password = self.get_text(*self.login2_ui.password_box).get_attribute("value")
        assert actual_username == username
        assert actual_password == password

        logged_in = self.click_on_submit()
        if expected == "success":
            assert logged_in.loaded, "Logged in page is not loaded"
            assert self.verify_url(self.get_url())
            assert self.is_displayed(*logged_in.logged_in_message_locator)
            assert self.is_displayed(*logged_in.logout_locator)
        else:
            assert self.is_displayed(*self.login2_ui.login_message), "Login message is not displayed"
            assert error_msg == self.get_text(*self.login2_ui.login_message).text