import telepot
from telepot.loop import MessageLoop
import variabiles
import time, os, platform
if(platform.system() == "Darwin"):
    import OSXUtility as utility
else:
    import WindowsUtility as utility


#variabiles
testing = True #definisci quale token tg utilizzare

def handle(msg): #what to do if new message is received
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg['text'].lower()
    
    
    if 'ping' == text:
        print(f"Ping from @{msg['from']['username']}")
        bot.sendMessage(chat_id, 'pong')
    elif 'proc' == text:
        procs = utils.getProc()
        txt = ''
        for item in procs:
            txt += item+'\n'
        bot.sendMessage(chat_id, txt)
    elif 'kill' in text:
        command = "taskkill /f /im " + text.split(' ')[1]
        os.system(command)
    
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