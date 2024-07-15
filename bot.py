import requests
import telebot
import time
from telebot import types
from must import Tele
import os

token = '7304586134:AAFWq0IUtRfoxVnUcwjRT6d8hybJR3FDQGQ' #توكنك
bot = telebot.TeleBot(token, parse_mode="HTML")

subscribers = ['1142868987', '1142868987']  # تحط.هنا ايديات يلي تريد البوت بشتغل عندهم

@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in subscribers:
        bot.reply_to(message, "​𝖧𝖾𝗒 𝖭𝗂𝗀𝗀𝖺! 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝗂𝗌 𝗇𝗈𝗍 𝖿𝗋𝖾𝖾. 𝖠𝗌𝗄 𝗭𝘅𝗼𝗿𝗻𝗮𝘁𝗼𝗲 𝗍𝗈 𝗀𝖾𝗍 𝖺𝖼𝖼𝖾𝗌𝗌 𝗍𝗈 𝗍𝗁𝗂𝗌 𝖡𝗈𝗍.")
        return
    bot.reply_to(message, "Send me cc combo file! ")

@bot.message_handler(content_types=["document"])
def main(message):
    if str(message.chat.id) not in subscribers:
        bot.reply_to(message, "𝖧𝖾𝗒 𝖭𝗂𝗀𝗀𝖺! 𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝗂𝗌 𝗇𝗈𝗍 𝖿𝗋𝖾𝖾. 𝖠𝗌𝗄 𝗭𝘅𝗼𝗿𝗻𝗮𝘁𝗼𝗲 𝗍𝗈 𝗀𝖾𝗍 𝖺𝖼𝖼𝖾𝗌𝗌 𝗍𝗈 𝗍𝗁𝗂𝗌 𝖡𝗈𝗍.")
        return
    
    dd = 0
    vbv = 0
    ko = bot.reply_to(message, "Checking Your Cards...⌛").message_id
    ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
    with open("combo.txt", "wb") as w:
        w.write(ee)

    try:
        with open("combo.txt", 'r') as file:
            lino = file.readlines()
            total = len(lino)
            for cc in lino:
                current_dir = os.getcwd()
                for filename in os.listdir(current_dir):
                    if filename.endswith(".stop"):
                        bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➤ @MG_HB')
                        os.remove('stop.stop')
                        return

                try:
                    data = requests.get('https://lookup.binlist.net/' + cc[:6]).json()
                except:
                    pass

                bank = data.get('bank', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                emj = data.get('country', {}).get('emoji', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                cn = data.get('country', {}).get('name', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                dicr = data.get('scheme', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                typ = data.get('type', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
                url = data.get('bank', {}).get('url', '𝒖𝒏𝒌𝒏𝒐𝒘𝒏')

                try:
                    last = str(Tele(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR"

                if 'challenge_required' in last:
                    last = 'declined'
                elif 'challenge_required' in last:
                    last = 'Approved'

                mes = types.InlineKeyboardMarkup(row_width=1)
                cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
                status = types.InlineKeyboardButton(f"• 𝗦َِ𝗧َِ𝗔َِ𝗧َِ𝗨َِ𝗦 : {last} •", callback_data='u8')
                cm3 = types.InlineKeyboardButton(f"• 𝙋َِ𝘼َِ𝙎َِ𝙎َِ𝙀َِ𝘿 ✅  : [ {vbv} ] •", callback_data='x')
                cm4 = types.InlineKeyboardButton(f"• 𝙍َِ𝙀َِ𝙅َِ𝙀َِ𝘾َِ𝙏َِ𝙀َِ𝘿 ❌ : [ {dd} ] •", callback_data='x')
                cm5 = types.InlineKeyboardButton(f"• 𝙏َِ𝙊َِ𝙏َِ𝘼َِ𝙇 🫠 : [ {total} ] •", callback_data='x')
                stop = types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
                mes.add(cm1, status, cm3, cm4, cm5, stop)
                bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝘽َِ𝙊َِ𝙏 ِ𝘽َِ𝙔 𝗭𝘅𝗼𝗿𝗻𝗮𝘁𝗼𝗲''', reply_markup=mes)
                msg = f'''𝙋َِ𝘼َِ𝙎َِ𝙎َِ𝙀َِ𝘿  ✅
    
𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: 3DS Lookup
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: authenticate_attempt_successful
    
𝗜𝗻𝗳𝗼: {dicr} - {typ}
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {cn} - {emj} 
    
𝗕𝗬: 𝗭𝘅𝗼𝗿𝗻𝗮𝘁𝗼𝗲 '''
                msg = f'''𝙋َِ𝘼َِ𝙎َِ𝙎َِ𝙀َِ𝘿 ✅
    
𝗖𝗮𝗿𝗱: <code>{cc}</code>
𝐆𝐚𝐭𝐞𝐰𝐚𝐲: 3DS Lookup
𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Authenticate Successful
    
𝗜𝗻𝗳𝗼: {dicr} - {typ}
𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {cn} - {emj} 
    
𝗕𝗬: 𝗭𝘅𝗼𝗿𝗻𝗮𝘁𝗼𝗲 '''
                print(last)
                if "authenticate_attempt_successful" in last:
                    vbv += 1
                    bot.reply_to(message, msg)
                
                elif "authenticate_successful" in last:
                    vbv += 1
                    
                    bot.reply_to(message, msg)
                
                else:
                    dd += 1
                time.sleep(1)
    except Exception as e:
        print(e)
    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➤ 𝗭𝘅𝗼𝗿𝗻𝗮𝘁𝗼𝗲')

@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
    with open("stop.stop", "w") as file:
        pass

print("تم تشغيل البوت")
bot.polling()
