
import smtplib
from email.message import EmailMessage
from time import sleep

# Configurações de login

EMAIL_ADDRESS = 'machado.david.developer@gmail.com'
EMAIL_PASSWORD = 'mtiqjlxrkrzhmdxn'
contatos = ['machadodavid32@gmail.com', 'aline.silvaguedes@yahoo.com.br']

# Criar e enviar um email

mail = EmailMessage()

mail['Subject'] = 'Seu pacote chegou nos correios'

mensagem = """
Olá, seu pacote acaba de chegar nos correios. Favor ir buscar até amanhã.
Seu código de rastreio é XV3345CVV

"""

mail['From'] = EMAIL_ADDRESS
mail['To'] = ', '.join(contatos)  # Está juntando a virgula e espaço para separar os emails.
mail.add_header('Content-Type', 'text/html')  # define se é somente texto, se tem html
mail.set_payload(mensagem.encode('utf-8'))  # define o que será inserido no email. No caso, a sua mensagem.

# Enviar o email:
for contato in contatos:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:    #criando uma conexão segura
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        email.send_message(mail)
        sleep(10)
    
 # Aqui > 'smtp.gmail.com', 465   < é o servidor smtp e nome do gmail. Caso queira configurar outro email, é só procurar por...
 # servidor smpt e nome do yahoo, outlook, etc...
 