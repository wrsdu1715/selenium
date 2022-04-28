from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_binary


def get_store_name() :
    store_name = ''
    tmp = driver.find_elements(By.CSS_SELECTOR, '#rstdtl-head > div.rstdtl-header.unofficial > section > div.rdheader-title-data > div.rdheader-rstname-wrap > div.rdheader-rstname > h2 > span')
    if not tmp:
        tmp = driver.find_elements(By.CSS_SELECTOR, '#rstdtl-head > div.rstdtl-header > section > div.rdheader-title-data > div.rdheader-rstname-wrap > div.rdheader-rstname > h2 > a')
    if not tmp:
        tmp = driver.find_elements(By.CSS_SELECTOR, '#rstdtl-head > div.rstdtl-header > section > div.rdheader-title-data > div.rdheader-rstname-wrap > div.rdheader-rstname > h2 > span')
    store_name += tmp[0].text
    return store_name

def get_store_address():
    store_address = driver.find_element(By.CSS_SELECTOR, '#column-main > div.map-rstinfo > table > tbody > tr:nth-child(1) > td').text
    store_address_replace = store_address.replace(' ', '')
    return store_address_replace

def get_store_data():
    stores = driver.find_elements(By.CLASS_NAME, 'hyakumeiten-shop__item')
    for store in stores:
        store.find_element(By.TAG_NAME, 'a').click()
        time.sleep(8)
        driver.switch_to.window(driver.window_handles[-1]) # 別タブへ移動
        store_name = get_store_name()
        driver.find_element(By.CSS_SELECTOR, '#rdnavi-map > div > a').click()
        time.sleep(5)
        store_address = get_store_address()
        driver.close()
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0]) # 別タブへ移動


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://award.tabelog.com/hyakumeiten/ramen_east/2020")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'body > div.theme-hyakumeiten.theme-hyakumeiten--ramen.is-east > div.hyakumeiten-contents > div.hyakumeiten-main-frame > div.hyakumeiten-main.hyakumeiten-main--rstlst > div.hyakumeiten-main__contents > div.hyakumeiten-search > div.hyakumeiten-search__area.js-search-area').click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'body > div.theme-hyakumeiten.theme-hyakumeiten--ramen.is-east > div.hyakumeiten-contents > div.hyakumeiten-main-frame > div.hyakumeiten-main.hyakumeiten-main--rstlst > div.hyakumeiten-main__contents > div.hyakumeiten-search > div.hyakumeiten-search__area.js-search-area > div.hyakumeiten-search__trigger.hyakumeiten-search__trigger--area1 > div > div > div > a:nth-child(2)').click()
    time.sleep(3)
    get_store_data()
    driver.quit()