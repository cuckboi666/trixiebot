from pyrogram import Client 
import os 
from os import path, makedirs 
from config import Config




"""START THAT BOT BBY"""

if __name__ == "__main__":
    if not path.isdir(Config.dl):
        makedirs(Config.dl)
    plugins = dict(
        root="plugins"
    )
    
    app = Client(
        "trixiebot",
        bot_token = Config.btoken,
        api_id = Config.aid,
        api_hash = Config.aih,
        plugins=plugins
    )
    
    print('Trixie has started!')
app.run()