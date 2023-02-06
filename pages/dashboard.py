import time

from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_title_xpath = "//header/div/h6"
    main_page_button_xpath = "//span[text()='Main page']//ancestor-or-self::div[@role='button']"
    players_button_xpath = "//ul[1]/div[2]"
    change_language_button_xpath = "//*/ul[2]/div[1]"
    sign_out_button_xpath = "//span[text()='Sign out']//ancestor-or-self::div[@role='button']"
    add_player_button_xpath = "//*[2][name() = 'a']/button"
    dev_team_contact_button_xpath = "//a[@target='_blank']"
    logo_scouts_panel_xpath = "//div[@title='Logo Scouts Panel']"
    players_count_section_xpath = "//div[text()='Players count']/parent::div/parent::div"
    matches_count_section_xpath = "// div[text() = 'Matches count'] / parent::div / parent::div"
    reports_count_section_xpath = "//div[text()='Reports count']/parent::div/parent::div"
    events_count_section_xpath = "//div[text()='Events count']/parent::div/parent::div"
    scouts_panel_text_xpath = "//div[@class='MuiCardContent-root']//p"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/'
    expected_title = 'Scouts panel'
    statistic_section_xpath = '//*/main/div[2]'
    expected_text = 'Players count'

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.scouts_panel_title_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_add_player_link(self):
        self.wait_for_presence_of_element_located(self.statistic_section_xpath)
        self.click_on_the_element(self.add_player_button_xpath)

    def check_text_to_be_present_in_element(self):
        self.wait_for_text_to_be_present_in_element(self.expected_text, self.statistic_section_xpath)

    def check_visibility_of_element_located(self):
        self.wait_for_visibility_of_element_located(self.logo_scouts_panel_xpath)

    def check_url_to_be(self):
        self.wait_for_url_to_be(self.dashboard_url)

    def click_players_button(self):
        self.click_on_the_element(self.players_button_xpath)
