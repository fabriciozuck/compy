from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

print('')
print('BEM VINDO AO COMPY!!!')
print('')
prod = input('-> Digite o nome do produto que deseja pesquisa: ')

drive = webdriver.Chrome(executable_path=os.getcwd()+os.sep + "/chrome/chromedriver")
drive.get("https://mercadolivre.com.br")

campo_pesquisa = drive.find_element_by_xpath("//input[@class='nav-search-input']")

campo_pesquisa.click()
campo_pesquisa.send_keys(prod)
campo_pesquisa.send_keys(Keys.ENTER)
