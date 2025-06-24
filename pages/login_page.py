from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from web_automation_framework.pages.base_page import BasePage
from ..ui_pages.activities.login_page_activity import LoginPageActivity


class LoginPage(BasePage):
    """
    Class for login page
    """
    def __init__(self, driver):
        """
        LoginPage constructor
        """
        super().__init__(driver)

    def navigate_login_page(self) -> LoginPageActivity:
        """
        Method to navigate login screen
        :return: None
        """
        self.driver.get("https://the-internet.herokuapp.com/login")
        return LoginPageActivity(driver=self.driver)

    def set_username(self, username) -> None:
        """
        Method to find the username box and set the username
        :param username: str
        :return: None
        """
        self.driver.find_element(By.ID, "username").send_keys(username)

    def set_password(self, password) -> None:
        """
        Method to find the password box and set the password
        :param password: str
        :return: None
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self)  -> None:
        """
        Method to find and click in login button
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def get_flash_message(self) -> str:
        """
        Method to find and get the flash message displayed after click on login button
        :return: str with the text of flash message
        """
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='flash'].flash"))).text
