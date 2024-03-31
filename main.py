import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data():
    data = pd.read_csv(
        'https://docs.google.com/spreadsheets/d/e/2PACX-1vTfPNHNf8pRVEIs4veXJrC3AZ4w_GvxxpRbanOaHJsO3XZRFfSQxMOZ_7JLN22-uA/pub?output=csv',
        )
    print(data)
    return data


def main():
    driver = webdriver.Chrome()
    for row in get_data().itertuples(index=False):
        nick = row[0]
        prom = row[1]
        link = row[2]
        driver.get(link)
        time.sleep(4)
        form = driver.find_element(By.XPATH, "//form[1]")
        fields = form.find_elements(By.CSS_SELECTOR, "input")
        fields[0].send_keys(prom)
        fields[1].send_keys(nick)
        button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        button.click()
        strUrl = driver.current_url
        while 'success' not in strUrl:
            strUrl = driver.current_url


if __name__ == '__main__':
    main()
