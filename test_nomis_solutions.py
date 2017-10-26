'''Test for Nomis Solutions home page'''
import pytest
from selenium import webdriver
import base_page

@pytest.fixture(scope='function')
def driver(request):
    ''' Fixture used to initialize driver for each test and close it at the end of the test'''
    driver = webdriver.Chrome('')  # Add your chromedriver location here
    driver.maximize_window()
    driver.get('https://www.nomissolutions.com/') # Navigate to the Nomis base page
    def teardown_function():
        ''' Close Chrome Browser once the test finish irrespective if test pass/fail'''
        driver.quit()
    request.addfinalizer(teardown_function)
    return driver

def test_get_started_redirect(driver):
    '''Used to navigate to Get Started Page when clicked on button'''
    nomis_page = base_page.NomisSolutionsPage(driver)
    nomis_page.click_get_started_btn()
    assert nomis_page.page_url() == 'https://info.nomissolutions.com/get-started'

def test_nomis_page_load(driver):
    '''Used to verify if user has landed on the right page'''
    nomis_page = base_page.NomisSolutionsPage(driver)
    assert nomis_page.page_url() == 'https://www.nomissolutions.com/'
    assert nomis_page.page_title() == 'Nomis Solutions | Bank Price Optimization Software'

def test_nomis_solutions_search(driver):
    '''Used to test Nomis Solutions search engine'''
    nomis_page = base_page.NomisSolutionsPage(driver)
    nomis_page.search_box_enter('test')
    # Check if clicking on search results redirects to appropriate page
    assert nomis_page.page_url() == 'https://www.nomissolutions.com/search?q=test'
