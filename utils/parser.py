from handlers.message_handler import conversation
from handlers.callback_query_handler import CallbackQueryHandler


async def MessageParser(update):
    # Parsing the message content
    print(update)
    if 'message' in update:
        chat_id = update['message']['chat']['id']
        text = update['message']['text']
        id_ = update['message']['message_id']
        if text == "/generate":
            await CallbackQueryHandler(chat_id, id_, text)
        else:
            await conversation(chat_id, text)
    elif 'callback_query' in update:
        chat_id = update['callback_query']['from']['id']
        id_ = update['callback_query']['message']['message_id']
        data = update['callback_query']['data']
        await CallbackQueryHandler(chat_id, id_, data)
