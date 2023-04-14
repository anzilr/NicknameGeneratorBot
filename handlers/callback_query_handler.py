from utils.api import Generator
from pydantic import BaseModel
from utils.inlinekeyboard import InlineKeyboardMarkup
from utils.sender import SendMessage, EditMessage


# Creating conversation data model
class ConversationData(BaseModel):
    state: int
    category: int = ""
    gender: int = ""


# Defining conversation states
STATE_START = 0
STATE_CATEGORY = 1
STATE_GENDER = 2
STATE_FINAL = 3

# Creating a dictionary to store conversation data
conversation_data = {}

CATEGORY_BUTTON = [
    [
        {'text': '📛 Nickname', 'callback_data': '2'},
        {'text': '🕹️ Game Name', 'callback_data': '5'}
    ],
    [
        {'text': '🐉 Fantasy Name', 'callback_data': '6'},
        {'text': '🎮 GamerTag', 'callback_data': '4'}
    ],
    [
        {'text': '🎌 Clan Name', 'callback_data': 'CLAN 9'},
        {'text': '🦸🏻‍♂️ SuperHero', 'callback_data': '3'}
    ]
]

GENDER_BUTTON = [
    [
        {'text': '♂️ Masculine', 'callback_data': '0'},
        {'text': '♀️ Feminine', 'callback_data': '1'}
    ],
    [
        {'text': '🔀 Random', 'callback_data': '2'}
    ]
]

CLAN_BUTTON = [
    [
        {'text': '🔠 Long', 'callback_data': '1'},
        {'text': '🔤 Short', 'callback_data': '0'}
    ],
    [
        {'text': '🔀 Random', 'callback_data': '2'}
    ]
]

FINAL_BUTTON = [
    [
        {'text': '🔄 Regenerate', 'callback_data': 'regenerate'}
    ],
    [
        {'text': '👨‍💻 Start agin', 'callback_data': 'STATE_CATEGORY'}
    ]
]


# Using CallbackQuery to regenerate result
async def CallbackQueryHandler(chat_id, message_id, data):
    state = conversation_data.get(chat_id, ConversationData(state=STATE_CATEGORY)).state
    if data == "/generate":
        button = await InlineKeyboardMarkup(buttons=CATEGORY_BUTTON)
        await SendMessage(chat_id=chat_id,
                          text="Select a category from below 👇🏻", reply_markup=button)
        # Storing the current state
        conversation_data[chat_id] = ConversationData(state=STATE_GENDER)

    elif data == "regenerate":
        button = await InlineKeyboardMarkup(buttons=FINAL_BUTTON)
        results = await Generator(conversation_data[chat_id].category, conversation_data[chat_id].gender)
        await EditMessage(chat_id=chat_id, message_id=message_id,
                          text=results, reply_markup=button)

    elif data == "STATE_CATEGORY":
        button = await InlineKeyboardMarkup(buttons=CATEGORY_BUTTON)
        await EditMessage(chat_id=chat_id, message_id=message_id,
                          text="Select a category from below 👇🏻", reply_markup=button)
        # Storing the current state
        conversation_data[chat_id] = ConversationData(state=STATE_GENDER)
        # del conversation_data[chat_id]
    else:
        if state == STATE_GENDER:
            if "CLAN" in data:
                cat, cat_num = data.split()
                button = await InlineKeyboardMarkup(buttons=CLAN_BUTTON)
                conversation_data[chat_id].category = cat_num
                await EditMessage(chat_id=chat_id, message_id=message_id,
                                  text="Select a format from below 👇🏻", reply_markup=button)

            else:
                button = await InlineKeyboardMarkup(buttons=GENDER_BUTTON)
                conversation_data[chat_id].category = data
                await EditMessage(chat_id=chat_id, message_id=message_id,
                                  text="Select a gender from below 👇🏻", reply_markup=button)

            conversation_data[chat_id].state = STATE_FINAL
        elif state == STATE_FINAL:
            conversation_data[chat_id].gender = data
            button = await InlineKeyboardMarkup(buttons=FINAL_BUTTON)
            results = await Generator(conversation_data[chat_id].category, conversation_data[chat_id].gender)
            await EditMessage(chat_id=chat_id, message_id=message_id,
                              text=results, reply_markup=button)

        # await SendMessage(chat_id, response, reply_markup)
