from pyrogram.enums import MessageMediaType


supported_list = ['audio', 'document', 'photo',
                  'video', 'animation', 'video_note']


async def download_media_content(message_dict, client, message):

    for type in MessageMediaType:
        type_of_message = type.name.lower()

        if (message_dict[type_of_message] and type_of_message in supported_list):
            at = getattr(message, type_of_message)
            # unixtime = time.mktime(message.date.timetuple())
            await client.download_media(at.file_id, file_name=f'.\\downloads\\{type_of_message}\\{message.sender_chat.id}\\')
