from selenium import webdriver
from selenium.webdriver.common.by import By


def test_simple():
    wb = webdriver.Chrome()
    wb.get('https://www.mvideo.ru/')
    wb.quit()
