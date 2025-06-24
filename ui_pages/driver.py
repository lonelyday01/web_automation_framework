class BaseDriver(object):
    def __init__(self, driver):
        self._driver = driver

    @property
    def driver(self):
        if callable(self._driver):
            return self._driver()
        return self._driver
