python
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from telegram import Bot

Dados do bot e da conta
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]  # opcional: pode ser fixo ou dinâmico
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

bot = Bot(token=BOT_TOKEN)

def enviar_mensagem(msg):
    try:
        bot.send_message(chat_id=CHAT_ID, text=msg)
    except Exception as e:
        print(f"Erro ao enviar mensagem: {e}")

def login_metroopinion():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.metroopinion.com/login")
        time.sleep(2)

        driver.find_element(By.NAME, "email").send_keys(EMAIL)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//button").click()
        time.sleep(4)

        if "dashboard" in driver.current_url:
            enviar_mensagem("✅ Login no MetroOpinion feito com sucesso (🇧🇷 PT / 🇺🇸 EN)")
        else:
