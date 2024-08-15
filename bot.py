import sys, glob, importlib, logging, logging.config, pytz, asyncio
from pathlib import Path
import re  # Added for filtering mentions
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import datetime  # For time-based greeting
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

from pyrogram import Client, idle, filters  # Added filters for message handling
from pyromod import listen
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from Script import script 
from datetime import date, datetime 
from aiohttp import web
from plugins import web_server
from plugins.clone import restart_bots

from TechVJ.bot import TechVJBot
from TechVJ.util.keepalive import ping_server
from TechVJ.bot.clients import initialize_clients

# Function to filter out mentions and specific text
def filter_mentions(message: str) -> str:
    # Remove all mentions except for @NcHSupport
    message = re.sub(r'@\w+', '', message)
    # Add @NcHSupport back if it was removed
    if "@NcHSupport" not in message:
        message += " @NcHSupport"
    # Remove specific text
    message = message.replace("𝕂𝔸ℕℍ𝔸𝕀𝕐𝔸🎭", "")
    return message.strip()

# Function to send a greeting message
async def send_greeting(client, message):
    user_first_name = message.from_user.first_name
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    current_time = now.strftime('%p')
    greeting = f"Good {'Morning' if current_time == 'AM' else 'Afternoon/Evening'}, {user_first_name}! 👋"
    greeting_message = (
        f"{greeting}\n\n"
        "I am a powerful auto-filter bot. You can use me in your group for auto-filtering with link shortening. "
        "Just add me as an admin in your group, and I'll provide movies with your link shortener."
    )
    await client.send_message(chat_id=message.chat.id, text=greeting_message)

# Adding a new handler for incoming messages
@TechVJBot.on_message(filters.text)
async def handle_message(client, message):
    # Send greeting message when a user sends a message
    await send_greeting(client, message)
    # Get the text of the incoming message
    text = message.text
    # Apply the filter_mentions function to the text
    filtered_text = filter_mentions(text)
    # Reply with the filtered text
    await message.reply(filtered_text)

ppath = "plugins/*.py"
files = glob.glob(ppath)
TechVJBot.start()
loop = asyncio.get_event_loop()

async def start():
    print('\n')
    print('Initalizing Your Bot')
    bot_info = await TechVJBot.get_me()
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Tech VJ Imported => " + plugin_name)
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()
    me = await TechVJBot.get_me()
    temp.BOT = TechVJBot
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    logging.info(LOG_STR)
    logging.info(script.LOGO)
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await TechVJBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    if CLONE_MODE == True:
        print("Restarting All Clone Bots.......")
        await restart_bots()
        print("Restarted All Clone Bots.")
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('Service Stopped Bye 👋')
