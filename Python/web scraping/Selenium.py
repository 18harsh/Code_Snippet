from selenium import webdriver
browser = webdriver.Firefox(executable_path='C:\\geckodriver-v0.26.0-win64\\geckodriver.exe')
browser.get('https://automatetheboringstuff.com/')
elem =browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(20) > li:nth-child(1) > a')
elem.click()
elems = browser.find_element_by_css_selector('p')
print(elems.text)
searchElem = browser.find_element_by_css_selector('.search-field')
searchElem.send_keys('zophie')
searchElem.submit()
browser.back()
browser.forward()
browser.refresh()
browser.quit()
browser = webdriver.Firefox(executable_path='C:\\geckodriver-v0.26.0-win64\\geckodriver.exe')
browser.get('https://automatetheboringstuff.com/')
elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > p:nth-child(9)')
print(elem.text)


