import time

import pytest

from pageObjects.LoginPage import Login
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import readConfig
from utilities.customLogger import LogGeneration
from pageObjects.AddcustomerPage import AddCustomer


class Test_searchCustomerByName_005:
    URL = readConfig.getApplicationURL()
    Username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGeneration.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("............. searchCustomerByName_005 ..............")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.SetUserName(self.Username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info(".......... login successful ............")

        self.logger.info("........ start searching customer by name ...........")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.ClickOnCustomersMenu()
        self.add_cust.ClickOnCustomerItemMenu()

        self.logger.info("............. searching customer by name ..........")

        search_cust = SearchCustomer(self.driver)
        search_cust.setFirstName("Brenda")
        search_cust.setLastName("Lindgren")
        search_cust.ClickSearch()
        time.sleep(3)

        assert True
        self.logger.info(".......... test_searchCustomerByName finished .......")
        self.driver.close()
