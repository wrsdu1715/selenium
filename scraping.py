from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import chromedriver_binary
driver = webdriver.Chrome()
driver.get("https://award.tabelog.com/hyakumeiten/ramen_east/2020?pref=gifu")
driver.find_element(By.CSS_SELECTOR, 'body > div.theme-hyakumeiten.theme-hyakumeiten--ramen.is-east > div.hyakumeiten-contents > div.hyakumeiten-main-frame > div.hyakumeiten-main.hyakumeiten-main--rstlst > div.hyakumeiten-main__contents > div.hyakumeiten-shop.js-floating-btn-visible > div.hyakumeiten-shop__list > div > a').click()
time.sleep(10)
driver.switch_to.window(driver.window_handles[-1]) # 別タブへ移動
store_name = driver.find_element(By.XPATH, '//*[@id="rstdtl-head"]/div[1]/section/div[1]/div[1]/div[1]/h2/span').text
driver.find_element(By.CSS_SELECTOR, '#rdnavi-map > div > a').click()
time.sleep(10)
store_address = driver.find_element(By.CSS_SELECTOR, '#column-main > div.map-rstinfo > table > tbody > tr:nth-child(1) > td').text
store_address_replace = store_address.replace(' ', '')
print(store_address_replace)
driver.quit()