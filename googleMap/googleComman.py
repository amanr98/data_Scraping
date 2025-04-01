
def googleload(page,screenshot = '',timeout = 2000):
    page.wait_for_load_state('domcontentloaded')
    page.wait_for_timeout(timeout)

    if screenshot != '':
        page.screenshot(path =f'{screenshot}.png',full_page =True)