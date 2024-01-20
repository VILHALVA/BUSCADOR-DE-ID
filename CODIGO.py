import telebot

# Token do bot
token = "TOKEN_AQUI"

# Inicializa o bot
bot = telebot.TeleBot(token)

# Função para lidar com a mensagem /start
@bot.message_handler(commands=["start"])
def start(message):
    # Envia uma mensagem de boas-vindas e instruções de uso:
    bot.send_message(message.chat.id, "OLÁ! ESTE BOT EXIBIRÁ O ID DO CHAT DE UMA MENSAGEM ENCAMINHADA.\n PARA USAR O BOT, ENVIE UMA MENSAGEM ENCAMINHADA (COM CITAÇÃO) DE ALGUM GRUPO OU CANAL.")

# Função para lidar com mensagens encaminhadas
@bot.message_handler(content_types=["text", "photo", "video", "audio", "document", "sticker", "voice"])
def mensagem_encerrada(message):
    # Verifica se a mensagem é encaminhada
    if message.forward_from_chat:
        # Obtém o id do chat da mensagem original
        id_chat = message.forward_from_chat.id
        # Envia a mensagem com o id do chat
        bot.reply_to(message, "<b>ID DO CHAT:\n</b><code>{}</code>".format(id_chat), parse_mode="html")
    else:
        bot.reply_to(message, "🤬ERRO: NÃO CONSEGUIR ENCONTRAR O ID. PODE ER POR UM DESSES DOIS MOTIVOS:\n1️⃣ESTA MENSAGEM NÃO FOI ENCAMINHADA COM CITAÇÃO.\n2️⃣VOCÊ ESTÁ TENTANDO ENCAMINHAR MENSAGEM PRIVADA DE USUÁRIO.")

# Inicia o bot
bot.polling()
