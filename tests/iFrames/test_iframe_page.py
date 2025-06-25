from web_automation_framework.tests.iFrames.iframe_base_test import IFramesPage


class TestIFramePage(IFramesPage):
    """
    Class to test iFrame page
    """

    def test_single_iframe_validation(self):
        """
        Test case to validate the functionality of a single iframe
        """
        self.navigate_to_iframe_page()
        assert self.iframe_ui.loaded, "iFrame page is not loaded"

        single_frame = self.iframe_ui.single_iframe_locator
        self.click_on_single_iframe()
        self.switch_frame(frame_locator=single_frame)
        assert self.is_displayed(*self.iframe_ui.single_textbox), "Single iframe textbox is not displayed"

        expected_text = self.iframe_ui.LBL_SIMPLE_IFRAME_TEST_TEXT
        self.enter_text_in_single_frame(text=expected_text)
        current_text = self.get_text(*self.iframe_ui.single_textbox).get_attribute("value")
        assert expected_text == current_text, \
        f"Fail: Expected text: {expected_text} is not equal to Current text: {current_text}"

        self.switch_frame("default")


    def test_multiple_iframe_validation(self):
        """
        Test case to validate the functionality of a multiple iframe
        """
        self.navigate_to_iframe_page()
        assert self.iframe_ui.loaded, "IFrame page is not loaded"

        mult_frame = self.iframe_ui.multiple_iframe_locator
        child_frame = self.iframe_ui.child_iframe_locator
        self.click_on_multiple_iframe()
        self.switch_frame(frame_locator=mult_frame)
        assert self.is_displayed(*child_frame), "Single iframe is not displayed in the current iframe"

        expected_text = self.iframe_ui.LBL_MULTIPLE_IFRAME_TEST_TEXT
        self.switch_frame(child_frame)
        assert self.is_displayed(*self.iframe_ui.single_textbox), "Single iframe textbox is not displayed"

        self.enter_text_in_single_frame(expected_text)
        current_text = self.get_text(*self.iframe_ui.single_textbox).get_attribute("value")
        assert expected_text == current_text, \
            f"Fail: Expected text: {expected_text} is not equal to Current text: {current_text}"

        self.switch_frame("default")