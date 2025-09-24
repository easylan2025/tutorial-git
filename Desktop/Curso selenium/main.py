import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


navegador = webdriver.Chrome()

navegador.get("https://www.hashtagtreinamentos.com/")

navegador.maximize_window()

time.sleep(7)


try:
    pop_up = navegador.find_element(By.ID, "botaoPopupFechar")
    pop_up.click()
    print("Popup fechado com sucesso.")
except:
    print("Nenhum popup encontrado, continuando...")

try:
    botao_verde = navegador.find_element(By.CLASS_NAME, "botao-verde")
    botao_verde.click()
    print("Botão verde clicado, tarefa concluída.")
except:
    print("Botão verde não encontrado.")

time.sleep(500)  # mantém o navegador aberto
