import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    navegador.get("http://www.uol.com.br")

    wait = WebDriverWait(navegador, 10)

    valor_dolar = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/header/div[2]/div/div/a[1]/span[2]')
    )).text
    print(f"O dólar hoje vale: {valor_dolar}")

    valor_euro = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/header/div[2]/div/div/a[2]/span[2]')
    )).text
    print(f"O euro hoje vale: {valor_euro}")

    # Agora sim, abrir Gmail
    navegador.get("https://www.gmail.com")
    time.sleep(10)  # só para você ver a página

except Exception as e:
    print(f"Erro ao abrir o navegador: {e}")
    input("Pressione Enter para sair...")

