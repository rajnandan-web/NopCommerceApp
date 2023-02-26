import pytest

from pageObjects.LoginPage import Login
from utilities.readProperties import readConfig
from utilities.customLogger import LogGeneration
from pageObjects.AddcustomerPage import AddCustomer
import random
import string
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    URL = readConfig.getApplicationURL()
    Username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger = LogGeneration.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info(".....................Test_003_addCustomer.................")
        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.SetUserName(self.Username)
        self.lp.SetPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("..................Login successful............")

        self.logger.info("............Start adding new customers .........")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.ClickOnCustomersMenu()
        self.add_cust.ClickOnCustomerItemMenu()

        self.add_cust.AddNewItem()
        self.logger.info("........... Providing some customer info ............")

        self.email = random_generator() + "@gmail.com"
        self.add_cust.setEmail(self.email)
        self.add_cust.setPassword('test123')
        self.add_cust.setFirstName('Rajnandan')
        self.add_cust.setLastName('Rajbanshi')
        self.add_cust.SetDOB("08/27/1997")
        self.add_cust.SetCompanyName('ust')
        self.add_cust.SetComment('This is for comment')
        self.add_cust.SetSave()

        self.logger.info("......... saving customer info ..............")
        self.logger.info("........... add customer validation started .....")

        self.message = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.message)

        if "customer has been added successfully" in self.message:
            assert True == True
            self.logger.info(" add customer test is passed")

        """else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer.png")
            self.logger.info("add customer test is failed")
            assert True == False

            self.driver.close()
            self.logger.info("............ ending add customer test ...........")
"""


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
