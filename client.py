from telethon import TelegramClient, events, sync
from pprint import pprint
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from datetime import timedelta, datetime

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 111111
api_hash = '$API_HASH'
phone_number = '+$PHONE_NUMER'
group = '$GROUP'

with TelegramClient('session_name', api_id, api_hash) as client:
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('Enter code: '))

    try:
        # # Does it have an username? Use it!
        entity = client.get_entity('$USER_NAME')

        # Do you have a conversation open with them? Get dialogs.
        client.get_dialogs()

        # # Are they participant of some group? Get them.

        # # Is the entity the original sender of a forwarded message? Get it.
        # client.get_messages('$GROUP', 100)

        # # NOW you can use the ID, anywhere!
        # entity = client.get_entity(123456)
        # # client.send_message(123456, 'Hi!')

        messages = client.get_messages(group, 10)
        message = messages[1].to_dict()
        pprint(message)
        print()
        print()

        user = message.get('from_id')
        print (user)
        print()
        print()
        full = client(GetFullUserRequest(user)).to_dict()
        # pprint(full)

        participants = client.get_participants(group)
        for participant in participants:
            participant_to_review = participant.to_dict()
            if str(user) == participant_to_review.get('id'):
                import pudb; pu.db



    except Exception as e:
        print (e)
