import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Removido o caminho para o PDF

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
    mensagem = f"""Olá, {nome}! Estamos muito felizes em compartilhar uma notícia maravilhosa: vamos nos casar! 

Deus tem sido bom conosco, e agora queremos celebrar esse momento abençoado ao lado de pessoas queridas como você.

Visite nosso site para todos os detalhes:
https://sites.icasei.com.br/viana2025

Você também pode baixar o App do iCasei (https://icasei.app.link) e buscar por viana2025 para acompanhar as novidades, confirmar presença, enviar mensagens e fotos!

Estamos contando os dias para viver esse sonho... e ele será ainda mais especial com a sua presença!

"Portanto, o que Deus uniu, ninguém o separe." (Marcos 10:9)

Com carinho,
Ana & Vitor"""
    
    print(f"\n{'='*50}")
    print(f"Preparando mensagem para: {nome} ({numero})")
    print(f"{'='*50}")
    
    # Abre a conversa com o contato
    driver.get(f"https://web.whatsapp.com/send?phone={numero}")
    
    try:
        # Espera até a caixa de mensagem aparecer (é importante aguardar o carregamento completo)
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@title="Digite uma mensagem" or @title="Type a message"]')))
        
        # Limpa qualquer texto existente e insere a mensagem linha por linha para evitar problemas
        input_box.click()  # Garantir que o foco está no campo certo
        for linha in mensagem.split('\n'):
            input_box.send_keys(linha)
            input_box.send_keys(Keys.SHIFT + Keys.ENTER)  # Adiciona quebra de linha sem enviar
        
        print("\nMensagem pronta para envio.")
        # Enviar a mensagem após confirmação do usuário
        acao = input("Pressione Enter para enviar a mensagem ou digite 'pular' para ir ao próximo contato, ou 'sair' para encerrar: ")
        
        if acao.lower() == 'sair':
            break
        elif acao.lower() == 'pular':
            print(f"Pulando {nome}...")
            continue
        
        # O usuário pressionou Enter para enviar
        print(f"Enviando mensagem para {nome}...")
        
        # Enviar a mensagem
        input_box.send_keys(Keys.ENTER)
        
        print(f"Mensagem enviada para {nome}!")
        
    except Exception as e:
        print(f"Erro ao processar {nome}: {e}")
        input("Pressione Enter para continuar com o próximo contato...")

print("\nProcessamento finalizado!")
driver.quit()