"""This module will use selenium for testing with Google Chrome Navigator"""

from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time


class BrowserTests(StaticLiveServerTestCase):
    """This class will test a product research and click on legals link"""

    def setUp(self):
        """setup the webdriver with Google Chrome driver"""

        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")

    def test_search_product_and_legals(self):
        """This method will do all the actions, check comments below"""

        # go to main page
        self.driver.get("http://127.0.0.1:8000/")

        # find search bar and send value nutella, find search button and click
        search = self.driver.find_element_by_name("search")
        top_search_button = self.driver.find_element_by_id("top-search-button")
        search.send_keys("nutella")
        time.sleep(2)
        top_search_button.click()
        time.sleep(2)

        # find legals link and click
        legals = self.driver.find_element_by_link_text("Mentions légales")
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", legals)
        time.sleep(2)
