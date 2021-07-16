# from selenium import webdriver
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# import random
# import string
# import time

# class BrowserTests(StaticLiveServerTestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        
#     def test_login_logout_signin(self):
#         letters = string.ascii_lowercase
#         stringmail = (''.join(random.choice(letters) for i in range(10)))

#         self.driver.get("http://127.0.0.1:8000/")

#         sign_in = self.driver.find_element_by_link_text("S'inscrire")
#         self.driver.execute_script("arguments[0].click();", sign_in)
#         time.sleep(2)

#         self.driver.find_element_by_name("email").send_keys(stringmail+"@test.com")
#         self.driver.find_element_by_name("username").send_keys(stringmail)
#         self.driver.find_element_by_name("password1").send_keys("Def741852")
#         self.driver.find_element_by_name("password2").send_keys("Def741852")
#         time.sleep(2)

#         self.driver.find_element_by_id("registration_button").click()
#         time.sleep(2)

#         self.assertIn("http://127.0.0.1:8000/authentication/login/", self.driver.current_url)

#         log_out = self.driver.find_element_by_link_text("Se déconnecter")
#         self.driver.execute_script("arguments[0].click();", log_out)
#         time.sleep(2)

#         log_in = self.driver.find_element_by_link_text("Se connecter")
#         self.driver.execute_script("arguments[0].click();", log_in)
#         time.sleep(2)

#         self.driver.find_element_by_name(
#             "email").send_keys(stringmail+"@test.com")
#         self.driver.find_element_by_name("password").send_keys("Def741852")
#         time.sleep(2)

#         self.driver.find_element_by_id("login_button").click()
#         time.sleep(2)
        
#         self.assertIn("http://127.0.0.1:8000/authentication/login/",
#                       self.driver.current_url)
