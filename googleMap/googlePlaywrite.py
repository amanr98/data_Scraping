from playwright.sync_api import sync_playwright as sp
from googleComman import googleload
from googleData import googleHtml

googleURL = 'https://www.google.com/maps/'

with sp() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url=googleURL)
    googleload(page)

    page.query_selector('input.searchboxinput ').fill('best restaurants in nagpur')
    googleload(page)

    page.query_selector('button#searchbox-searchbutton').click()
    googleload(page)
    

    page.query_selector_all('a.hfpxzc')[0].click()
    googleload(page,screenshot='googleMap/a.png',timeout=4000)

    googleHtml(page.inner_html('body'))
    

