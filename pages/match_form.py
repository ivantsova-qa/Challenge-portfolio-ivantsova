from pages.base_page import BasePage


class MatchForm(BasePage):

    add_match_button_xpath = '//a/button'

    my_team_field_xpath = "//input[@name='myTeam']"
    enemy_team_field_xpath = "//input[@name='enemyTeam']"
    my_team_score_field_xpath = "//input[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//input[@name='enemyTeamScore']"
    date_selection_xpath = "//input[@name='date']"
    match_at_home_radiobutton_xpath = "//input[@name='matchAtHome' and contains (@value, 'true')]"
    match_out_home_radiobutton_xpath = "//input[@name='matchAtHome' and contains (@value, 'false')]"
    tshirt_color_field_xpath = "//input[@name='tshirt']"
    league_field_xpath = "//input[@name='league']"
    time_played_field_xpath = "//input[@name='timePlayed']"
    number_field_xpath = "//input[@name='number']"
    web_match_field_xpath = "//input[@name='webMatch']"
    general_field_xpath = "//input[@name='general']"
    rating_field_xpath = "//input[@name='rating']"

    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//span[text()='Clear']//parent::button"

    player_button_xpath = "//ul[2]/div[1]"
    matches_button_xpath = "//span[text()='Matches']/ancestor::div[2]"
    reports_button_xpath = "//span[text()='Reports']/ancestor::div[2]"

    added_match_alert_xpath = "//div[text()='Added match.']"
    success_added_match_text = 'Added match.'

    def click_add_match_button(self):
        self.click_on_the_element(self.add_match_button_xpath)

    def type_in_my_team(self, my_team):
        self.field_send_keys(self.my_team_field_xpath, my_team)

    def type_in_enemy_team(self, enemy_team):
        self.field_send_keys(self.enemy_team_field_xpath, enemy_team)

    def type_in_my_team_score(self, my_team_score):
        self.field_send_keys(self.my_team_score_field_xpath, my_team_score)

    def type_in_enemy_team_score(self, enemy_team_score):
        self.field_send_keys(self.enemy_team_score_field_xpath, enemy_team_score)

    def type_in_date(self, date):
        self.field_send_keys(self.date_selection_xpath, date)

    def click_match_at_home_radiobutton(self):
        self.click_on_the_element(self.match_at_home_radiobutton_xpath)

    def click_match_out_home_radiobutton(self):
        self.click_on_the_element(self.match_out_home_radiobutton_xpath)

    def type_in_t_short_color_field(self, t_short_color):
        self.field_send_keys(self.tshirt_color_field_xpath, t_short_color)

    def type_in_league_field(self, league):
        self.field_send_keys(self.league_field_xpath, league)

    def type_in_time_played_field(self, time_play_field):
        self.field_send_keys(self.time_played_field_xpath, time_play_field)

    def type_in_number_field(self, number):
        self.field_send_keys(self.number_field_xpath, number)

    def type_in_web_match_field(self, web_match):
        self.field_send_keys(self.web_match_field_xpath, web_match)

    def type_in_general_field(self, general):
        self.field_send_keys(self.general_field_xpath, general)

    def type_in_rating_field(self,rating):
        self.field_send_keys(self.rating_field_xpath, rating)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def check_success_added_match(self):
        self.wait_for_text_to_be_present_in_element_value(self.success_added_match_text,
                                                          self.added_match_alert_xpath)

    def check_visibility_alert_located(self):
        self.wait_for_visibility_of_element_located(self.added_match_alert_xpath)

