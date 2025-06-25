import time

import pytest
from web_automation_framework.tests.base_test import BaseTest
from web_automation_framework.ui_pages.ui_pages.java_script_page_ui import JavaScriptPageUi


class AlertType:
    ALERT = "alert"
    CONFIRM = "confirm"
    PROMPT = "prompt"


class AlertBaseTest(BaseTest):
    """
    Class for Alert page
    """
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.alert_ui = JavaScriptPageUi(driver)

    def navigate_to_alert_page(self) -> None:
        """
        Method to navigate to alert page
        :return: None
        """
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    def click_on_basic_alert(self):
        """
        Method to find and click on the basic alert button
        :return: None
        """
        self.click(*self.alert_ui.js_basic_alert)

    def click_on_confirm_alert(self):
        """
         Method to find and click on the confirm alert button
        :return: None
        """
        self.click(*self.alert_ui.js_confirm_alert)

    def click_on_prompt_alert(self):
        """
        Method to find and click on the prompt alert button
        :return: None
        """
        self.click(*self.alert_ui.js_promp_alert)

    def click_on_alert_item(self, alert_type=AlertType().ALERT, accept=True, prompt=""):
        """
        Method to interact with the alert displayed
        :return: None
        """
        alert = self.driver.switch_to.alert
        if alert_type == AlertType().ALERT:
            alert.accept()
        elif alert_type == AlertType().CONFIRM:
            if accept:
                alert.accept()
            else:
                alert.dismiss()
        elif alert_type == AlertType().PROMPT:
            alert.send_keys(prompt)
            if accept:
                alert.accept()
            else:
                alert.dismiss()

    def get_result_text(self):
        """
        Method to get the result after interact with an alert
        :return: str
        """
        return self.find(*self.alert_ui.result_locator).text