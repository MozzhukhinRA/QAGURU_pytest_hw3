from selene import browser, have

def test_fiend_quest(option_browser, opening_browser):
    browser.element('[id="text"]').type('qaguru').press_enter()
    print("Test completed")

def test_search_link_stuff(option_browser, opening_browser):
    browser.element('[id="text"]').type('trhurtmgerwumgrtuijmhtyiujmiougmetriohmrt').press_enter()
    browser.element('[class="EmptySearchResults-Title"]').should(have.text('Ничего не нашли'))
    print("Test completed")
