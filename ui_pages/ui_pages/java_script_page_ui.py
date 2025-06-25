from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from web_automation_framework.ui_pages.ui_pages.base_page_ui import BasePageUi


class JavaScriptPageUi(BasePageUi):
    """
    Class for JavaScript page
    """
    LBL_JAVASCRIPT_PAGE_TITLE = "JavaScript Alerts"
    LBL_BASIC_ALERT_RESULT = "You successfully clicked an alert"
    LBL_CONFIRM_ALERT_RESULT = "You clicked: Ok"
    LBL_CANCEL_ALERT_RESULT = "You clicked: Cancel"
    LBL_PROMPT_ALERT_EMPTY_RESULT = "You entered:"
    LBL_PROMPT_ALERT_CANCEL_RESULT = "You entered: null"
    LBL_PROMPT_ALERT_SEND_TEXT = "Inserting text in propt alert 123@asd"
    LBL_PROMPT_ALERT_TEXT_RESULT = f"You entered: {LBL_PROMPT_ALERT_SEND_TEXT}"



    def __init__(self, driver):
        self.result_locator = (By.ID, "result")
        self.js_basic_alert = (By.CSS_SELECTOR, "button[onclick='jsAlert()']")
        self.js_confirm_alert = (By.CSS_SELECTOR, "button[onclick='jsConfirm()']")
        self.js_promp_alert = (By.CSS_SELECTOR, "button[onclick='jsPrompt()']")
        super().__init__(driver)

    @property
    def loaded(self):
        try:
            return self.LBL_JAVASCRIPT_PAGE_TITLE == self.title_text
        except NoSuchElementException:
            return False
