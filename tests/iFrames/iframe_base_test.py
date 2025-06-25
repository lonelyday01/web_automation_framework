import pytest
from selenium.webdriver.common.by import By
from web_automation_framework.tests.base_test import BaseTest
from web_automation_framework.ui_pages.ui_pages.iframes_page_ui import IFramesPageUI


class IFramesPage(BaseTest):
    """
    Class with common methods for iFrames
    """
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.iframe_ui = IFramesPageUI(driver)

    def navigate_to_iframe_page(self):
        """
        Method to navigate to iframe page
        :return: None
        """
        self.driver.get("https://demo.automationtesting.in/Frames.html")

    def click_on_single_iframe(self):
        """
        Method to click on single iframe button
        :return: None
        """
        self.click(*self.iframe_ui.single_iframe_btn_locator)

    def click_on_multiple_iframe(self):
        """
        Method to click on multiple iframe button
        :return: None
        """
        self.click(*self.iframe_ui.multiple_iframe_btn_locator)

    def enter_text_in_single_frame(self, text):
        """
        Method to insert text in a textbox inside an iframe
        :param text: str
        :return: None
        """
        self.find(*self.iframe_ui.single_textbox).send_keys(text)

    def enter_text_in_nested_frame(self, text):
        """

        :param text:
        :return:
        """
        self.find(*self.iframe_ui.single_textbox).send_keys(text)

    def switch_frame(self, frame_locator):
        """
        Method to change a specific frame
        :param frame_locator: str
        :return: None
        """
        if frame_locator == "default":
            self.driver.switch_to.default_content()
        else:
            iframe = self.find(*frame_locator)
            self.driver.switch_to.frame(iframe)