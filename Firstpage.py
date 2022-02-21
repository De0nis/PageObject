from BasePage import Base
from Locators import FirstpagePageLocators
class Titlepage(Base):
    
    def open(browsertype,url):
        Base.open(browsertype,url)

    def should_be_located_search_field(self,browser):
        assert(Base.is_element_present(self,browser,(FirstpagePageLocators.SEARCH_FIELD))), (                    
         "Search field is not presented, but should be")

    def shold_be_key_send_field_text(self,browser):
        assert(Base.is_key_sending(self,browser,(FirstpagePageLocators.SEARCH_FIELD), (FirstpagePageLocators.SEARCH_KEY))),(
         "key in field is not presented, but should be")
        
    def should_be_mail_link (self,browser):
        assert(Base.is_element_present(self,browser,(FirstpagePageLocators.MAIL_LOCATOR))), (                      
        "Mail link is not presented, but should be")  

    def should_be_located_loginform(self,browser):
        assert(Base.is_element_present(self,browser,(FirstpagePageLocators.LOGIN_FORM))), (                      
        "LoginForm is not presented, but should be")
    
    def should_be_open_loginform(self,browser):
        assert(Base.is_new_window_opening(browser, (FirstpagePageLocators.LOGIN_FORM), FirstpagePageLocators.LOGIN_FORM2)), (                      
       "LoginForm is not opend, but should be")

