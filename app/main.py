from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

print("---------------------")
print("BEM VINDO AO COMPY!!!")
print("---------------------")
print("(1) Mercado Livre")
print("(2) Ali Express")
print("(3) Lojas Americanas")
print("(4) Amazon")
print("(5) Magazine Luiza")
print("(6) Kabum")
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
    link = "https://www.amazon.com.br/"
    search = "//input[@class='nav-input']"

elif site == 5:
    link = "https://www.magazineluiza.com.br/"
    search = "//input[@class='field-input-search ui-autocomplete-input']"

elif site == 6:
    link = "https://www.kabum.com.br/"
    search = "//input[@class='sprocura']"

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

# try:
#     list_prod = drive.find_elements_by_xpath("//h2[@class='ui-search-item__group__element']")
# except:
#     print("Não trabalhamos com thumbnail")


try:
    list_prod = drive.find_elements_by_xpath("//h2[@class='ui-search-item__title ui-search-item__group__element']")
    list_prod2 = drive.find_elements_by_xpath("//h2[@class='ui-search-item__title']")
except:
    pass    

if list_prod:
   for prod in list_prod:
       print(prod.text)
elif list_prod2:
     for prod in list_prod2:
         print(prod.text)