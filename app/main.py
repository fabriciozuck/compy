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
    search = "//input[@class='nav-search-input']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")

elif site == 2:
    link = "https://pt.aliexpress.com/"
    search = "//input[@class='search-key']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")

else:
    print("Você não selecionou nenhuma das opções.")
    quit()


drive = webdriver.Chrome(executable_path=os.getcwd()+os.sep + "driver/chromedriver")
drive.get(link)

campo_pesquisa = drive.find_element_by_xpath(search)

campo_pesquisa.click()
campo_pesquisa.send_keys(prod)
campo_pesquisa.send_keys(Keys.ENTER)
