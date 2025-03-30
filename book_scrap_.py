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

"""-------------------------------------------OUTPUT---------------------------------
[{'title': 'A Light in the Attic', 'price': '51.77', 'rating': 3}, {'title': 'Tipping the Velvet', 'price': '53.74', 'rating': 1}, {'title': 'Soumission', 'price': '50.10', 'rating': 1}, {'title': 'Sharp Objects', 'price': '47.82', 'rating': 4}, {'title': 'Sapiens: A Brief History of Humankind', 'price': '54.23', 'rating': 5}, {'title': 'The Requiem Red', 'price': '22.65', 'rating': 1}, 
{'title': 'The Dirty Little Secrets of Getting Your Dream Job', 'price': '33.34', 'rating': 4}, {'title': 'The Coming Woman: A Novel Based on the Life of the Infamous Feminist, Victoria Woodhull', 'price': '17.93', 'rating': 3},
{'title': 'The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics', 'price': '22.60', 'rating': 4}, {'title': 'The Black Maria', 'price': '52.15', 'rating': 1}, {'title': 'Starving Hearts (Triangular Trade Trilogy, #1)', 'price': '13.99', 'rating': 2},
{'title': "Shakespeare's Sonnets", 'price': '20.66', 'rating': 4}, {'title': 'Set Me Free', 'price': '17.46', 'rating': 5}, {'title': "Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)", 'price': '52.29', 'rating': 5}, {'title': 'Rip it Up and Start Again', 'price': '35.02', 'rating': 5},
{'title': 'Our Band Could Be Your Life: Scenes from the American Indie Underground, 1981-1991', 'price': '57.25', 'rating': 3}, {'title': 'Olio', 'price': '23.88', 'rating': 1}, {'title': 'Mesaerion: The Best Science Fiction Stories 1800-1849', 'price': '37.59', 'rating': 1}, {'title': 'Libertarianism for Beginners', 'price': '51.33', 'rating': 2},
{'title': "It's Only the Himalayas", 'price': '45.17', 'rating': 2}]
"""
