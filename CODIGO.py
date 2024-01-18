import telebot

# Token do bot
token = "TOKEN_DO_BOT"

# Inicializa o bot
bot = telebot.TeleBot(token)

# Função para lidar com a mensagem /start
@bot.message_handler(commands=["start"])
def start(message):
    # Envia uma mensagem de boas-vindas
    bot.send_message(message.chat.id, "Olá! Este bot exibirá o id do chat de uma mensagem encaminhada.")
    # Envia instruções de uso
    bot.send_message(message.chat.id, "Para usar o bot, envie uma mensagem encaminhada de algum grupo ou canal.")

# Função para lidar com mensagens encaminhadas
@bot.message_handler(content_types=["text", "photo", "video", "audio", "document", "sticker", "voice"])
def mensagem_encerrada(message):
    # Obtém o id do chat da mensagem original
    id_chat = message.chat.id
    # Envia a mensagem com o id do chat
    bot.send_message(id_chat, "ID do chat: -{}".format(message.chat.id))

# Inicia o bot
bot.polling()
