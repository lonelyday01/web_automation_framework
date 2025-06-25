from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from web_automation_framework.ui_pages.ui_pages.base_page_ui import BasePageUi


class IFramesPageUI(BasePageUi):
    """
    Class for iframes page
    """
    LBL_IFRAME_TITLE_PAGE = "Automation Demo Site"
    LBL_SIMPLE_IFRAME_TEST_TEXT = "Iframe simple"
    LBL_MULTIPLE_IFRAME_TEST_TEXT = "Iframe anidado"

    def __init__(self, driver):
        super().__init__(driver)
        self.title_locator = (By.XPATH, "//div[@class='container']//*[starts-with(name(), 'h')]")
        self.single_iframe_btn_locator = (By.CSS_SELECTOR, "a[href='#Single'].analystic")
        self.multiple_iframe_btn_locator = (By.CSS_SELECTOR, "a[href='#Multiple'].analystic")
        self.single_iframe_locator = (By.CSS_SELECTOR, "iframe#singleframe")
        self.multiple_iframe_locator = (By.CSS_SELECTOR, "iframe[src='MultipleFrames.html']")
        self.child_iframe_locator = (By.CSS_SELECTOR, ".iframe-container iframe[src='SingleFrame.html']")
        self.single_textbox = (By.CSS_SELECTOR, "div.container input[type='text']")


    @property
    def loaded(self):
        try:
            return self.LBL_IFRAME_TITLE_PAGE == self.title_text
        except NoSuchElementException:
            return False

    @property
    def title_text(self):
        try:
            title = self.wait.until(EC.visibility_of_element_located(self.title_locator)).text.strip()
            return title
        except (NoSuchElementException, ElementNotVisibleException):
            return None