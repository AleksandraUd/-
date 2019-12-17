link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser, request):
	browser.get(link)
	button = browser.find_elements_by_css_selector(".btn-add-to-basket")
	assert len(button)>0, 'There is no button'