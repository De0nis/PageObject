
from Loginpage import Loginpage
import pytest
@pytest.fixture(scope='session')
def url():
    url='https://passport.yandex.ru'
    return url

class Testloginepage:
   
    @pytest.mark.smoke
    def test_find_search_field(self,browser):  
        Loginpage.should_be_login_form(self,browser)

    def test_sending_uncorrect_keys_5numbers(self,browser,key='55555'):    
        Loginpage.should_send_key_to_form(self,browser,key)

    def test_sending_uncorrect_keys_8symbols(self,browser,key='#@$%:&*}'):    
        Loginpage.should_send_key_to_form(self,browser,key)

    def test_sending_uncorrect_keys_8letters(self,browser,key='yuighjnb'):    
        Loginpage.should_send_key_to_form(self,browser,key)

    def test_sending_correct_keys_mail(self,browser,key='zzzz@xx.com'):    
        Loginpage.should_send_key_to_form(self,browser,key)

    def test_sending_correct_keys_phone(self,browser,key='89999999999'):    
        Loginpage.should_send_key_to_form(self,browser,key)
    
    