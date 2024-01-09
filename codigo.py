# Passo a passo do projeto de automação

import pyautogui
import time

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# 1 - Apertar o windows

pyautogui.PAUSE = 1.2 #comando para dar um intervalo entre os comandos do pyautogui, para que não haja problema caso o sistema trave
pyautogui.press("win")

# 2 - Procurar e abrir o chrome

pyautogui.write("chrome")
pyautogui.press("enter")

# 3 - Acessar o site especificado

pyautogui.write(link)
pyautogui.press("enter")

# 4 - Fazer login

time.sleep(3.5) #comando que da um intervalo especifico para o comando logo abaixo
pyautogui.click(x=563, y=353)
pyautogui.write("emaildeacesso@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhadeacesso")
pyautogui.press("tab")
pyautogui.press("enter")

# 5 - Importar a base de dados

import pandas

tabela = pandas.read_csv("produtos.csv")

# 6 - Cadastrar um produto e repetir o processo até que os items dentro da tabela acabem

for linha in tabela.index:

    time.sleep(2.5)
    pyautogui.click(x=712, y=257)

    #código do produto
    pyautogui.write(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    #marca do produto
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    #tipo do produto
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    #categoria do produto
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    #preço unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    #custo do produto
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #o comando panda.isna verifica se o valor informado é vazio
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    
    #enviar produto
    pyautogui.press("enter")
    pyautogui.scroll(5000)
