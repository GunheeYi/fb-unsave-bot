# Android environment
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome('chromedriver', options=chrome_options)

driver.get("https://facebook.com")
driver.find_element(By.NAME, 'email').send_keys('ENTER YOUR EMAIL HERE') # ENTER YOUR EMAIL HERE
driver.find_element(By.NAME, 'pass').send_keys('ENTER YOUR PASSWORD HERE') # ENTER YOUR PASSWORD HERE
driver.find_element(By.NAME, 'login').click()
time.sleep(5)
driver.get("https://www.facebook.com/saved")
time.sleep(3)

while True:
    time.sleep(0.5)
    unsaves = driver.find_elements(By.CLASS_NAME, "sx_1b9265")
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(unsaves[0], 5, 5)
    action.click()
    action.perform()
    time.sleep(0.5)

    els = driver.find_elements(By.CLASS_NAME, "hzawbc8m")
    for el in els:
        if el.get_attribute("innerHTML")=="Unsave":
            el.click()
