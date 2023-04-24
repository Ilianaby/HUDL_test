from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import selenium.common.exceptions



class LoginPage:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_login_page(self):
        self.driver.get("https://www.hudl.com/")
        try:
            self.login_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@data-qa-id='login-hudl']")))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def click(self, element):
        # Click the link using JavaScript executor
        self.driver.execute_script("arguments[0].click();", element)

    def submit_creds(self, email, password):
        self.driver.find_element(By.ID, "email").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.login_button = self.driver.find_element(By.ID, "logIn")

        if not self.login_button.is_enabled():
            raise Exception("logIn button is unavailable")

        self.login_button.click()

    def is_login_successful(self):
        try:
            self.wait.until(EC.staleness_of(self.login_button))
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-qa-id='webnav-usermenu-logout']")))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def check_not_logged_in(self):
        self.driver.get("https://www.hudl.com/home")
        assert self.driver.current_url != "https://www.hudl.com/home", "Logout failed"

    def check_element_by_id(self, element_id):
        try:
            self.wait.until(EC.presence_of_element_located((By.ID, element_id)))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def get_error_message(self):
        assert self.login_button.is_displayed(), "logIn button is available"
        try:
            self.wait.until(EC.text_to_be_present_in_element((By.XPATH, "//p[@data-qa-id='error-display']"),
                                                             "We didn't recognize that email and/or password."))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def find_logout(self):
        self.logout_link = self.driver.find_element(By.XPATH, "//a[@data-qa-id='webnav-usermenu-logout']")

    def click_logout(self):
        try:
            self.click(self.logout_link)
            self.wait.until(EC.staleness_of(self.logout_link))
            return True
        except selenium.common.exceptions.TimeoutException:
            return False

    def close_session(self):
        self.driver.quit()
