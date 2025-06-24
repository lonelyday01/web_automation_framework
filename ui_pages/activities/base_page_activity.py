from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from web_automation_framework.ui_pages.driver import BaseDriver
from selenium.webdriver.support import expected_conditions as EC



class BasePageActivity(BaseDriver):
    """
    Base page activity
    """
    def __init__(self, driver, timeout = 10):
        self.timeout = timeout
        super().__init__(driver)

    @property
    def loaded(self):
        """
        Use to check if the page is loaded
        must be implemented in all pages
        """
        raise NotImplementedError(f"'loaded' property is not implemented in {self.__class__}")

    @property
    def wait(self) -> WebDriverWait:
        """
        :return: WebDriverWait property
        """
        return WebDriverWait(driver=self.driver, timeout=self.timeout)

    @property
    def title_text(self):
        """
        Gets the title text of the current page
        :return: str or None
        """
        locator = (
            By.XPATH, f"//div[@class='example']//*[starts-with(name(), 'h') and normalize-space(text()) != '']"
        )
        try:
            title = self.wait.until(EC.visibility_of_element_located(locator)).text.strip()
            return title
        except (NoSuchElementException, ElementNotVisibleException):
            print("Title does not exist in the current page")
            return None
