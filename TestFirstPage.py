from Firstpage import Titlepage
import pytest
@pytest.fixture(scope = 'session')
def url():
    url = 'https://yandex.ru'
    return url

class TestTitlepage:
    @pytest.mark.smoke 
    def test_find_search_field(self, browser):
        Titlepage.should_be_located_search_field(self, browser)
 
    def test_key_send_search_field(self, browser):
        Titlepage.shold_be_key_send_field_text(self, browser)
    @pytest.mark.smoke 
    def test_find_mail_link(self, browser):
        Titlepage.should_be_located_search_field(self, browser)
    @pytest.mark.smoke 
    def test_login_form_on_titlepage(self, browser):
        Titlepage.should_be_located_loginform(self, browser)
    @pytest.mark.smoke 
    def  test_login_form_open(self, browser):
         Titlepage.should_be_open_loginform(self, browser)

      
