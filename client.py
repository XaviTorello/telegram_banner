from pprint import pprint
from datetime import timedelta, datetime

from telethon import TelegramClient, events, sync
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

api_id = 111111
api_hash = '$API_HASH'
phone_number = '+$PHONE_NUMER'
group = '$GROUP'

with TelegramClient('session_name', api_id, api_hash) as client:
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('Enter code: '))

    try:
        entity = client.get_entity('$USER_NAME')

        dialog_list = client.get_dialogs()

        messages_list = client.get_messages_list(group, 10)

        # Get n message (sorted by date desc, 0 will be latest message)
        message = messages_list[1].to_dict()
        # pprint(message)

        # Reach related user information
        user = message.get('from_id')
        full = client(GetFullUserRequest(user)).to_dict()
        # pprint(full)

        # Iterate our group participants list
        participants = client.get_participants(group)
        for participant in participants:
            participant_to_review = participant.to_dict()

            # If "spammer" user is a participant
            if str(user) == participant_to_review.get('id'):
                import pudb; pu.db

            # Review if there is any bot in our participants
            if participant_to_review.get('bot'):
                import pudb; pu.db
                # print (participant_to_review.get('bot'), participant_to_review.get('id'), participant_to_review.get('username'))
                
        # Ban user
        # rights = ChatBannedRights(
        #     until_date=datetime.now() + timedelta(days=700),
        #     view_messages_list=True,
        #     send_messages_list=True,
        #     send_media=True,
        #     send_stickers=True,
        #     send_gifs=True,
        #     send_games=True,
        #     send_inline=True,
        #     embed_links=True
        # )
        # request = client(EditBannedRequest(group, user, rights))

    except Exception as e:
        print (e)
