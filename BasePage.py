from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from conftest import browser
class Base:                                    #main_test_base_class
        def __init__(self):
            self.browser=browser()
            
        def is_element_present(self,browser,locator):
            try:
                browser.find_element(*locator)
            except NoSuchElementException:
               return False      
            return True    
            
        def is_element_not_present(self,browser, locator):
            try:
                browser.find_element(*locator)
            except TimeoutException:
                return True
            return False

        def is_key_sending(self,browser,key, locator):
            try:
                browser.find_element(*locator).send_keys(*key)
            except NoSuchElementException:
                return False      
            return True    

        def clear_form(self,browser, locator):   
                browser.find_element(*locator).clear()
                return True   

        def press_button(self,browser, locator):   
                browser.find_element(*locator).click()       
                return True    

        def return_answer(self,browser, locator1,locator2):
            try:
                answer=(browser.find_element(*locator1).get_attribute(*locator2))
            except NoSuchElementException:
                return False      
            return answer     

        def current_URL(browser):
                 curl=browser.current_url
                 return curl

        def is_new_window_opening(browser, locator, locator2):
            try:
                browser.find_element(*locator).click()
                newimage_window = browser.window_handles[0]
                browser.switch_to.window(newimage_window)
                browser.find_element(*locator2)  
            except NoSuchElementException:
                return False      
            return True
           

