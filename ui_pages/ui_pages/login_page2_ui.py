from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from web_automation_framework.ui_pages.ui_pages.base_page_ui import BasePageUi
from selenium.webdriver.common.by import By


class LoginPage2Ui(BasePageUi):
    """
    Class with all items in login page 2
    """
    LBL_TEST_LOGIN_PAGE_HEADER = "Test login"
    CORRECT_PASSWORD = "Password123"
    CORRECT_USER = "student"
    INCORRECT_PASSWORD = "password"
    INCORRECT_USER = "teacher"
    INVALID_USER_MSG = "Your username is invalid!"
    INVALID_PASSWORD_MSG = "Your password is invalid!"

    def __init__(self, driver):
        super().__init__(driver)
        self.username_box = (By.CSS_SELECTOR, "input#username[type='text']")
        self.password_box = (By.CSS_SELECTOR, "input#password[type='password']")
        self.title_locator = (By.CSS_SELECTOR, "header.site-header#site-header")
        self.header_locator = (By.CSS_SELECTOR, "section[id='login'] h2")
        self.login_message = (By.CSS_SELECTOR, "div#error.show")
        self.submit_btn = (By.ID, "submit")

    @property
    def loaded(self):
        try:
            return self.LBL_TEST_LOGIN_PAGE_HEADER == self.title_text
        except NoSuchElementException:
            return False

    @property
    def title_text(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.header_locator)).text
        except (NoSuchElementException, ElementNotVisibleException):
            return None