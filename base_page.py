from locators import *

class BasePage(object):
    '''Base class to initialize the base page which is inherited by other Pages'''
    def __init__(self, driver):
        self.driver = driver

class NomisSolutionsPage(BasePage):
    '''This is the page for the Nomis Solutions Home Page'''

    def click_get_started_btn(self):
        ''' Method used to navigate to the get started page'''
        self.driver.find_element(*NomisSolutionsPageLocators.GET_STARTED_BUTTON).click()

    def page_title(self):
        ''' Return page title'''
        return self.driver.title

    def page_url(self):
        ''' Return page url'''
        return self.driver.current_url

    def search_box_enter(self, text):
        '''Method used to click on search box and submit the input by user 

        Args:
            text (string): Text to be entered and submitted in the search box
        '''
        element = self.driver.find_element(*NomisSolutionsPageLocators.SEARCH_BOX)
        element.send_keys(text)
        self.driver.find_element(*NomisSolutionsPageLocators.SEARCH_BUTTON).click()
