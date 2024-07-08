import telebot
from TOKEN import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "OLÁ! ESTE BOT EXIBIRÁ O ID DO CHAT DE UMA MENSAGEM ENCAMINHADA.\n PARA USAR O BOT, ENVIE UMA MENSAGEM ENCAMINHADA (COM CITAÇÃO) DE ALGUM GRUPO OU CANAL.")

@bot.message_handler(content_types=["text", "photo", "video", "audio", "document", "sticker", "voice"])
def mensagem_encerrada(message):
    if message.forward_from_chat:
        id_chat = message.forward_from_chat.id
        bot.reply_to(message, "<b>ID DO CHAT:\n</b><code>{}</code>".format(id_chat), parse_mode="html")
    else:
        bot.reply_to(message, "🤬ERRO: NÃO CONSEGUIR ENCONTRAR O ID. PODE ER POR UM DESSES DOIS MOTIVOS:\n1️⃣ESTA MENSAGEM NÃO FOI ENCAMINHADA COM CITAÇÃO.\n2️⃣VOCÊ ESTÁ TENTANDO ENCAMINHAR MENSAGEM PRIVADA DE USUÁRIO.")

bot.polling()
