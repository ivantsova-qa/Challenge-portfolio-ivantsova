import datetime
from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage():

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def field_send_keys(self, selector, value, locator_type=By.XPATH):
        return self.driver.find_element(locator_type, selector).send_keys(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()

    def get_page_title(self, url):
        # self.driver.get(url)
        return self.driver.title

    def assert_element_text(self, driver, xpath, expected_text):
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element_text = element.text
        assert expected_text == element_text

    def wait_for_element_to_be_clickable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))

    def wait_for_presence_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))

    def wait_for_text_to_be_present_in_element(self, text, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))

    def wait_for_url_to_be(self, url):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.url_to_be(url))

    def wait_for_alert_is_not_present(self):
        WebDriverWait(self.driver, 8).until_not(EC.alert_is_present())

    def wait_for_visibility_of_element_located(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located((locator_type, locator)))

    def wait_for_text_to_be_present_in_element_value(self, text, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 5)
        element = wait.until(EC.text_to_be_present_in_element((locator_type, locator), text))

    def select_item_from_dropdown_list(self, locator1, locator2, locator_type=DEFAULT_LOCATOR_TYPE):
        self.driver.find_element(locator_type, locator1).click()
        self.driver.find_element(locator_type, locator2).click()

    def save_screenshot(self, name):
        now_date = datetime.datetime.utcnow().strftime('%d.%m.%Y.%H.%M.%S')
        screenshot_name = name + 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Anastasiia\\DareIT\\Git\\Challenge-portfolio-ivantsova\\screenshot\\'
                                    + screenshot_name)
