import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector(".btn-add-to-basket") == True, "Wrong language"

