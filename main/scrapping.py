import time
import requests

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver = '/home/guilherme-gso/tmp/chromedriver'
x_path = '//div[@class="leaflet-content col-xs-12 col-sm-8 col-sm-offset-2 marginTop-20"]'

def scrap(remedy):
  url = f'https://consultaremedios.com.br/{remedy}/bula'

  option = Options()
  driver = webdriver.Chrome(chromedriver)
  driver.get(url)

  element = driver.find_element_by_xpath(x_path)
  html = element.get_attribute('outerHTML')
  soup = BeautifulSoup(html, 'html.parser')
  paragraph = soup.find(class_='marginBottom-30 leaflet-content__text')

  return paragraph.get_text()


