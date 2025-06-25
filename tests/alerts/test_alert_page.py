from web_automation_framework.tests.alerts.alert_base_test import AlertBaseTest


class TestAlertPage(AlertBaseTest):
    """
    Class to test alert page
    """
    def test_basic_alert_validation(self):
        """
        Test case to validate the funcionality of basic alert
        """
        self.navigate_to_alert_page()
        assert self.alert_ui.loaded, "Alert Page is not loaded"

        self.click_on_basic_alert()
        self.click_on_alert_item(alert_type="alert")
        assert self.get_result_text() == self.alert_ui.LBL_BASIC_ALERT_RESULT

    def test_confirm_alert_validation(self):
        """
        Test case to validate the functionality of confirm alert
        """
        self.navigate_to_alert_page()
        assert self.alert_ui.loaded, "Alert Page is not loaded"

        self.click_on_confirm_alert()
        self.click_on_alert_item(alert_type="confirm")
        assert self.get_result_text() == self.alert_ui.LBL_CONFIRM_ALERT_RESULT

        self.click_on_confirm_alert()
        self.click_on_alert_item(alert_type="confirm", accept=False)
        assert self.get_result_text() == self.alert_ui.LBL_CANCEL_ALERT_RESULT

    def test_propt_alert_validation(self):
        """
        Test case to validate the functionality of prompt alert
        """
        self.navigate_to_alert_page()
        assert self.alert_ui.loaded, "Alert Page is not loaded"

        self.click_on_prompt_alert()
        self.click_on_alert_item(alert_type="prompt")
        assert self.get_result_text() == self.alert_ui.LBL_PROMPT_ALERT_EMPTY_RESULT

        self.click_on_prompt_alert()
        self.click_on_alert_item(alert_type="prompt", prompt=self.alert_ui.LBL_PROMPT_ALERT_SEND_TEXT)
        assert self.get_result_text() == self.alert_ui.LBL_PROMPT_ALERT_TEXT_RESULT

        self.click_on_prompt_alert()
        self.click_on_alert_item(alert_type="prompt", accept=False, prompt=self.alert_ui.LBL_PROMPT_ALERT_SEND_TEXT)
        assert self.get_result_text() == self.alert_ui.LBL_PROMPT_ALERT_CANCEL_RESULT
