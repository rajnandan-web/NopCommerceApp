import time

import pytest

from pageObjects.LoginPage import Login
from utilities.readProperties import readConfig
from utilities.customLogger import LogGeneration
from utilities import XLUtis


class Test_002_DDT_login:
    URL = readConfig.getApplicationURL()
    path = ".\\TestData\\test_login.xlsx"
    logger = LogGeneration.loggen()

    @pytest.mark.sanity
    def test_login_ddt(self, setup):
        self.logger.info("...............Test_002_DDT_login.....................")
        self.logger.info(".....................Verifying login DDT Test.................")
        self.driver = setup
        self.driver.get(self.URL)

        self.lp = Login(self.driver)

        self.row = XLUtis.getRowCount(self.path, 'Sheet1')
        print("number of rows in Excel : ", self.row)

        list_status = []

        for r in range(2, self.row + 1):
            self.user = XLUtis.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtis.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtis.readData(self.path, 'Sheet1', r, 3)

            self.lp.SetUserName(self.user)
            self.lp.SetPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if exp_title == act_title:
                if self.exp == 'pass':
                    self.logger.info("************* passed ************")
                    self.lp.ClickLogout()
                    list_status.append("pass")

                elif self.exp == 'fail':
                    self.logger.info("******** failed **********")
                    self.lp.ClickLogout()
                    list_status.append("fail")

            elif act_title != exp_title:

                if self.exp == 'pass':
                    self.logger.info("*********** failed *****************")
                    list_status.append("fail")

                elif self.exp == 'fail':
                    self.logger.info("*********** passed *********")
                    list_status.append("pass")

        if "fail" not in list_status:

            self.logger.info("login ddt test is passed ....")
            self.driver.close()
            assert True

        else:

            self.logger.info("login ddt test is failed ...")
            self.driver.close()
            assert False

        self.logger.info("********* end of login ddt test ************")
        self.logger.info("************ completed Test_002_DDT_login ***** ")
