from selenium.webdriver.common.by import By

class LoginpageLocators(object):
    LOGIN_ID_FIELD = (By.ID,"passp-field-login")
    LOGIN_INCORRECT=(By.ID,"field:input-login:hint")
    LOGIN_INCORRECT_ANSWER=('text')
    LOGIN_CONFORM_BUTTON=(By.ID,"passp:sign-in")
    LOGIN_PASS = (By.ID,"passp-field-phoneCode")
    LOGIN_PASS2 = (By.ID,"passp-field-confirmation-code")
class FirstpagePageLocators(object):
    LOGIN_FORM=(By.LINK_TEXT,"Войти")
    LOGIN_FORM2=(By.CLASS_NAME,"passp-login-form")
    MAIL_LOCATOR=(By.LINK_TEXT,"Почта")
    SEARCH_FIELD=(By.ID, "text")
    SEARCH_KEY=('ян')