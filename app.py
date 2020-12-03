from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

drive = webdriver.Chrome(executable_path=os.getcwd()+os.sep + "chromedriver")
drive.get("https://mercadolivre.com.br")

campo_pesquisa = drive.find_element_by_xpath("//input[@class='nav-search-input']")

campo_pesquisa.click()
campo_pesquisa.send_keys("Fone Gamer Razer")
campo_pesquisa.send_keys(Keys.ENTER)
try:
    pass
except expression as identifier:
    pass
else:
    pass
