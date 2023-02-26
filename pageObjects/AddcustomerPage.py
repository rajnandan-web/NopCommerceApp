from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By


class AddCustomer:
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_menu_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    button_add_new_item_xpath = "//a[normalize-space()='Add new']"
    text_email_xpath = "//input[@id='Email']"
    text_password_xpath = "//input[@id='Password']"
    text_firstname_xpath = "//input[@id='FirstName']"
    text_lastname_xpath = "//input[@id='LastName']"
    radio_button_male_id = "Gender_Male"
    radio_button_female_id = "Gender_Female"
    date_of_birth_xpath = "//input[@id='DateOfBirth']"
    company_name_xpath = "//input[@id='Company']"
    customer_role_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    list_item_administrations_xpath = "//li[contains(text(),'Administrations')]"
    list_item_guests_xpath = "//li[contains(text(),'Guests')]"
    list_item_vendors_xpath = "//li[contains(text(),'Vendors')]"
    list_item_registers_xpath = "//li[contains(text(),'Registered')]"
    drop_down_manager_of_vendors = "//select[@id='VendorId']"
    text_admin_comment_xpath = "//textarea[@id='AdminComment']"
    button_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.list_item = None
        self.driver = driver

    def ClickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,"//a[@href='#']//p[contains(text(),'Customers')]").click()

    def ClickOnCustomerItemMenu(self):
        self.driver.find_element(By.XPATH,"//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()

    def AddNewItem(self):
        self.driver.find_element(By.XPATH,"//a[normalize-space()='Add new']").click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys(email)
        
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,"//input[@id='Password']").send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,"//input[@id='LastName']").send_keys(lastname)

    def SetDOB(self,dob):
        self.driver.find_element(By.XPATH,"//input[@id='DateOfBirth']").send_keys(dob)

    def SetCompanyName(self,CompanyName):
        self.driver.find_element(By.XPATH,"//input[@id='Company']").send_keys(CompanyName)

    def SetComment(self,comment):
        self.driver.find_element(By.XPATH, "//textarea[@id='AdminComment']").send_keys(comment)

    def SetCustomerRole(self, role):
        self.driver.find_element(By.XPATH,"//div[@class='input-group-append input-group-required']//div["
                                          "@role='listbox']").click() 
        time.sleep(3)
        if role == "Registered":
            self.list_item = self.driver.find_element(By.XPATH,"//li[contains(text(),'Registered')]")

        elif role == "Administrators":
            self.list_item = self.driver.find_element(By.XPATH,"//li[contains(text(),'Administrations')]")
        # here user can be 'registered' or 'guest' only one
        elif role == "Guests":
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//li[contains(text(),'Guests')//span[@title='delete']]").click()
            self.list_item = self.driver.find_element(By.XPATH,"//li[contains(text(),'Guests')]")

        elif role == "Registered":
            self.list_item = self.driver.find_element(By.XPATH,"//li[contains(text(),'Registered')]")

        elif role == "Vendors":
            self.list_item = self.driver.find_element(By.XPATH,"//li[contains(text(),'Vendors')]")

        else:
            self.list_item = self.driver.find_element(By.XPATH,"//li[contains(text(),'Guests')]")
        time.sleep(3)
        self.driver.execute_script("arguments[0].click;", self.list_item)

    def ManagerOfVendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, "//select[@id='VendorId']"))
        drp.select_by_visible_text(value)

    def SetGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.XPATH,"Gender_Male").click()

        elif gender == "Female":
            self.driver.find_element(By.XPATH,"Gender_Female").click()

        else:
            self.driver.find_element(By.XPATH,"Gender_Male").click()

    def SetSave(self):
        self.driver.find_element(By.XPATH,"//button[@name='save']").click()
