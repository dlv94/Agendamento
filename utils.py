from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def iniciar_driver():
    options = Options()
    # options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 4)
    driver.maximize_window()
    return driver, wait


def aguardar_horario(inicio):
    if inicio == "07h59m":
        while True:
            agora = datetime.now()
            if agora.hour > 7 or (agora.hour == 7 and agora.minute == 59 and agora.second > 20):
                print("Horário atingido. Iniciando agendamento!")
                break
            else:
                print(f"Aguardando 07:59... Agora são {agora:%H:%M:%S}")
                sleep(10)
