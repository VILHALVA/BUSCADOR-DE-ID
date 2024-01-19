import telebot

# Token do bot
token = "TOKEN_AQUI"

# Inicializa o bot
bot = telebot.TeleBot(token)

# Função para lidar com a mensagem /start
@bot.message_handler(commands=["start"])
def start(message):
    # Envia uma mensagem de boas-vindas e instruções de uso:
    bot.send_message(message.chat.id, "Olá! Este bot exibirá o id do chat de uma mensagem encaminhada.\n Para usar o bot, envie uma mensagem encaminhada (Com citação) de algum grupo ou canal.")

# Função para lidar com mensagens encaminhadas
@bot.message_handler(content_types=["text", "photo", "video", "audio", "document", "sticker", "voice"])
def mensagem_encerrada(message):
    # Obtém o id do chat da mensagem original
    id_chat = message.chat.id
    # Envia a mensagem com o id do chat
    bot.reply_to(message, "<b>ID DO CHAT:\n</b><code>-{}</code>".format(id_chat), parse_mode="html")

# Inicia o bot
bot.polling()
