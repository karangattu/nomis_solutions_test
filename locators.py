from selenium.webdriver.common.by import By

class NomisSolutionsPageLocators(object):
    """A class for Nomis Solutions Page locators. All Nomis Solutions Page locators should be listed here"""
    SEARCH_BOX = (By.NAME, 'search')
    SEARCH_BUTTON = (By.CLASS_NAME, 'gsc-search-button')
    GET_STARTED_BUTTON = (By.LINK_TEXT, 'GET STARTED')

