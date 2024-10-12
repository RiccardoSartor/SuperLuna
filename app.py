import telepot
from telepot.loop import MessageLoop
import variabiles
import time, platform
if(platform.system() == "Darwin"):
    import OSXUtility as utility
else:
    import WindowsUtility as utility


#variabiles
testing = True #definisci quale token tg utilizzare

def handle(msg): #what to do if new message is received
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg['text'].lower()
    
    if '/start' == text:
        bot.sendMessage(chat_id, "Luna Balena!")
    elif 'ping' == text:
        print(f"Ping from @{msg['from']['username']}")
        bot.sendMessage(chat_id, 'pong')
    elif 'proc' == text:
        procs = utility.processes()
        counter = 11
        txt = 'Pid | Name\n'
        for item in procs:
            if len(txt) + len(str(item[0])) + len(item[1]) + 2 > 4096: #to avoid telegram length message limit
                bot.sendMessage(chat_id, txt)
                txt = ''
            txt += str(item[0]) + " " + str(item[1]) + '\n'
        bot.sendMessage(chat_id, txt)
    elif 'kill' in text:
        if len(text.split(" ")) == 2:
            utility.killProc(text.split(' ')[1])
            bot.sendMessage(chat_id, "👍")
        else:
            bot.sendMessage(chat_id, "Errore, comando: 'kill [filename]'")
    elif text == 'shutdown':
        utility.shutdown()
        bot.sendMessage(chat_id, "👍")
    elif text == "reboot":
        utility.reboot()
        bot.sendMessage(chat_id, "👍")
    elif "link" in text:
        if len(text.split(" ")) == 2:
            utility.openLink(text.split(" ")[1])
        else:
            bot.sendMessage(chat_id, "Errore, comando: 'link [example.com]")

bot = telepot.Bot(variabiles.token_test if testing else variabiles.token_public)
MessageLoop(bot, handle).run_as_thread()
print(f'Logged in')
while 1:
    time.sleep(10)



"""
msg example: {
    'message_id': 598, 
    'from': {
        'id': 2067687200, 
        'is_bot': False, 
        'first_name': 'giovanni giorgio', 
        'username': 'giovannigiorgio51', 
        'language_code': 'it'
    }, 
    'chat': {'id': 2067687200, 
    'first_name': 'giovanni giorgio', 
    'username': 'giovannigiorgio51', 
    'type': 'private'
    }, 
'date': 1658947122, 
'text': '/start', 
'entities': [{
    'offset': 0, 
    'length': 6, 
    'type': 'bot_command'}]
}
"""