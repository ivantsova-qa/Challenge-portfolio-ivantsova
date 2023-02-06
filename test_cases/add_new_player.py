import os
import time
import unittest

from selenium import webdriver

from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddPlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        super(TestAddPlayer, self).setUp(self)

    def test_add_new_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        time.sleep(3)

        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_text_to_be_present_in_element()
        dashboard_page.check_visibility_of_element_located()
        dashboard_page.click_add_player_link()

        add_player_page = AddPlayer(self.driver)
        add_player_page.check_url_to_be()
        add_player_page.title_of_page()
        add_player_page.check_alert_is_not_present()
        add_player_page.type_in_name('TestName')
        time.sleep(0.5)
        add_player_page.type_in_surname('TestSurname')
        time.sleep(0.5)
        add_player_page.type_in_age('01012000')
        time.sleep(0.5)
        add_player_page.type_in_main_position('MainPlayer')
        add_player_page.click_submit_button()
        time.sleep(1)
        # add_player_page.save_screenshot('AP_001')

    def test_add_new_player_with_empty_fields(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_url_to_be()
        dashboard_page.click_add_player_link()

        add_player_page = AddPlayer(self.driver)
        add_player_page.check_text_to_be_present_in_element_value()
        add_player_page.click_submit_button()
        time.sleep(1)
        # add_player_page.save_screenshot('AP_002')

    def test_clear_fields(self):
        TestLoginPage.test_log_in_to_the_system(self)
        # user_login = LoginPage(self.driver)
        # user_login.type_in_email('user01@getnada.com')
        # user_login.type_in_password('Test-1234')
        # user_login.click_sign_in_button()

        dashboard_page = Dashboard(self.driver)
        dashboard_page.check_url_to_be()
        dashboard_page.click_add_player_link()

        add_player_page = AddPlayer(self.driver)
        add_player_page.type_in_email('testemail@gmail.com')
        add_player_page.type_in_name('TestName')
        add_player_page.type_in_surname('TestSurname')
        add_player_page.type_in_phone('+4878000000')
        add_player_page.type_in_weight('75')
        add_player_page.type_in_height('175')
        add_player_page.type_in_age('01012000')
        add_player_page.select_right_leg_dropdown_list()
        add_player_page.type_in_club('TestClub')
        add_player_page.type_in_level('TestLevel')
        add_player_page.type_in_main_position('TestMainPosition')
        add_player_page.type_in_second_position('TestSecondPosition')
        add_player_page.select_district_dropdown_list()
        add_player_page.type_in_achievements('TestAchievements')
        add_player_page.type_in_laczy('Test')
        add_player_page.type_in_nineteen_minute('TestTime')
        add_player_page.type_in_facebook('https://fecebook.com')
        # add_player_page.save_screenshot('AP_003(01)')
        add_player_page.click_clear_button()
        add_player_page.check_empty_filed()
        time.sleep(3)
        # add_player_page.save_screenshot('AP_003(02)')

    def test_template_add_new_player(self, test_name, test_surname, test_age, test_main_player):

        add_player_page = AddPlayer(self.driver)
        add_player_page.check_url_to_be()
        add_player_page.title_of_page()
        add_player_page.check_alert_is_not_present()
        add_player_page.type_in_name(test_name)
        add_player_page.type_in_surname(test_surname)
        add_player_page.type_in_age(test_age)
        add_player_page.type_in_main_position(test_main_player)
        add_player_page.click_submit_button()
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.quit()
