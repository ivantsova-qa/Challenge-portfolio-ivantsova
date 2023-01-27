# Task 1: Software configuration

## Subtask 1: Why did I choose to participate in the Dare IT Challenge?
I decided to take part in the Dare IT Challenge to learn to write autotest and check my knowledge in testing and possibly to become a part of the Dare IT team in the future.

Inspires me to learn new steck technologies, testing approach, programming languages,  and apply them in practice, not just to learn the theory.

My goal is to complete this Challenge and get an internship at the Dare IT company.

From the course I expect cool experienced mentors, a lot of communication and new acquaintances, interesting and close to real work tasks, develop my knowledge in automated testing.

# Task 2: Selectors

> Searching for selectors on the login pageList all the elements that are on the login page.

### Examples 

- scouts_panel_title_xpath
```
//h5
//*[@id="__next"]/form/div/div[1]/h5
//h5[contains(@class,"MuiTypography-h5")]
//div[@class="MuiCardContent-root"]//h5
//child::div/h5
```
- login_field_xpath
```
//*[@id="login"]
//input[@name="login"]
/html/body/div/form/div/div[1]/div[1]/div/input
//child::div/input[@name="login"]
//input[@type="text"]
```
- password_field_xpath
```
//*[@id="password"]
//input[@name="password"]
/html/body/div/form/div/div[1]/div[2]/div/input
//child::div//input [@type="password"]
//input[@type="password"]
```
- remaind_password_hyperlink_xpath
```
//*[@id="__next"]/form/div/div[1]/a
//a [text()="Remind password"]
//a[contains(text(),"password")]
//child::div/a
//div/following-sibling::a
/html/body/div/form/div/div[1]/a
//div [@class="MuiCardContent-root"]/a
```
- listbox_language_xpath
```
//*[@id="__next"]/form/div/div[2]/div/div
//div[@role="button"]
//div[text()="English"]
//input/preceding-sibling::div
//div[@aria-haspopup="listbox"]
```
- sign_in_button_xpath
```
//*[@id="__next"]/form/div/div[2]/button
//button[@type="submit"]
//span[@class="MuiButton-label"]/parent::button
//child::div/button
//div/following-sibling::button
//div/following-sibling::button[contains(@type, "submit")]
```
# Task 3: First automatic test, asserts
### Goal
>The goal of the task is to perform an automatic test that checks the correctness of the displayed page title, click on the button, Fill the fields with text.

✅ Get to know the "framework" <br>
✅ Click on the elements on the page <br>
✅ Fill the fields with text <br>
✅ Use "assert" <br>
✅ Start testing <br>