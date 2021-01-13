from selenium import webdriver
import time

login_id = input("ID: ")
login_pw = input("PW: ")

driver = webdriver.Edge(executable_path='.../msedgedriver.exe')
driver.get("https://www.naver.com/")
time.sleep(3)

login_btn = driver.find_element_by_class_name("ico_naver")
login_btn.click()
time.sleep(3)



driver.execute_script("document.getElementsByName('id')[0].value=\'" + login_id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + login_pw + "\'")
driver.find_element_by_xpath('//*[@id="log.login"]').click()
