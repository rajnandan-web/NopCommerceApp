from selenium.webdriver.common.by import By


class Login:
    text_box_username_id = "Email"
    text_box_password_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    link_logout_link_text = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def SetUserName(self, Username):
        self.driver.find_element(By.ID, 'Email').clear()
        self.driver.find_element(By.ID, 'Email').send_keys(Username)

    def SetPassword(self, password):
        self.driver.find_element(By.ID, 'Password').clear()
        self.driver.find_element(By.ID, 'Password').send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log in']").click()

    def ClickLogout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()
