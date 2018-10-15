import telegram

my_token = '565712291:AAHqK7gvHtQ5WKmvfAFBzKb1_sLp7Q_rL24'

bot = telegram.Bot(token= my_token)

updates = bot.getUpdates()
chat_id = bot.getUpdates()[-1].message.chat.id


bot.sendMessage(chat_id=chat_id, text='새 글이 올랑모')
bot.sendMessage(chat_id=chat_id, text=str(updates))