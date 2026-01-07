import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

paid_users = set()

TARGET_CHANNEL_ID = '@babichtgc'

@bot.message_handler(commands=['start']) # command /start
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("Message to @babichtgc"))
    bot.send_message(message.chat.id,
                     f"Hello, {message.from_user.first_name}! I'm babich telegram bot. Made by @babichtgc\n\nPrint /help to see available commands",
                     reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Message to @babichtgc":
        send_payment(message)
    else:
        bot.send_message(message.chat.id, "I don't understand you\n\nType /help to see available commands")

@bot.message_handler(commands=['help']) # command /help
def help(message):
    bot.send_message(message.chat.id, "*Available commands:*\n"
        "/start - Start the bot\n"
        "/send - Send text to @babichtgc\n"
        "/help - Show this help message", parse_mode='Markdown')

@bot.message_handler(commands=['send']) # command /send
def send_payment(message):
    if message.chat.id in paid_users: # Check if user has already paid
        bot.send_message(message.chat.id, "You have already paid. You can send me something now")
        return
    
    prices = [types.LabeledPrice(label="1 Star", amount=1)] # 1 XTR
    bot.send_invoice(
        chat_id=message.chat.id,
        title="Payment",
        description="To send something to @babichtgc, you need to pay 1 Star!",
        invoice_payload="send_message_star",
        provider_token='',
        currency="XTR",
        prices=prices,
        start_parameter="send_message"
    )

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    if message.successful_payment.invoice_payload == "send_message_star":
        paid_users.add(message.chat.id)
        bot.send_message(
            message.chat.id,
            "Payment successful!\n\n You can now send me a message to forward to @babichtgc"
        )

@bot.message_handler(func=lambda msg: msg.chat.id in paid_users, content_types=[
    'text', 'photo', 'video', 'voice', 'sticker'
])
def forward_paid_message(message):
    try:
        if message.content_type == 'text':
            bot.send_message(TARGET_CHANNEL_ID, message.text + "\n\n@babichtgbot")

        elif message.content_type == 'photo':
            bot.send_photo(TARGET_CHANNEL_ID, message.photo[-1].file_id, caption=message.caption or "")

        elif message.content_type == 'video':
            bot.send_video(TARGET_CHANNEL_ID, message.video.file_id, caption=message.caption or "")

        elif message.content_type == 'voice':
            bot.send_voice(TARGET_CHANNEL_ID, message.voice.file_id, caption=message.caption or "")

        elif message.content_type == 'sticker':
            bot.send_sticker(TARGET_CHANNEL_ID, message.sticker.file_id)

        bot.reply_to(message, "Your message has been sent to @babichtgc ✅")

    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

    finally:
        paid_users.discard(message.chat.id) # Remove user from paid users

@bot.message_handler()
def message(message):
    if message.text.lower() == 'ping' or message.text.lower() == 'пинг':
        bot.reply_to(message, "pong")
    else:
        bot.send_message(message.chat.id, "I don't understand you\n\nType /help to see available commands")

bot.infinity_polling()
