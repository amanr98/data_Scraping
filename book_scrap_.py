from playwright.sync_api import sync_playwright as sy

book_info = []

def ratingfun(string):
    switch = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return switch.get(string, "Invalid input") 

with sy() as py:
    browser = py.chromium.launch()
    page = browser.new_page()
    page.goto('https://books.toscrape.com/')


    books = page.query_selector_all('.product_pod')
    # title = books.query_selector('h3 a').get_attribute('title')
    # print(title)
    # price = books.query_selector('.price_color').text_content()
    # print(price)

    # rating = books.query_selector('p.star-rating').get_attribute('class')
    # print(rating)
    
    for book_I in books:
        title = book_I.query_selector('h3 a').get_attribute('title')
        price = book_I.query_selector('.price_color').text_content()[1:]
        rating = book_I.query_selector('p.star-rating').get_attribute('class')
        rate = ratingfun(rating.split()[1])

        book_info.append({
            'title':title,
            'price':price,
            'rating':rate
        })
    
    print(book_info)
    
    
    
    
    # v = page.query_selector_all('h3')
    # for title in v:
    #     book_info.append({
    #        'title': title.query_selector('a').get_attribute('title')
    #     })

    # print(book_info)
    
    browser.close()