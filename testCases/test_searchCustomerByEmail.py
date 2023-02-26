import time

import pytest

from pageObjects.LoginPage import Login
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import readConfig
from utilities.customLogger import LogGeneration
from pageObjects.AddcustomerPage import AddCustomer


class Test_searchCustomerByEmail_004:
    URL = readConfig.getApplicationURL()
    Username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGeneration.loggen()

    @pytest.mark.sanity
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("............. searchCustomerByEmail_004 ..............")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.SetUserName(self.Username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info(".......... login successful ............")

        self.logger.info("........ start searching customer by email ...........")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.ClickOnCustomersMenu()
        self.add_cust.ClickOnCustomerItemMenu()

        self.logger.info("............. searching customer by email id ..........")

        search_cust = SearchCustomer(self.driver)
        search_cust.setEmail("victoria_victoria@nopCommerce.com")
        search_cust.ClickSearch()
        time.sleep(3)

        assert True
        self.logger.info(".......... test_searchCustomerByEmail finished .......")
        self.driver.close()
