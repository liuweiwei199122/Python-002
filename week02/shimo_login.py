from selenium import webdriver
import time
wb = webdriver.Chrome()
url = 'https://shimo.im'
wb.get(url)
#/html/body/div[1]/div[1]/header/nav/div[3]/a[2]/button
#//*[@id="homepage-header"]/nav/div[3]/a[2]/button
wb.find_element_by_xpath('//button[@class="login-button btn_hover_style_8"]').click()
time.sleep(1)
wb.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys('15001799836')
time.sleep(1)
wb.find_element_by_xpath('//input[@name="password"]').send_keys('069666')
time.sleep(1)
wb.find_element_by_xpath('//button[@type="black"]').click()