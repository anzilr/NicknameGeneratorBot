import traceback
from utils.inlinekeyboard import InlineKeyboardMarkup
from utils.sender import SendMessage
from utils.api import Generator
from config import START_TEXT


CMD = ["/start", "/help"]
CONV_CMD = ["/generate", "/gen"]


async def conversation(chat_id, text):
    try:
        # Getting the current state of the conversation


        if text in CMD:
            reply_markup = await InlineKeyboardMarkup(buttons=[
                [
                    {'text': '🗃️ Source', 'url': 'https://github.com/anzilr/NicknameGeneratorBot'},
                    {'text': '↩️ Share Me', 'url': 't.me/share/url?url=Hi! I am 🤖 @NicknameGeneratrBot. \n\nI can generate nicknames for you 😎.'}
                ],
                [
                    {'text': '👨‍💻 Generate',
                     'callback_data': '/generate'}
                ]
            ])

            await SendMessage(chat_id=chat_id, text=START_TEXT, reply_markup=reply_markup)



    except Exception:
        print(traceback.format_exc())


