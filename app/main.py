from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import platform

so = platform.system()

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
    list_prod = "//h2"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")
elif site == 2:
    link = "https://pt.aliexpress.com/"
    search = "//input[@id='search-key']"
    list_prod = "//a[@class='item-title']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")
elif site == 3:
    link = "https://www.americanas.com.br/"
    search = "//input[@class='src-input']"
    list_prod = "//span[@class='src__Text-sc-154pg0p-0 src__Name-sc-1di8q3f-3 fLqTUE']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")
elif site == 4:
    link = "https://www.amazon.com.br/"
    search = "//input[@class='nav-input']"
    list_prod = "//span[@class='a-size-base-plus a-color-base a-text-normal']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")
elif site == 5:
    link = "https://www.magazineluiza.com.br/"
    search = "//input[@class='field-input-search ui-autocomplete-input']"
    list_prod = "//h3[@class='productTitle']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")
elif site == 6:
    link = "https://www.kabum.com.br/"
    search = "//input[@class='sprocura']"
    list_prod = "//a[@class='sc-fzoLsD gnrNhT item-nome']"

    prod = input("-> Digite o nome do produto que deseja pesquisa: ")
else:
    print("Você não selecionou nenhuma das opções.")
    quit()

if so == 'Linux':
    drive = webdriver.Chrome(executable_path=os.getcwd()+os.sep + "app/driver/chromedriver")
elif so == 'Windows':
    drive = webdriver.Chrome(executable_path=os.getcwd()+os.sep + "app/driver/winchromedriver.exe")
elif so == 'Darwin':
    drive = webdriver.Chrome(executable_path=os.getcwd()+os.sep + "app/driver/chromedriveros")
else:
    print('Sistema Operacional não identificado.')

drive.get(link)

field = drive.find_element_by_xpath(search)
field.click()
field.send_keys(prod)
field.send_keys(Keys.ENTER)

items = drive.find_elements_by_xpath(list_prod)

for prod in items:
    print(prod.text)
