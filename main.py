import configparser
import time
import sys
from utils.utils import count_offset, count_replies, generate_message
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon import TelegramClient

# Reading Configs
config = configparser.ConfigParser()
config.read("config.ini")

# Setting configuration values
api_id = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
api_hash = str(api_hash)

phone = config['Telegram']['phone']
username = config['Telegram']['username']
chat_id = config['Telegram']['chat_id']
offset_per_day = config['Telegram']['offset_per_day']


client = TelegramClient(username, api_id, api_hash)
client.start()
print("Client Created")


async def collect_messages(client, my_channel, count_limit):
    offset_id = 0
    limit = 100
    all_messages = []
    total_messages = 0
    while True:
        print("Current Offset ID is:", offset_id, "; Total Messages:", total_messages)
        history = await client(GetHistoryRequest(
            peer=my_channel,
            offset_id=offset_id,
            offset_date=0,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))
        if not history.messages:
            break
        messages = history.messages
        for message in messages:

            all_messages.append(message.to_dict())
        offset_id = messages[len(messages) - 1].id
        total_messages = len(all_messages)
        if count_limit != 0 and total_messages >= count_limit:
            break

    replies, forwards = count_replies(all_messages)
    replies_sorted = sorted(replies, key=replies.get, reverse=True)
    forwards_sorted = sorted(forwards, key=forwards.get, reverse=True)
    message_result = 'Hey! Daily summary has come. Check it out! \n '
    message_result += await generate_message(replies_sorted, replies, 'replies', message_result)
    message_result += await generate_message(forwards_sorted, forwards, 'forwards', message_result)
    print(replies)
    print(forwards)
    receiver = await client.get_input_entity('lobster_watcher')
    try:
        print("Sending Message... ")
        await client.send_message(receiver, message_result)
    except Exception as e:
        print(e)
        client.disconnect()
        sys.exit()


async def main():
    my_channel = await client.get_entity(chat_id)
    day = input("Введите день (e.g. 9, 15): ")
    month = input("Введите месяц (e.g. 5, 12): ")
    year = input("Введите год: ")
    offset = count_offset({'day': day,
                           'month': month,
                           'year': year}, offset_per_day)
    print('Offset is - '+str(offset))
    await collect_messages(client, my_channel, offset)
    client.disconnect()


with client:
	client.loop.run_until_complete(main())
