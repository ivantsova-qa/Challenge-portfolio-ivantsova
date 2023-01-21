from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//button[@type='submit']"
    scouts_panel_title_xpath = "//div[@class='MuiCardContent-root']//h5"
    listbox_language_xpath = "//div[@aria-haspopup='listbox']"
    remaind_password_hyperlink_xpath = "//a [text()='Remind password']"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)
