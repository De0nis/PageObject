import pytest
from selenium import webdriver
   
@pytest.fixture(scope='session')
def browser(url):
    print("\nstart Crome browser for test..")
    browser = webdriver.Chrome()
    
    browser.implicitly_wait(15)
    browser.get(url)    
    yield browser
    print("\nquit browser..")
    browser.quit()
   