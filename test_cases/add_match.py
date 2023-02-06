import os
import time
import unittest

from selenium import webdriver

from pages.add_a_player import AddPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from pages.match_form import MatchForm
from pages.players_page import PlayersPage
from test_cases.add_new_player import TestAddPlayer
from test_cases.login_to_the_system import TestLoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddMatch(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)
        super(TestAddMatch, self).setUp(self)

    def test_template_add_new_match(self):
        match_page = MatchForm(self.driver)
        match_page.type_in_my_team('TestMyTeam')
        match_page.type_in_enemy_team('TestEnemyTeam')
        match_page.type_in_my_team_score('5')
        match_page.type_in_enemy_team_score('1')
        match_page.type_in_date('02022022')
        match_page.click_match_at_home_radiobutton()
        match_page.type_in_t_short_color_field('green')
        match_page.type_in_league_field('TestLeague')
        match_page.type_in_time_played_field('90')
        match_page.type_in_number_field('3')
        match_page.type_in_web_match_field('TestWeb')
        match_page.type_in_general_field('TestGeneral')
        match_page.type_in_rating_field('5')
        match_page.click_submit_button()
        time.sleep(3)

    def test_add_new_match(self):
        TestLoginPage.test_log_in_to_the_system(self)

        dashboard_page = Dashboard(self.driver)
        dashboard_page.click_add_player_link()

        TestAddPlayer.test_template_add_new_player(self, 'TestNewMatch', 'TestNewMatch', '01012000', 'TestNewMatch')
        add_player_page = AddPlayer(self.driver)
        add_player_page.click_match_button()

        match_page = MatchForm(self.driver)
        match_page.click_add_match_button()

        TestAddMatch.test_template_add_new_match(self)
        match_page.check_visibility_alert_located()
        match_page.check_success_added_match()
        time.sleep(2)
        # match_page.save_screenshot('AM_001')

