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
    bURl = 'https://books.toscrape.com/catalogue/'
    page.goto(bURl + "page-1.html")

    # v=0
    # while True:
    #     next_button = page.query_selector(".next a")
    #     v=v+1
    #     if not next_button:
    #         break  # No more pages, stop looping
    #     next_page_url = next_button.get_attribute("href") 
    #     page.goto(bURl + next_page_url)
    # print(v)


    while True :
        books = page.query_selector_all('.product_pod')
        
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

            print(print(f"Title: {title}, Price: {price}, Rating: {rate}"))
        
        next_button = page.query_selector(".next a")

        if not next_button:
            break;
        
        next_page_url = next_button.get_attribute("href") 

        page.goto(bURl + next_page_url)
    print(book_info)
    browser.close()