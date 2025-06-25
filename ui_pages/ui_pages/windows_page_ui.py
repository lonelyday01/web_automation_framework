from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from web_automation_framework.ui_pages.ui_pages.base_page_ui import BasePageUi


class WindowsPageUi(BasePageUi):
    """
    Class with all visual elements of the windows page
    """
    LBL_WINDOWS_TITLE_PAGE = "Opening a new window"
    def __init__(self, driver):
        super().__init__(driver)
        self.click_here_btn = (By.CSS_SELECTOR, "div.example a[href='/windows/new']")
        self.new_window_txt = (By.CSS_SELECTOR, "div.example h3")

    @property
    def loaded(self) -> bool:
        """
        Property to verify if the windows page is loaded
        :return: boll
        """
        try:
            return self.LBL_WINDOWS_TITLE_PAGE == self.title_text
        except NoSuchElementException:
            return False
