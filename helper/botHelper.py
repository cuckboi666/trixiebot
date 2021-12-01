from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram.errors import exceptions, UserNotParticipant 
from pymongo import MongoClient 
from requests import head 

import __main__ 
from os import path 
from inspect import currentframe 
from datetime import date 

# import creds and required shit 
from helper.botMessages import BotMessage

try:
    from config import Config 
except ModuleNotFoundError:
    from config import Config 
finally:
    mongoSTR = Config.mongo_str
    
filename = 'botHelper'

"""Connecting to DB"""
if mongoSTR:
    mongo_client = MongoClient(mongoSTR)
    db_user = mongo_client['URL_Uploader']
    collection_user = db_user['members']
    
"""Defining fxns"""
def line_number(fileName, e):
    cf = currentframe() 
    return f'In {fileName}.py at line {cf.f_back.f_lineno} {e}'
    
async def search_user_in_community(bot, update):
    try:
        await bot.get_chat_member('@cucklorde666', update.chat.id)
        
    except UserNotParticipant:
        await update.reply_text(BotMessage.not_joined_community, parse_mode = 'html', reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton('Join our Channel.', url = 'https://t.me/nycPnPsexyTime')],
        ]))
        return 
    except exceptions.bad_request_400.ChatAdminRequired:
        return True 
    except Exception as e:
        await bot.send_message(Config.my, line_number(fileName, e))
        return True 
    else:
        return True 
    
# find user in DB 
def checking_user_in_db(userid):
    if mongoSTR:
        document = {'userid' : userid}
        if collection_user.find_one(document):
            return True 
        collection_user.insert_one(document)
    return

# check length of files 
async def length_of_file(bot, url, userid): 
    try:
        h = head(url, allow_redirects=True)
        header = h.headers
        content_length = int(header.get('content-length'))
        file_length = int(content_length/1048576) 
    except TypeError:
        return 'Not Valid' 
    except Exception as e:
        await bot.send_message(Config.my, line_number(fileName, e))
        return 'Not Valid' 
    else:
        if content_length > 2097152000: 
            return 'Telegram Limit'
        return 'Valid'