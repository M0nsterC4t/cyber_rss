import os

import requests
from telegram.ext import ExtBot

from dotenv import load_dotenv
# load_dotenv()
bot_token = os.getenv('BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
message_thread_id=os.getenv('THREAD_MESSAGE_ID')
class TelegramBot:
    def __init__(self):
        self._bot = ExtBot(token=bot_token)
        self._chat_id = chat_id
        self._message_thread_id = message_thread_id

    async def send_message(self, message):
        try:
            await self._bot.send_message(chat_id=self._chat_id,
                                     message_thread_id= self._message_thread_id,
                                     text=message)
        except Exception as e:
            print(e)
            pass

    async def send_document(self, caption, message_thread_id, document, filename):
        try:
            await self._bot.send_document(chat_id=self._chat_id,
                                      message_thread_id=message_thread_id,
                                      caption=caption,
                                      document=document,
                                      filename=filename,
                                      parse_mode='markdown')
        except Exception as e:
            print(e)
            pass