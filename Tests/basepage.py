import self
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class basepage:
    def __int__(self, driver):
        self.driver = driver

    def do_click(self, bylocator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(bylocator)).click()

