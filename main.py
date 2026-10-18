
import data
from selenium import webdriver
from pages import AutomationTestStorePage
import time

# class with different functions for testing the app
class TestAutomationTestStore:

    @classmethod
    def setup_class(cls):
      #  cls.driver = webdriver.Chrome()
      #  cls.driver.maximize_window()
      

        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        cls.driver = webdriver.Chrome(options=options)




    #  self means the current instance of the class
    # Basic Homepage Smoke Tests
    # ============================================================
    # Individual validation tests retained for troubleshooting.
    # Uncomment a test when isolating a specific page-element failure.
    # ============================================================
    #def test_homepage_title(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    expected_title = "A place to practice your automation skills!"
    #    assert homepage.get_title() == expected_title

    #def test_homepage_url(self):
    #   self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    assert homepage.get_url() == data.AUTOMATION_TEST_STORE_URL

    #def test_heading_msg(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    assert 'Welcome to the Automation Test Store!' in homepage.get_heading_value()

    #def test_logo_title(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    assert homepage.get_logo_title() == "Automation Test Store"

    #def test_login_text(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    assert homepage.get_login_text() == "Login or register"

    #def test_search_box_visibility(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    assert homepage.is_search_box_displayed() == True

    #def test_nav_shopping_cart_visibility(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    assert homepage.is_nav_shopping_cart_displayed() == True

    #def test_category_menu_visibility(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    assert homepage.is_category_menu_displayed() == True


    # Calling the step function from POM pages.py
    def test_website_loaded(self):
        self.driver.get(data.AUTOMATION_TEST_STORE_URL)
        homepage = AutomationTestStorePage(self.driver)
        result = homepage.verify_website_loaded()
        assert result["title"] == "A place to practice your automation skills!"
        assert result["url"] == data.AUTOMATION_TEST_STORE_URL
        assert 'Welcome to the Automation Test Store!' in result["heading_value"]
        assert result["logo_title"] == "Automation Test Store"
        assert result["login_text"] == "Login or register"
        assert result["search_box"] is True
        assert result["nav_shopping_cart"] is True
        assert result["category_menu"] is True



    # ============================================================
    # Individual validation tests retained for troubleshooting.
    # Uncomment a test when isolating a specific page-element failure.
    # ============================================================

    # Navigation Tests
    #def test_item_selected(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    homepage.select_item()
    #    time.sleep(10)


    #def test_item_input_quantity(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    homepage.select_quantity()
    #    time.sleep(8)

    #def test_item_quantity_and_checkout(self):
    #    self.driver.get(data.AUTOMATION_TEST_STORE_URL)
    #    homepage = AutomationTestStorePage(self.driver)
    #    homepage.select_item()
    #    homepage.select_quantity()
    #    homepage.clear_input_value()
    #    homepage.enter_input_quantity_value(2)
    #    homepage.add_to_cart()
    #    homepage.click_on_checkout()
    #    time.sleep(8)

    # Calling the step function for checking out items
    def test_checking_out_items(self):
        self.driver.get(data.AUTOMATION_TEST_STORE_URL)
        homepage = AutomationTestStorePage(self.driver)
        homepage.checking_out_items(2)


    # Automating the methods that enter personal details in the new user account registration
    def test_entering_new_user_personal_details(self):
        self.driver.get(data.AUTOMATION_TEST_STORE_URL)
        homepage = AutomationTestStorePage(self.driver)
        # Complete checkout before entering registration details
        homepage.checking_out_items(2)
        results = homepage.registering_new_user_personal_details("jose", "jose juan", "jose#",
       "Gonzales", "Garcia Gonzalez", "Sandoval%%", "JohnSmith@bikers.com")
        assert results["latin_characters_f_n"] == "jose"
        assert results["spaces_f_n"] == "jose juan"
        assert results["special_characters_f_n"] == "jose#"
        assert results["latin_characters_l_n"] == "Gonzales"
        assert results["spaces_l_n"] == "Garcia Gonzalez"
        assert results["special_characters_l_n"] == "Sandoval%%"
        assert results["email_address_l_n"] == "JohnSmith@bikers.com"


    # ============================================================
    # This test calls on all the methods from selecting item to finishing registering
    # Uncomment a test when isolating a specific page-element failure.
    # ============================================================
    def test_create_account(self):
        self.driver.get(data.AUTOMATION_TEST_STORE_URL)
        homepage= AutomationTestStorePage(self.driver)
        homepage.select_item()
        homepage.select_quantity()
        homepage.clear_input_value()
        homepage.enter_input_quantity_value(2)
        homepage.add_to_cart()
        homepage.click_on_checkout()
        assert homepage.check_register_account_radio()
        homepage.register_account_continue_button()
        homepage.enter_latin_characters_first_name("John")
        assert homepage.get_latin_characters_first_name_value() == "John"
        homepage.clear_first_name_field()
        homepage.enter_spaces_first_name("Emily Lynn")
        assert homepage.get_spaces_first_name_value() == "Emily Lynn"
        homepage.clear_first_name_field()
        homepage.enter_special_characters_first_name("John$$" )
        assert homepage.get_special_characters_first_name_value() == "John$$"
        homepage.clear_first_name_field()
    # last name tests
        homepage.enter_latin_characters_last_name("Delgado")
        assert homepage.get_latin_characters_last_name_value() == "Delgado"
        homepage.clear_last_name_field()
        homepage.enter_spaces_last_name("Sanchez Cuevas")
        assert homepage.get_spaces_last_name_value() =="Sanchez Cuevas"
        homepage.clear_last_name_field()
        homepage.enter_special_characters_last_name("Martinez#")
        assert homepage.get_special_characters_last_name_value() == "Martinez#"
        homepage.clear_last_name_field()
    # email address tests
        homepage.enter_email_address("johndoe@example.com")
        assert homepage.get_email_address() == "johndoe@example.com"
        homepage.clear_email_address_field()
    # address tests
        homepage.enter_address("1234 Smith Hwy")
        assert homepage.get_address() == "1234 Smith Hwy"
        homepage.clear_address_field()
    # city tests
        homepage.enter_city("San Jose")
        assert homepage.get_city() == "San Jose"
        homepage.clear_city_field()
    # region state tests
        homepage.click_region_state()
        homepage.select_region_state()
    # zip code tests
        homepage.enter_zip_code("78741")
        time.sleep(25)
        assert homepage.get_zip_code() == "78741"
        homepage.clear_zip_code_field()
    # country tests
        homepage.click_country_field()
        homepage.select_country()
    # create login name
        homepage.enter_login_name("joseph12")
        assert homepage.get_login_name() == "joseph12"
    # create login password
        homepage.enter_login_password("che1234")
        assert homepage.get_login_password() == "che1234"
    # confirm password test
        homepage.enter_login_password_confirm("che1234")
        assert homepage.get_login_password_confirm() == "che1234"
    # click privacy policy checkbox
        homepage.click_privacy_policy()
    # click create account continue button
        homepage.click_create_account_continue_button()
        time.sleep(8)


