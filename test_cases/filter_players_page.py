import os
import time
import unittest

from selenium import webdriver

from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.players_page import PlayersPage
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestFilterPlayers(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_filter_players_by_name(self):
        TestLoginPage.test_log_in_to_the_system(self)

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_players_button()

        players_page = PlayersPage(self.driver)
        players_page.click_filter_button()
        players_page.type_in_name_field('testname')
        players_page.click_close_filter_button()
        time.sleep(2)
        players_page.check_text_to_be_present_in_element('testname')
        # players_page.save_screenshot('FP_001')

