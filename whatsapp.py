import time
import pandas as pd
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Lê a planilha CSV
df = pd.read_csv("convidados.csv")

# Configurações do Chrome
options = Options()
driver = webdriver.Chrome(options=options)

# Abre o WhatsApp Web
driver.get("https://web.whatsapp.com")
input("Confirme que o WhatsApp Web já carregou e pressione Enter...")

for index, row in df.iterrows():
    nome = row['Nome']
    numero = f"+{row['DDI']}{row['DDD']}{row['Número de WhatsApp']}"

    mensagem = f"""Olá, {nome} e família!

Estamos muito felizes em compartilhar uma notícia maravilhosa: vamos nos casar! ✨

Deus tem sido bom conosco, e agora queremos celebrar esse momento abençoado ao lado de pessoas queridas como vocês.

Visite nosso site para todos os detalhes:
👉 https://sites.icasei.com.br/viana2025

Você também pode baixar o App do iCasei (https://icasei.app.link) e buscar por viana2025 para acompanhar as novidades, confirmar presença, enviar mensagens e fotos! 📸💌

Estamos contando os dias para viver esse sonho... e ele será ainda mais especial com a sua presença!

"Portanto, o que Deus uniu, ninguém o separe." (Marcos 10:9) ✨

Com carinho,
Ana & Vitor
"""

    # Codifica a mensagem para manter quebras de linha
    mensagem_encoded = urllib.parse.quote(mensagem)

    # Abre a conversa
    driver.get(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem_encoded}")
    time.sleep(15)  # Dá tempo pra abrir e carregar bem

    try:
        # Dá ENTER para enviar a mensagem
        input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true" and @role="textbox"]')
        input_box.send_keys(Keys.ENTER)
        time.sleep(30)

        print(f"Convite enviado para {nome}!")
    except Exception as e:
        print(f"Erro ao enviar para {nome}: {e}")

driver.quit()
print("Todos os convites foram enviados!")
