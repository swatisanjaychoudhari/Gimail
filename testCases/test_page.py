import pytest
from utilites.readproperties import Readconfig


class Test_page:
    url = Readconfig.geturl()

    def test_page_001(self, setup):
        self.driver = setup()
        self.driver.get(self.url)


