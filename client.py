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

    except Exception as e:
        print (e)
