import pytest
from selenium.common import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:
    """
    Common methods for all login in the website
    """

    @pytest.fixture(autouse=True)
    def setup_base(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, page: str):
        """
        Methodo to naviage a specific page
        :param page: str
        :return:
        """
        self.driver.get(page)

    def find(self, by, locator) -> WebElement:
        """
        Find an element in the curren page
        :param by: (xpath, ID, CCS_locator, etc.)
        :param locator: str locator of the element to find
        :return: WebElement
        """
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def find_all(self, by, locator) -> list[WebElement]:
        """
        Find all elements with the same locator
        :param by: (xpath, ID, CCS_locator, etc.)
        :param locator: str locator of the elements to find
        :return: A list of WebElements
        """
        return self.driver.find_elements(by, locator)

    def click(self, by, locator):
        """
        Perform 'click' event on other 'WebElement'
        :param by: (xpath, ID, CCS_locator, etc.)
        :param locator: str locator of the elements to find
        :return: None
        """
        self.wait.until(EC.element_to_be_clickable((by, locator))).click()

    def get_text(self, by, locator):
        """
        Gets text of a 'WebElement'
        :param by: (xpath, ID, CCS_locator, etc.)
        :param locator: str locator of the elements to find
        :return: str
        """
        return self.wait.until(EC.visibility_of_element_located((by, locator)))

    def is_displayed(self, by, locator) -> bool:
        """
        Checks if a 'WebElement' is displayed
        :param by: (xpath, ID, CCS_locator, etc.)
        :param locator: str locator of the elements to find
        :return: bool
        """
        try:
            self.wait.until(EC.visibility_of_element_located((by, locator)))
            return True
        except (NoSuchElementException, ElementNotVisibleException):
            return False
