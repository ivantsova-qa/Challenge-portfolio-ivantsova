from pages.base_page import BasePage


class MatchForm(BasePage):
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

pass