from bs4 import BeautifulSoup as bs
restro_list = []


def googleHtml(innerhtml):
    bodypage = bs(innerhtml,'html.parser')

    # main heading 
    r_name = bodypage.select_one('h1.DUwDvf').text
    # sub heading
    r_name1 = bodypage.select_one('h2.bwoZTb')
    if r_name1:
        r_name1 = r_name1.text
    else:
        r_name1 = 'Not Available'

    # starting reviews stars
    headStart = bodypage.select_one('div.F7nice > span').text
    # starting reviews
    headRevies = bodypage.select_one('span[aria-label*="reviews"]').text

    # restaurant  type
    r_Type = bodypage.select_one('button.DkEaL').text
    # about 
    r_About = bodypage.select_one('div.PYvSYb')
    if r_About:
        r_About = r_About.text
    else:
        r_About = 'Not Available'


    # r_About1 = bodypage.select_one('div.E0DTEd').text.replace('\ue5ca','')
    # dine or not
    dineIn = bodypage.select_one('div[aria-label*="dine-in"]')
    if dineIn:
        dineIn = dineIn.text.replace('\ue5ca','')
    else:
        dineIn = 'Not Available'

    # take away/ drive through or not
    drive_through = bodypage.select_one('div[aria-label*="drive-through"]')
    take_away= bodypage.select_one('div[aria-label*="takeaway"]')

    if take_away:
        take_away = take_away.text.replace('\ue5ca','')
    elif drive_through:
        take_away = drive_through.text.replace('\ue5ca','')
    else:
        take_away = 'Not Available'
        
    # location 
    location = bodypage.select_one('div.Io6YTe').text

    # price range reported by people 
    price_range = bodypage.find(string=lambda text: text and '₹' in text)
    if price_range:
        print(f"{price_range.strip()} per person")
    
    # price suggest by people
    reported_by_people = bodypage.select_one('div.BfVpR')
    if reported_by_people:
        reported_by_people = reported_by_people.text

    price_range_people ={
        'price_range':price_range,
        'reported_by_people':reported_by_people
    }

    # restro infromation
    restro_list.append({
        'name':r_name,
        'name1':r_name1,
        'starts':headStart,
        'reviews':headRevies,
        'restaurant type':r_Type,
        'about':r_About,
        'serves type':dineIn,
        'take away':take_away,
        'loacation':location,
        'price range by people':price_range_people
    })

    print(restro_list)
