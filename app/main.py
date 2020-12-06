from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

print("---------------------")
print("BEM VINDO AO COMPY!!!")
print("---------------------")
print("(1) Mercado Livre")
print("(2) Ali Express")
print("(3) Lojas Americanas")
print("(4) Casas Bahia")
print("")
site = int(input("-> Escolha o site que você quer pesquisar: "))

if site == 1:
    link = "https://mercadolivre.com.br"
    search = "//input[@class='nav-search-input']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")

elif site == 2:
    link = "https://pt.aliexpress.com/"
    search = "//input[@id='search-key']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")

elif site == 3:
    link = "https://www.americanas.com.br/"
    search = "//input[@class='src-input']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")

elif site == 4:
    link = "https://www.casasbahia.com.br/"
    search = "//input[@id='strBusca']"

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

try:

    list_prod = drive.find_elements_by_xpath("//h2[@class='ui-search-item__title ui-search-item__group__element']")


except:
    print("Não trabalhamos com thumbnail")

try:
    drive.find_elements_by_xpath("//h2[@class='ui-search-item__title']")
except:
    print("Não estamos no formato listagem")

for prod in list_prod:
    print(list_prod)












# listagem
# //h2[@class="ui-search-item__title"]


# tubnail 
# //h2[@class='ui-search-item__title ui-search-item__group__element']