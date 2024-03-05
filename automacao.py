import pyautogui
import time
pyautogui.PAUSE = 2
import pandas

#entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("win")
pyautogui.write("google ch")
pyautogui.press("backspace")
pyautogui.press("enter")
time.sleep(5)
pyautogui.write(link)
pyautogui.press("enter")

#fazer login
pyautogui.press("tab")
pyautogui.write("joaozinho@dograu")
pyautogui.press("tab")
pyautogui.write("123485")
pyautogui.press("tab")
pyautogui.press("enter")
#importar base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)
#cadastrar 1 produto
#para cada linha da tabela
for linha in tabela.index:

    #codigo
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.click(x=538, y=315)
    pyautogui.write(codigo)
    #marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    #tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    #categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    #preco
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    #custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(+5000)
#repetir o processo de cadastro para os demais produtos