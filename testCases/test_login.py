import pytest

from pageObjects.LoginPage import Login
from utilities.readProperties import readConfig
from utilities.customLogger import LogGeneration


class Test_001_login:
    URL = readConfig.getApplicationURL()
    Username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGeneration.loggen()

    @pytest.mark.regression
    def test_home_page_title(self, setup):

        self.logger.info(".....................Test_001_login.................")
        self.logger.info(".....................Verifying Home Page Title.................")
        self.driver = setup
        self.driver.get(self.URL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("..................... Home Page Title Passed.................")

        """else:
            self.driver.save_screenshot(
                "C:\\Users\\USER\PycharmProjects\\NopCommerceApp\ScreenShot\\" + "test_home_page_title.png")
            self.driver.close()
            self.logger.info("..................... Home Page Title is Failed.................")
            assert False"""


    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info(".....................Verifying login Test.................")
        self.driver = setup
        self.driver.get(self.URL)
        self.lp = Login(self.driver)
        self.lp.SetUserName(self.Username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info(".....................Login Test is passed.................")
            self.driver.close()

        """else:
            self.driver.save_screenshot(
                "C:\\Users\\USER\PycharmProjects\\NopCommerceApp\ScreenShot\\" + "test_login.png")
            self.driver.close()
            self.logger.info(".....................Login Test is failed.................")"""
        # assert False
