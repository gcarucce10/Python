import os
import smtplib
from email.message import EmailMessage
from private import senha

# LOGAR NO EMAIL
EMAIL_ADDRESS = 'gabriel.carucce@unesp.br'
EMAIL_PASSWORD = senha

# CRIAR MENSAGEM
msg = EmailMessage()
msg['Subject'] = 'Teste de email'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'lucascamaro14@gmail.com'
msg.set_content('Olá, Lu! Você parece um pouco introspectivo hoje...')

# ENVIO
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)