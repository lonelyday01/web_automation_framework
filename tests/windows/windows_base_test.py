import pytest

from web_automation_framework.tests.base_test import BaseTest
from web_automation_framework.ui_pages.ui_pages.windows_page_ui import WindowsPageUi


class WindowsBaseTest(BaseTest):
    """
    Class with common methods for Windows tests
    """
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.windows_ui = WindowsPageUi(driver)

    def navigate_to_window_handle_page(self):
        """
        Method to navigate to window handle page
        :return: None
        """
        self.driver.get("https://the-internet.herokuapp.com/windows")

    def click_on_click_here(self):
        """
        Method to perform click event on 'click here' button
        :return: None
        """
        self.click(*self.windows_ui.click_here_btn)

    def get_current_window_handle(self):
        """
        Method to get the current window handle
        :return: Windows instance
        """
        return self.driver.current_window_handle

    def get_list_of_window_handle(self):
        """
        Get all the current windows handle oppend
        :return: list
        """
        return self.driver.window_handles

    def switch_windows(self, handle="main"):
        """
        Method to change to specific windows handle
        :param handle: str
        :return:
        """
        self.driver.switch_to.window(handle)

