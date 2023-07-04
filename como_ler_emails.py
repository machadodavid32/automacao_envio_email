# Necessário instalar a biblioteca rich com pip install rich no terminal.

from imapclient import IMAPClient
from datetime import datetime, date
import email
from rich import print

# configurações de login
HOST = 'imap.gmail.com'
USERNAME = 'machado.david.developer@gmail.com'
PASSWORD = 'mtiqjlxrkrzhmdxn'


# Abrir conexão com gmail

with IMAPClient(HOST) as server:
    server.login(USERNAME, PASSWORD)
    print(server.list_folders())  # vai mostrar as pastas disponíveis para leitura.
    # Neste momento, ao colocar o programa para rodar, no terminal vai aparecer..
    # o nome das pastas em uma tupla. Vamos escolher a pasta 'INBOX' 
    server.select_folder('INBOX', readonly=True)
    
    # pesquisa(filtrar emails) neste caso abaixo por datas. Mas existe outros...
    # filtros na documentação do imapclient
    messages = server.search(
        [u'SINCE', date(datetime.now().year, datetime.now().month, datetime.now().day)])
    
    for uid, message_data in server.fetch(messages, 'RFC822').items():
        email_message = email.message_from_bytes(message_data[b'RFC822'])
        print(f'id: {uid}')
        print(f'FROM: {email_message.get("From")}')
        print(f'TÓPICO: {email_message.get("Subject")}')
        if email_message.is_multipart():  # multipart são aqueles emails que são encaminhados mais de uma vez, quando a pessoa manda varios.
            for part in email_message.walk():
                if part.get_content_type() in ('text/plain', 'text/html'): # Aqui para caso o email seja em qualquer um desses dois tipos eu consigo ler
                    try:
                        print(part.get_payload(decode=True).decode())
                    except UnicodeDecodeError as erro:  # aqui é para alguns momentos em que há erro de codificação por caracteres especiais.
                        print(part.get_payload(decode=True).decode('latin-1'))
                        
                        
     
     # get_payload - comando para extrair os dados
     # decode=True.decode() decodificar os dados extraídos.                   
                            