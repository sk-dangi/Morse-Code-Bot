import os
from dotenv import load_dotenv
import telebot

load_dotenv()

api_key = os.getenv("API_KEY")


MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


bot = telebot.TeleBot(token=api_key)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Just Send Me Morse To Encrypt or Decrypt")
	
@bot.message_handler(commands=['help'])
def help(message):
	bot.reply_to(message, "what you want to help from us")


@bot.message_handler(commands=['encrypt','e','E'])
def encrypt(message):
    text = "Enter your morese"
    bot.reply_to(message,text)

@bot.message_handler()
def chat(message):
        user_input = message.text.upper()
        if user_input[0] == "." or user_input[0] == "-":
            try:
                user_input += " "
                
                list_key = list(MORSE_CODE_DICT.keys())
                list_value = list(MORSE_CODE_DICT.values())
                morese = ""
                dec = ""
                for code in user_input:
                    if code != " ":
                        morese += code
                        space = 0
                    else:
                        space += 1  
                        if space == 2:
                            dec += " "
                        else:
                            dec = dec +   list_key[list_value.index(morese)]
                            morese = ""

                bot.reply_to(message,dec)   
            except Exception as e:
                bot.reply_to(message, e)
        else:
            try:
                enc = ""
                for i in user_input:
                    if i != " ":
                        enc +=  MORSE_CODE_DICT[i] + " "
                    else:
                        enc += " "    
                        
                bot.reply_to(message,enc) 
            except Exception as e:
                text = 'PLEASE TYPE IN UPPER CASE LETTER' 
                bot.reply_to(message,text) 
        
    
print("started......")    
bot.polling(none_stop=True, timeout=123)
    
	
    
    
        

    
	