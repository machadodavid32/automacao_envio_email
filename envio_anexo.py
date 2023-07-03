import smtplib
from email.message import EmailMessage
import imghdr  # este faz reconhecer anexos de imagens


# Configurações de login

EMAIL_ADDRESS = 'machado.david.developer@gmail.com'
EMAIL_PASSWORD = 'mtiqjlxrkrzhmdxn'

# Criar e enviar um email

mail = EmailMessage()

mail['Subject'] = 'arquivos em anexos'

mensagem = """
Olá, seu pacote acaba de chegar nos correios. Favor ir buscar até amanhã.
Seu código de rastreio é XV3345CVV

"""

mail['From'] = EMAIL_ADDRESS
mail['To'] = 'machadodavid32@gmail.com'
mail.add_header('Content-Type', 'text/html')  # define se é somente texto, se tem html
mail.set_payload(mensagem.encode('utf-8'))  # define o que será inserido no email. No caso, a sua mensagem.

# Anexar arquivos
imagens = ['bluesky.jpg', 'retro.jpg']
"""Obs: Caso as imagens não estejam na mesma pasta do projeto, temos que colocar o caminho de origem com duas barras.
Exemplo: imagens = ['C:\\Users\\cliente\\Desktop\\python\\automacaopython']"""
for imagem in imagens:
    with open(imagem, 'rb') as arquivo:
        dados = arquivo.read()
        extensao_imagem = imghdr.what(arquivo.name)
        nome_arquivo = arquivo.name
        mail.add_attachment(dados, maintype='image',
                            subtype=extensao_imagem, filename=nome_arquivo)


# Anexar qualquer tipo de arquivo (que não seja imagem)

arquivos = ['csv_exemplo.csv', 'exemplo_word.docx',
            'ExemploPlanilha.xlsx', 'PDF_Exemplo.pdf', 'Untitled presentation.pptx']

for arquivo in arquivos:
    with open(arquivo, 'rb') as arquivo:
        dados = arquivo.read()
        nome_arquivo = arquivo.name
        mail.add_attachment(dados, maintype='application',
                            subtype='octet-stream', filename=nome_arquivo)        

# Enviar o email:
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:    #criando uma conexão segura
    email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    email.send_message(mail)
    
 # Aqui > 'smtp.gmail.com', 465   < é o servidor smtp e nome do gmail. Caso queira configurar outro email, é só procurar por...
 # servidor smpt e nome do yahoo, outlook, etc...
 