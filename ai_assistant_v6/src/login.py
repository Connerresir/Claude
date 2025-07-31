from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from .credentials import Credentials

class Login:
    def __init__(self):
        self.credentials = Credentials()

    def login(self, service_name, username, login_url, username_field_id, password_field_id, submit_button_id):
        password = self.credentials.get_credential(service_name, username)
        if not password:
            print(f"No password found for {username} on {service_name}")
            return None

        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get(login_url)
            driver.find_element(By.ID, username_field_id).send_keys(username)
            driver.find_element(By.ID, password_field_id).send_keys(password)
            driver.find_element(By.ID, submit_button_id).click()
            print(f"Successfully logged in to {service_name} as {username}")
            return driver
        except Exception as e:
            print(f"Error logging in to {service_name}: {e}")
            return None
