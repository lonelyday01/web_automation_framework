from web_automation_framework.tests.windows.windows_base_test import WindowsBaseTest


class TestWindowsPage(WindowsBaseTest):
    """
    Class with the test cases to validate of window page functionality
    """
    def test_single_windows(self):
        """
        Test case to verify the functionality of a single window handle
        """
        self.navigate_to_window_handle_page()
        assert self.windows_ui.loaded, "Windows page is not loaded"

        original_handle = self.get_current_window_handle()
        assert self.is_displayed(*self.windows_ui.click_here_btn)
        self.click_on_click_here()

        windows_handles = self.get_list_of_window_handle()
        assert len(windows_handles) > 1, "Only original page is opened"

        self.switch_windows(windows_handles[1])
        assert self.is_displayed(*self.windows_ui.new_window_txt)

        self.switch_windows(original_handle)
        assert self.windows_ui.loaded, "Windows page is not loaded"
