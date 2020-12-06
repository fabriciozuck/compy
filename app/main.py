from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

print("---------------------")
print("BEM VINDO AO COMPY!!!")
print("---------------------")
print("(1) Mercado Livre")
print("(2) Ali Express")
print("")
site = int(input("-> Escolha o site que você quer pesquisar: "))

if site == 1:
    link = "https://mercadolivre.com.br"
    prod = input("-> Digite o nome do produto que deseja pesquisa: ")
elif site == 2:
    link = "https://pt.aliexpress.com/"
    prod = input("-> Digite o nome do produto que deseja pesquisa: ")
else:
    print("Você não selecionou nenhuma das opções.")


drive = webdriver.Chrome(executable_path=os.getcwd()+os.sep + "driver/chromedriver")
drive.get(link)

campo_pesquisa = drive.find_element_by_xpath("//input[@class='nav-search-input']")

campo_pesquisa.click()
campo_pesquisa.send_keys(prod)
campo_pesquisa.send_keys(Keys.ENTER)
