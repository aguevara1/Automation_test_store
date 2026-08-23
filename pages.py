
# imports
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



# Defining the page class, locators and method in the class
class AutomationTestStorePage:
    HEADING_LOCATOR = (By.XPATH, "//div[contains(@class,'welcome_msg')]//h4[contains(text(), 'Welcome to the Automation Test Store!')]")
    LOGO_LOCATOR = (By.XPATH, '//div[contains(@class, "logo")]//img[contains(@title, "Automation Test Store")]')
    LOGIN_LOCATOR = (By.XPATH, "//a[contains(text(), 'Login or register')]")
    SEARCH_FILTER_LOCATOR = (By.ID, 'filter_keyword')
    NAV_SHOPPING_CART_LOCATOR = (By.XPATH, "//li[@data-id='menu_cart']//span[contains(@class,'menu_text')]")
    CATEGORY_MENU_LOCATOR = (By.ID,'categorymenu')
    ITEM_LOCATOR = (By.XPATH, "//a[@title='Skinsheen Bronzer Stick']")
    ITEM_QUANTITY_LOCATOR = (By.ID, 'product_quantity')
    ADD_TO_CART_BUTTON_LOCATOR = (By.CLASS_NAME,"cart")
    CHECKOUT_BUTTON_LOCATOR = (By.ID,'cart_checkout1')
    REGISTER_ACCOUNT_RADIO_LOCATOR = (By.ID, 'accountFrm_accountregister')
    REGISTER_ACCOUNT_CONTINUE_BUTTON_LOCATOR = (By.XPATH, "//button[contains(., 'Continue')]")
    CREATE_ACCOUNT_FIRST_NAME_LOCATOR = (By.ID, 'AccountFrm_firstname')
    CREATE_ACCOUNT_LAST_NAME_LOCATOR = (By.ID, 'AccountFrm_lastname')
    CREATE_ACCOUNT_EMAIL_LOCATOR = (By.ID, 'AccountFrm_email')
    CREATE_ACCOUNT_ADDRESS_LOCATOR = (By.ID, 'AccountFrm_address_1')
    CREATE_ACCOUNT_CITY_LOCATOR = (By.ID, 'AccountFrm_city')
    CREATE_ACCOUNT_REGION_STATE_LOCATOR = (By.ID, 'AccountFrm_zone_id')
    CREATE_ACCOUNT_SELECT_REGION_STATE_LOCATOR = (By.XPATH,'//option[text()="Crimea"]')
    CREATE_ACCOUNT_ZIP_CODE_LOCATOR = (By.ID, 'AccountFrm_postcode')
    CREATE_ACCOUNT_COUNTRY_LOCATOR = (By.ID, 'AccountFrm_country_id')
    CREATE_ACCOUNT_SELECT_COUNTRY_LOCATOR = (By.XPATH, '//option[text()="Ukraine"]')
    CREATE_ACCOUNT_LOGIN_NAME_LOCATOR = (By.ID, 'AccountFrm_loginname')
    CREATE_ACCOUNT_LOGIN_PASSWORD_LOCATOR = (By.ID, 'AccountFrm_password')
    CREATE_ACCOUNT_LOGIN_PASSWORD_CONFIRM_LOCATOR = (By.ID, 'AccountFrm_confirm')
    CREATE_ACCOUNT_CONTINUE_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and contains(@class,"lock-on-click") and normalize-space()="Continue"]')
    CREATE_ACCOUNT_PRIVACY_POLICY_LOCATOR = (By.ID, 'AccountFrm_agree')
    LOGIN_TO_EXISTING_ACCOUNT_LOCATOR = (By.XPATH, '//a[text()="Login or register"]')
    LOGIN_TO_EXISTING_ACCOUNT_LOGIN_NAME_LOCATOR = (By.ID, 'loginFrm_loginname')
    LOGIN_TO_EXISTING_ACCOUNT_PASSWORD_LOCATOR = (By.ID, 'loginFrm_password')
    LOGIN_TO_EXISTING_ACCOUNT_LOGIN_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and contains(@class,"btn-orange") and normalize-space()="Login"] ')
    LOGOUT_WELCOME_USER_LOCATOR = (By.XPATH, '//div[contains(text(),"Welcome back")]')
    LOGOUT_WELCOME_USER_LOGOUT_LOCATOR = (By.XPATH, '//a[contains(@href, "account/logout")]')
    #CHECKING_ORDER_HISTORY_LOCATOR = (By.XPATH, '//a[@href="https://automationteststore.com/index.php?rt=account/history"]')
    SUB_NAV_HOME_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.active.menu_home')
    SUB_NAV_HOME_BUTTON_ACCOUNT_LOCATOR = (By.XPATH, '//a[contains(@class,"menu_account")]/span[contains(@class, "menu_text") and normalize-space()="Account"]')
    CHECK_MY_ORDER_BUTTON_LOCATOR = (By.XPATH, '//a[contains(@class,"menu_order")]/span[contains(@class, "menu_text") and normalize-space()="Check Your Order"]')



    def __init__(self, driver):
        self.driver = driver  # Initialize the driver

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_heading_value(self):
        return self.driver.find_element(*self.HEADING_LOCATOR).text

    def get_logo_title(self):
        return self.driver.find_element(*self.LOGO_LOCATOR).get_attribute("title")

    def get_login_text(self):
        return self.driver.find_element(*self.LOGIN_LOCATOR).text

    def is_search_box_displayed(self):
        return self.driver.find_element(*self.SEARCH_FILTER_LOCATOR).is_displayed()

    def is_nav_shopping_cart_displayed(self):
        cart = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAV_SHOPPING_CART_LOCATOR)
        )
        return cart.is_displayed()

    def is_category_menu_displayed(self):
        return self.driver.find_element(*self.CATEGORY_MENU_LOCATOR).is_displayed()

