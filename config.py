import os 
from dotenv import load_dotenv


load_dotenv()

class Config():
    btoken = os.getenv("BOT_TOKEN")    
    aid = os.getenv("API_ID")
    aih = os.getenv("API_HASH")
    my = os.getenv("MY_ID")
    dl = os.getenv("DL_LOCATION")
    cid = os.getenv("CHAT_ID")
    mongo_str = os.getenv("MONGO_STR")
    

