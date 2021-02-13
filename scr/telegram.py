from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotoVideo


api_id = your_app_id
api_hash = 'your_api_hash'

################################################
channel_username = 't.me/channel_name'
################################################

client = TelegramClient('test_session', api_id, api_hash)
client.start()

async def main():
  photos = await client.get_messages(channel_username, 0, filter=InputMessagesFilterPhotoVideo)
  def callback(current, total):
      print('Download', current, 'out of', total,
              'bytes: {:.2%}'.format(current / total))
  print(photos.total)

with client:
    client.loop.run_until_complete(main())