# Automating methods for testing complete address details
    # the region state is not being selected,,,the field is left BLANK!!!!!!!!!!!!!*****
    def test_complete_address_country(self):
        self.driver.get(data.AUTOMATION_TEST_STORE_URL)
        homepage = AutomationTestStorePage(self.driver)
        # Complete checkout before entering registration details
        homepage.checking_out_items(2)
        # Entering personal details
        homepage.registering_new_user_personal_details("jose", "jose juan", "jose#",
       "Gonzales", "Garcia Gonzalez", "Sandoval%%", "JohnSmith@bikers.com")

        result = homepage.entering_complete_address_country("123 Smith Ave", "San Miguel","12345")
        assert result["address_returned"] == "123 Smith Ave"
        assert result["city_returned"] == "San Miguel"
        assert result["zip_returned"] == "12345"
        time.sleep(8)


# Automating methods for testing login credentials, reading privacy policy and continuing
    def test_login_credentials_privacy_policy_continuing(self):
        self.driver.get(data.AUTOMATION_TEST_STORE_URL)
        homepage = AutomationTestStorePage(self.driver)
        # Complete checkout before entering registration details
        homepage.checking_out_items(2)
        # Entering personal details
        homepage.registering_new_user_personal_details("jose", "jose juan", "jose#",
       "Gonzales", "Garcia Gonzalez", "Sandoval%%",
       "JohnSmith@bikers.com")
        # Entering complete address
        homepage.entering_complete_address_country("123 Smith Ave", "San Miguel", "12345")
        result = homepage.creating_login_name_password("Toshua1234", "vlut1439", "vlut1439")
        assert result["login_name_entered"] == "Toshua1234"
        assert result["password_entered"] == "vlut1439"
        assert result["password_confirmed_entered"] == "vlut1439"
        time.sleep(20)


    def test_login_to_existing_account(self):
        self.driver.get(data.AUTOMATION_TEST_STORE_URL)
        homepage = AutomationTestStorePage(self.driver)
        homepage.existing_user_login("Joshua123", "pass12345")
        time.sleep(20)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()