# test check
# new ch
import time

import self
from selenium.webdriver.common.keys import Keys
import allure
import allure_pytest
import outcome
import pytest
from selenium import webdriver
from allure_commons.types import AttachmentType
import logging
from selenium.webdriver.common.by import By

import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="class")
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(self.driver.get_scerenshot_as_png(), 'Failed_Testcases', attachmenttype=AttachmentType.PNG)


@pytest.fixture(scope="class")
def setup_teardown(request):
    global driver
    # op = webdriver.ChromeOptions()
    # op.add_experimental_option("detach", True)
    # driver = webdriver.Remote(options=op, command_executor="http://192.168.43.173:4444/wd/hub")
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield

    driver.quit()


class Testcheckdemo:
    def __int__(self, driver):
        self.driver = driver

    @pytest.mark.smoke
    @pytest.mark.usefixtures("log_on_failure", "setup_teardown")
    def test_title(self):
        logging.info("Opening website")

        self.driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
        self.driver.maximize_window()
        # driver.send_keys(Keys.F5)
        a = self.driver.find_element(By.XPATH, '//input[@name="picture"]')
        # time.sleep(10)
        # a.send_keys(Keys.F5)
        a.send_keys("C:\\Users\\Vishal\\Desktop\\test.png")
        time.sleep(10)

    @pytest.mark.smoke
    @pytest.mark.usefixtures("log_on_failure", "setup_teardown")
    def test_title1(self):
        logging.info("Opening website")
        self.driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
        self.driver.maximize_window()
        a = self.driver.find_element(By.XPATH, '//input[@name="picture"]')
        t = self.driver.title
        assert t == 'vishal'
    #
    #
    # @pytest.mark.smoke
    # def test_title2(setup_teardown):
    #     logging.info("Opening website")
    #     driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
    #     driver.maximize_window()
    #     a = driver.find_element(By.XPATH, '//input[@name="picture"]')
    #     t = driver.title
    #     assert t == 'vishal'
