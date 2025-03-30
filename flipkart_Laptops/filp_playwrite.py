from playwright.sync_api import sync_playwright as sy
from flip_laptops import crapData

fURL = 'https://www.flipkart.com/'

with sy() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(fURL)
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(2000)

    firstSearch = page.query_selector('input[title="Search for Products, Brands and More"]')
    firstSearch.fill('laptop gaming')
    page.wait_for_timeout(2000)

    search_button = page.query_selector('button[aria-label="Search for Products, Brands and More"]')
    search_button.click()
    
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(2000)

    crapData(page.inner_html('body'))