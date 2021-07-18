"""This module will use selenium for testing with Google Chrome Navigator"""

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import random
import string
import time


class BrowserTests(StaticLiveServerTestCase):
    """This class will test a registering, logout and login an user"""

    def setUp(self):
        """setup the webdriver with Google Chrome driver"""

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def test_login_logout_signin(self):
        """This method will do all the actions, check comments below"""

        # create a random string of 10 letters used for generate an random
        # email
        letters = string.ascii_lowercase
        stringmail = (''.join(random.choice(letters) for i in range(10)))

        # go to main page
        self.driver.get("http://127.0.0.1:8000/")

        # click on the registration page
        sign_in = self.driver.find_element_by_link_text("S'inscrire")
        self.driver.execute_script("arguments[0].click();", sign_in)
        time.sleep(2)

        # feel the form fields and click on registration
        self.driver.find_element_by_name(
            "email").send_keys(stringmail+"@test.com")
        self.driver.find_element_by_name("username").send_keys(stringmail)
        self.driver.find_element_by_name("password1").send_keys("Def741852")
        self.driver.find_element_by_name("password2").send_keys("Def741852")
        time.sleep(2)
        self.driver.find_element_by_id("registration_button").click()
        time.sleep(2)
        self.assertIn("http://127.0.0.1:8000/authentication/login/",
                      self.driver.current_url)

        # click on logout
        log_out = self.driver.find_element_by_link_text("Se déconnecter")
        self.driver.execute_script("arguments[0].click();", log_out)
        time.sleep(2)

        # click on login
        log_in = self.driver.find_element_by_link_text("Se connecter")
        self.driver.execute_script("arguments[0].click();", log_in)
        time.sleep(2)

        # feel the form fields with previous data for check login
        self.driver.find_element_by_name(
            "email").send_keys(stringmail+"@test.com")
        self.driver.find_element_by_name("password").send_keys("Def741852")
        time.sleep(2)
        self.driver.find_element_by_id("login_button").click()
        time.sleep(2)
        self.assertIn("http://127.0.0.1:8000/authentication/login/",
                      self.driver.current_url)
