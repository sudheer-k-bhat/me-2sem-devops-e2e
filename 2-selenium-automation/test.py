from selenium.webdriver import Chrome

class TestSuite:

    def test_one(self):
        browser = Chrome('/usr/local/bin/chromedriver')
        browser.get('https://duckduckgo.com')

        search_form = browser.find_element_by_id('search_form_input_homepage')
        search_form.send_keys('real python')
        search_form.submit()

        results = browser.find_elements_by_class_name('result')
        assert 'https://realpython.com' in results[0].text

        browser.close()