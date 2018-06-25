from selenium import webdriver

doodle=webdriver.Chrome('D:\\selenium\\webdriver\\chromedriver_win32\\chromedriver.exe')

doodle.get('https://www.facebook.com/')
doodle.maximize_window()
doodle.get_screenshot_as_file('D:\\facebook1.png')
doodle.find_element_by_id('email').send_keys('zubairkhan84@gmail.com')
doodle.find_element_by_id('pass').send_keys('fire@1234')
print(doodle.title)
assert "Facebook" in doodle.title #assert caputured heading shown in url
doodle.find_element_by_id('loginbutton').click()
doodle.implicitly_wait(1)
doodle.quit()


