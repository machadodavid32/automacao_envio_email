from transformando_em_funcao import Emailer

email = Emailer('machado.david.developer@gmail.com', 'mtiqjlxrkrzhmdxn')

lista_contatos = ['machadodavid32@gmail.com', 'aline.silvaguedes@yahoo.com.br']
mensagem = """Testes personalizados e automatizados de email"""

email.definir_conteudo(topico="Seu pacote chegou", email_remetente='machado.david.developer@gmail.com',
                       lista_contatos=lista_contatos, conteudo_email=mensagem)

imagens = ['retro.jpg', 'bluesky.jpg']

email.anexar_imagem(imagens)

email.enviar_email(15)