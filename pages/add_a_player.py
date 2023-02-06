import time

from pages.base_page import BasePage


class AddPlayer(BasePage):
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title = 'Add player'
    name_field_xpath = '//input[@name="name"]'
    surname_field_xpath = '//input[@name="surname"]'
    phone_field_xpath = '//input[@name="phone"]'
    weight_field_xpath = '//input[@name="weight"]'
    height_field_xpath = '//input[@name="height"]'
    age_field_xpath = '//input[@name="age"]'
    main_position_field_xpath = '//input[@name="mainPosition"]'
    submit_button_xpath = '//*[text()= "Submit"]'
    all_input_fields_xpath = '//*/form/div[2]/div//input'
    text_for_fields = ''
    email_field_xpath = '//input[@name="email"]'
    right_leg_xpath = '//*/ul/li[1]'
    leg_dropdown_xpath = '//*[@id="mui-component-select-leg"]'
    club_field_xpath = '//input[@name="club"]'
    level_field_xpath = '//input[@name="level"]'
    second_position_field_xpath = '//input[@name="secondPosition"]'
    district_dropdown_xpath = '//*[@id="mui-component-select-district"]'
    achievements_field_xpath = '//input[@name="achievements"]'
    laczy_field_xpath = '//input[@name="webLaczy"]'
    nineteen_minute_field_xpath = '//input[@name="web90"]'
    facebook_field_xpath = '//input[@name="webFB"]'
    clear_button_xpath = '//*/button[2]/span[1]'
    lodz_district_xpath = '//*[@id="menu-district"]//li[5]'
    alert_successful_save_xpath = '//div[@role="alert"]'
    text_successful_saved_players = 'Saved player.'
    match_button_xpath = '//*/ul[2]/div[2]'

    def title_of_page(self):
        time.sleep(3)
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def check_url_to_be(self):
        self.wait_for_url_to_be(self.add_player_url)

    def check_alert_is_not_present(self):
        self.wait_for_alert_is_not_present()

    def type_in_email(self, email):
        self.field_send_keys(self.email_field_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.phone_field_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.weight_field_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.height_field_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.age_field_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def check_text_to_be_present_in_element_value(self):
        self.wait_for_text_to_be_present_in_element_value(self.text_for_fields, self.all_input_fields_xpath)

    def select_right_leg_dropdown_list(self):
        self.select_item_from_dropdown_list(self.leg_dropdown_xpath, self.right_leg_xpath)

    def type_in_club(self, club):
        self.field_send_keys(self.club_field_xpath, club)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    def type_in_second_position(self, second_position):
        self.field_send_keys(self.second_position_field_xpath, second_position)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.achievements_field_xpath, achievements)

    def select_district_dropdown_list(self):
        self.select_item_from_dropdown_list(self.district_dropdown_xpath, self.lodz_district_xpath)

    def type_in_laczy(self, laczy):
        self.field_send_keys(self.laczy_field_xpath, laczy)

    def type_in_nineteen_minute(self, nineteen_minute):
        self.field_send_keys(self.nineteen_minute_field_xpath, nineteen_minute)

    def type_in_facebook(self, facebook):
        self.field_send_keys(self.facebook_field_xpath, facebook)

    def click_clear_button(self):
        self.click_on_the_element(self.clear_button_xpath)

    def check_success_saved_player(self):
        self.wait_for_text_to_be_present_in_element_value(self.text_successful_saved_players,
                                                          self.alert_successful_save_xpath)

    def click_match_button(self):
        self.click_on_the_element(self.match_button_xpath)

    def check_empty_filed(self):
        self.assert_element_text(self.driver, self.email_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.name_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.surname_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.phone_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.weight_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.height_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.age_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.leg_dropdown_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.club_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.level_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.main_position_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.second_position_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.district_dropdown_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.achievements_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.laczy_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.nineteen_minute_field_xpath, self.text_for_fields)
        self.assert_element_text(self.driver, self.facebook_field_xpath, self.text_for_fields)