# Automating the tests for website loading correctly
# returning a python dictionary, key, values
    def verify_website_loaded(self):
        return {
            "title": self.get_title(),
            "url": self.get_url(),
            "heading_value": self.get_heading_value(),
            "logo_title": self.get_logo_title(),
            "login_text": self.get_login_text(),
            "search_box": self.is_search_box_displayed(),
            "nav_shopping_cart": self.is_nav_shopping_cart_displayed(),
            "category_menu": self.is_category_menu_displayed(),
        }




# Product selection tests
    def select_item(self):
         WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ITEM_LOCATOR)).click()

    def select_quantity(self):
        self.driver.find_element(*self.ITEM_QUANTITY_LOCATOR).click()

    def clear_input_value(self):
        self.driver.find_element(*self.ITEM_QUANTITY_LOCATOR).clear()

    def enter_input_quantity_value(self,quantity):
        self.driver.find_element(*self.ITEM_QUANTITY_LOCATOR).send_keys(quantity)

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON_LOCATOR).click()

    def click_on_checkout(self):
        checkout = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON_LOCATOR))
        checkout.click()

# Automating the methods for checking out items into one step
    def checking_out_items(self,quantity):
        self.select_item()
        self.select_quantity()
        self.clear_input_value()
        self.enter_input_quantity_value(quantity)
        self.add_to_cart()
        self.click_on_checkout()



    # Register account ///  left off here!!!!!
    def check_register_account_radio(self):
        radio = self.driver.find_element(*self.REGISTER_ACCOUNT_RADIO_LOCATOR)
        if not radio.is_selected():
            radio.click()
        return radio.is_selected()

    def register_account_continue_button(self):
        self.driver.find_element(*self.REGISTER_ACCOUNT_CONTINUE_BUTTON_LOCATOR).click()

    # Enter user data in first name field to create account
    def enter_latin_characters_first_name(self, latin_first_name):
        self.driver.find_element(*self.CREATE_ACCOUNT_FIRST_NAME_LOCATOR).send_keys(latin_first_name)

    def get_latin_characters_first_name_value(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_FIRST_NAME_LOCATOR).get_attribute("value")

    def clear_first_name_field(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_FIRST_NAME_LOCATOR).clear()

    def enter_spaces_first_name(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_FIRST_NAME_LOCATOR).send_keys(value)

    def get_spaces_first_name_value(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_FIRST_NAME_LOCATOR).get_attribute("value")

    def enter_special_characters_first_name(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_FIRST_NAME_LOCATOR).send_keys(value)
    def get_special_characters_first_name_value(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_FIRST_NAME_LOCATOR).get_attribute("value")

