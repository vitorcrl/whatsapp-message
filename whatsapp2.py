import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caminho para seu convite em PDF
CAMINHO_PDF = "convite.pdf"

# Lê a planilha CSV
df = pd.read_csv("convidados.csv")

# Abre o WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione Enter para continuar...")

wait = WebDriverWait(driver, 30)  # espera até 30 segundos para os elementos aparecerem

for index, row in df.iterrows():
    nome = row['Nome']
    numero = f"+{row['DDI']}{row['DDD']}{row['Número de WhatsApp']}"

    mensagem = f"""Olá, {nome}!

Estamos muito felizes em compartilhar uma notícia maravilhosa: vamos nos casar! ✨

Deus tem sido bom conosco, e agora queremos celebrar esse momento abençoado ao lado de pessoas queridas como você.

Visite nosso site para todos os detalhes:
👉 https://sites.icasei.com.br/viana2025

Você também pode baixar o App do iCasei (https://icasei.app.link) e buscar por viana2025 para acompanhar as novidades, confirmar presença, enviar mensagens e fotos! 📸💌

Estamos contando os dias para viver esse sonho... e ele será ainda mais especial com a sua presença!

"Portanto, o que Deus uniu, ninguém o separe." (Marcos 10:9) ✨

Com carinho,
Ana & Vitor
"""

    driver.get(f"https://web.whatsapp.com/send?phone={numero}&text={mensagem}")
    
    try:
        # Espera até a caixa de mensagem aparecer
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @role="textbox"]')))
        
        input_box.send_keys(Keys.ENTER)
        time.sleep(5)

        # Envia o convite em PDF
        clip_button = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Anexar"]')))
        clip_button.click()
        time.sleep(1)

        file_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@accept="*"]')))
        file_input.send_keys(CAMINHO_PDF)
        time.sleep(2)

        send_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@data-icon="send"]')))
        send_button.click()
        time.sleep(5)

        print(f"Convite enviado para {nome}!")
    except Exception as e:
        print(f"Erro ao enviar para {nome}: {e}")

driver.quit()
print("Todos os convites foram enviados!")
