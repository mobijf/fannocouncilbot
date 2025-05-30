import telebot

# جایگزین کردن توکن بات
TOKEN = "7890945064:AAG0ocXX9wbarqPMP-I9jff6Vz0j7bipZTw"
CHAT_ID = "8145564275"  # آیدی مقصد برای ارسال پیام‌ها

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! می‌تونی پیامت رو بنویسی تا برسونیم به شورا.")

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    user_info = bot.get_chat(message.chat.id)
    username = user_info.username if user_info.username else f"کاربر ناشناس ({message.chat.id})"
    
    bot.send_message(CHAT_ID, f"📩 پیام جدید از {username}:\n\n{message.text}")
    bot.reply_to(message, "پیامت به شورای صنفی فرستاده شد. مرسی از اعتمادت!")

print("ربات در حال اجراست...")
bot.polling()