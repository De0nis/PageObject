from BasePage import Base
from Locators import LoginpageLocators

class Loginpage(Base):
    def should_be_login_form(self, browser):  
        assert Base.is_element_present(self, browser, (LoginpageLocators.LOGIN_ID_FIELD)), ("Login form is not presented")
    def should_send_key_to_form(self, browser, key):
        browser.get('https://passport.yandex.ru')     
        Base.is_key_sending(self, browser, key, (LoginpageLocators.LOGIN_ID_FIELD))
        Base.press_button(self, browser, (LoginpageLocators.LOGIN_CONFORM_BUTTON)) 
        assert (Base.is_element_present(self, browser, (LoginpageLocators.LOGIN_INCORRECT))) or (Base.is_element_present(self, browser, 
        (LoginpageLocators.LOGIN_INCORRECT2))), ("Login form is not presented")

   