# Enter user data in last name field to create account
    def enter_latin_characters_last_name(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_LAST_NAME_LOCATOR).send_keys(value)

    def get_latin_characters_last_name_value(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_LAST_NAME_LOCATOR).get_attribute("value")

    def clear_last_name_field(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_LAST_NAME_LOCATOR).clear()

    def enter_spaces_last_name(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_LAST_NAME_LOCATOR).send_keys(value)

    def get_spaces_last_name_value(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_LAST_NAME_LOCATOR).get_attribute("value")

    def enter_special_characters_last_name(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_LAST_NAME_LOCATOR).send_keys(value)

    def get_special_characters_last_name_value(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_LAST_NAME_LOCATOR).get_attribute("value")

# Enter user data in email field
    def enter_email_address(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_EMAIL_LOCATOR).send_keys(value)

    def get_email_address(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_EMAIL_LOCATOR).get_attribute("value")

    def clear_email_address_field(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_EMAIL_LOCATOR).clear()


    # Automating methods for first_name, last_name, and email address into 1-step method
    def registering_new_user_personal_details(self, latin_first_name, space_first_name, special_first_name, latin_last_name, space_last_name, special_last_name, email_address):
        self.check_register_account_radio()
        self.register_account_continue_button()
        self.enter_latin_characters_first_name(latin_first_name)
        latin_C_F_N = self.get_latin_characters_first_name_value()
        self.clear_first_name_field()
        self.enter_spaces_first_name(space_first_name)
        spaces_F_N = self.get_spaces_first_name_value()
        self.clear_first_name_field()
        self.enter_special_characters_first_name(special_first_name)
        special_C_F_N = self.get_special_characters_first_name_value()
        self.clear_first_name_field()
        # Leave a valid first name to use in the next step
        self.enter_latin_characters_first_name(latin_first_name)
        # last name tests
        self.enter_latin_characters_last_name(latin_last_name)
        latin_C_L_N = self.get_latin_characters_last_name_value()
        self.clear_last_name_field()
        self.enter_spaces_last_name(space_last_name)
        spaces_L_N = self.get_spaces_last_name_value()
        self.clear_last_name_field()
        self.enter_special_characters_last_name(special_last_name)
        special_C_L_N = self.get_special_characters_last_name_value()
        self.clear_last_name_field()
        self.enter_latin_characters_last_name(latin_last_name)
        # email tests
        self.enter_email_address(email_address)
        email_address_check = self.get_email_address()
        return{
            "latin_characters_f_n": latin_C_F_N,
            "spaces_f_n": spaces_F_N,
            "special_characters_f_n": special_C_F_N,
            "latin_characters_l_n": latin_C_L_N,
            "spaces_l_n": spaces_L_N,
            "special_characters_l_n": special_C_L_N,
            "email_address_l_n": email_address_check
        }




# Enter physical address
    def enter_address(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_ADDRESS_LOCATOR).send_keys(value)

    def get_address(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_ADDRESS_LOCATOR).get_attribute("value")

    def clear_address_field(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_ADDRESS_LOCATOR).clear()
# Enter city
    def enter_city(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_CITY_LOCATOR).send_keys(value)

    def get_city(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_CITY_LOCATOR).get_attribute("value")

    def clear_city_field(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_CITY_LOCATOR).clear()
# Enter region state, searchable drop-down
    def click_region_state(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_REGION_STATE_LOCATOR).click()

    def select_region_state(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_SELECT_REGION_STATE_LOCATOR)).click()

# Enter zip code
    def click_on_zip_code_field(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CREATE_ACCOUNT_ZIP_CODE_LOCATOR)).click()

    def enter_zip_code(self, value):
        self.driver.find_element(*self.CREATE_ACCOUNT_ZIP_CODE_LOCATOR).send_keys(value)

    def get_zip_code(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_ZIP_CODE_LOCATOR).get_attribute("value")

    def clear_zip_code_field(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_ZIP_CODE_LOCATOR).clear()
# Enter country, searchable drop-down list
    def click_country_field(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_COUNTRY_LOCATOR).click()

    def select_country(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_SELECT_COUNTRY_LOCATOR).click()

# Automating methods for address, city, zip and country

    def entering_complete_address_country(self, address, city, zip_code):
        self.enter_address(address)
        address_returned = self.get_address()
        self.enter_city(city)
        city_returned = self.get_city()
        # selecting country first that way the region state belong to chosen country
        self.click_country_field()
        self.select_country()
        self.click_region_state()
        self.select_region_state()
        self.click_region_state()
        self.click_on_zip_code_field()
        self.enter_zip_code(zip_code)
        zip_returned = self.get_zip_code()
      #  self.click_country_field()
      #  self.select_country()
        self.click_login_name_field()
        return {
            "address_returned": address_returned,
            "city_returned": city_returned,
            "zip_returned": zip_returned
        }



