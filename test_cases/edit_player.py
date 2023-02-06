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


class TestEditPlayers(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_edit_player_after_filtering(self):
        TestLoginPage.test_log_in_to_the_system(self)

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_players_button()

        players_page = PlayersPage(self.driver)
        players_page.click_filter_button()
        players_page.type_in_name_field('TestName')
        players_page.type_in_surname_field('TestSurname')
        players_page.type_in_main_position_field('TestMainPosition')
        players_page.click_close_filter_button()
        time.sleep(2)
        # players_page.save_screenshot('EP_001(01)')
        players_page.click_on_the_players('TestName', 'TestSurname', 'TestMainPosition')
        time.sleep(1)

        change_player = AddPlayer(self.driver)
        change_player.type_in_email('testemail@gmail.com')
        change_player.type_in_phone('+4878000000')
        change_player.type_in_weight('75')
        change_player.type_in_height('175')
        change_player.select_right_leg_dropdown_list()
        change_player.type_in_club('TestClub')
        change_player.type_in_level('TestLevel')
        change_player.type_in_second_position('TestSecondPosition')
        change_player.select_district_dropdown_list()
        change_player.type_in_achievements('TestAchievements')
        change_player.type_in_laczy('Test')
        change_player.type_in_nineteen_minute('TestTime')
        change_player.type_in_facebook('https://fecebook.com')
        change_player.click_submit_button()
        change_player.check_success_saved_player()
        # change_player.save_screenshot('EP_001(02)')




