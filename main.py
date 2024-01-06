import os
import asyncio
from pprint import pprint
from pyrogram import Client, filters
from dotenv import load_dotenv
# Раскраска вывода в терминале, как в js chalk
from yachalk import chalk
from handlers import download_media_content
load_dotenv()

phone = os.getenv('PHONE_NUMBER')
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

app = Client("my_account")
new_dict = {}
keys_for_filter = ['id']


@app.on_message()
async def my_handler(client, message):
    for key, value in message.__dict__.items():
        new_dict[key] = value

    # filtered_dict = {key: new_dict[key] for key in keys_for_filter}
    # pprint(new_dict)
    # await message.forward("me")
    print(message)
    print(message.sender_chat.id)
    await download_media_content(new_dict, client, message)
    # with open('test.txt', 'a') as file:
    #     file.write(str(new_dict))

app.run()