# Create login name
    def click_login_name_field(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_LOGIN_NAME_LOCATOR).click()

    def enter_login_name(self,value):
        self.driver.find_element(*self.CREATE_ACCOUNT_LOGIN_NAME_LOCATOR).send_keys(value)

    def get_login_name(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_LOGIN_NAME_LOCATOR).get_attribute("value")
# Create login password
    def enter_login_password(self,value):
        self.driver.find_element(*self.CREATE_ACCOUNT_LOGIN_PASSWORD_LOCATOR).send_keys(value)

    def get_login_password(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_LOGIN_PASSWORD_LOCATOR).get_attribute("value")

# Create confirm password
    def enter_login_password_confirm(self,value):
        self.driver.find_element(*self.CREATE_ACCOUNT_LOGIN_PASSWORD_CONFIRM_LOCATOR).send_keys(value)

    def get_login_password_confirm(self):
        return self.driver.find_element(*self.CREATE_ACCOUNT_LOGIN_PASSWORD_CONFIRM_LOCATOR).get_attribute("value")

# Click privacy policy checkbox
    def click_privacy_policy(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_PRIVACY_POLICY_LOCATOR).click()

# Click create account continue button
    def click_create_account_continue_button(self):
        self.driver.find_element(*self.CREATE_ACCOUNT_CONTINUE_BUTTON_LOCATOR).click()

# Automating the methods for creating a login name, password and confirming reading privacy policy
    def creating_login_name_password(self, login_name, password, password_confirmed):
        self.enter_login_name(login_name)
        login_name_entered = self.get_login_name()
        self.enter_login_password(password)
        password_entered = self.get_login_password()
        self.enter_login_password_confirm(password_confirmed)
        password_confirmed_entered = self.get_login_password_confirm()
        self.click_privacy_policy()
        self.click_create_account_continue_button()
        return {
            "login_name_entered": login_name_entered,
            "password_entered": password_entered,
            "password_confirmed_entered": password_confirmed_entered
        }


    def click_login_or_register(self):
        self.driver.find_element(*self.LOGIN_TO_EXISTING_ACCOUNT_LOCATOR).click()

    def enter_account_login_name(self, login_name):
        self.driver.find_element(*self.LOGIN_TO_EXISTING_ACCOUNT_LOGIN_NAME_LOCATOR).send_keys(login_name)

    def enter_account_password(self, password):
        self.driver.find_element(*self.LOGIN_TO_EXISTING_ACCOUNT_PASSWORD_LOCATOR).send_keys(password)

    def click_account_login_button(self):
        self.driver.find_element(*self.LOGIN_TO_EXISTING_ACCOUNT_LOGIN_BUTTON_LOCATOR).click()

    # Hover over
    def hover_over_home_button(self):
        home_button = self.driver.find_element(*self.SUB_NAV_HOME_BUTTON_LOCATOR)
        ActionChains(self.driver).move_to_element(home_button).perform()

    # Hover over
    def hover_over_account_button(self):
        account_button = self.driver.find_element(*self.SUB_NAV_HOME_BUTTON_ACCOUNT_LOCATOR)
        ActionChains(self.driver).move_to_element(account_button).perform()

    def click_check_my_order_button(self):
        self.driver.find_element(*self.CHECK_MY_ORDER_BUTTON_LOCATOR).click()

    def hover_welcome_back_user(self):
        for_logoff = self.driver.find_element(*self.LOGOUT_WELCOME_USER_LOCATOR)
        ActionChains(self.driver).move_to_element(for_logoff).perform()

    def click_logout(self):
        logout_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGOUT_WELCOME_USER_LOGOUT_LOCATOR))
        logout_button.click()

    # Automating existing account login
    def existing_user_login(self,login_name, password):
        self.click_login_or_register()
        self.enter_account_login_name(login_name)
        self.enter_account_password(password)
        self.click_account_login_button()
        self.hover_over_account_button()
        self.click_check_my_order_button()
        self.hover_welcome_back_user()
        self.click_logout()










