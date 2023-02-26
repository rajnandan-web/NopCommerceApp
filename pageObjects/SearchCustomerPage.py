from selenium.webdriver.common.by import By


class SearchCustomer:
    # add customer page

    text_email_id = "SearchEmail"
    text_firstname_id = "SearchFirstName"
    text_lastname_id = "SearchLastName"
    search_button_id = "search-customers"

    table_xpath = "//div[@id='customers-grid_wrapper']"
    table_row_xpath = "//div[@id='customers-grid_wrapper']//tbody/tr"
    table_column_xpath = "//div[@id='customers-grid_wrapper']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element(By.ID, "SearchEmail").clear()
        self.driver.find_element(By.ID, "SearchEmail").send_keys(email)

    def setFirstName(self, firstname):
        self.driver.find_element(By.ID, "SearchFirstName").clear()
        self.driver.find_element(By.ID, "SearchFirstName").send_keys(firstname)

    def setLastName(self, lastname):
        self.driver.find_element(By.ID, "SearchLastName").clear()
        self.driver.find_element(By.ID, "SearchLastName").send_keys(lastname)

    def ClickSearch(self):
        self.driver.find_element(By.ID, "search-customers").click()

    def GetNOofRows(self):
        return len(self.driver.find_element(By.XPATH, self.table_row_xpath))

    def GetNOofColumn(self):
        return len(self.driver.find_element(By.XPATH, self.table_column_xpath))

    def SearchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.GetNOofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            email_id = table.find_element(By.XPATH,
                                          "//div[@id='customers-grid_wrapper']//tbody/tr[" + str(r) + "]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def SearchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.GetNOofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH,
                                      "//div[@id='customers-grid_wrapper']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
