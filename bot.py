import sys, glob, importlib, logging, logging.config, pytz, asyncio
from pathlib import Path
import re  # Added import for regex filtering
from pyrogram import Client, idle, filters
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

# Function to get time-based greetings
def get_greeting() -> str:
    tz = pytz.timezone('Asia/Kolkata')
    now = datetime.now(tz)
    hour = now.hour

    if 5 <= hour < 12:
        return "Good Morning"
    elif 12 <= hour < 17:
        return "Good Afternoon"
    elif 17 <= hour < 20:
        return "Good Evening"
    else:
        return "Good Night"

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

# New handler for incoming messages to apply the filter
@TechVJBot.on_message(filters.text)
async def handle_message(client, message):
    # Get the text of the incoming message
    text = message.text
    # Apply the filter_mentions function to the text
    filtered_text = filter_mentions(text)
    # Get time-based greeting
    greeting = get_greeting()
    # Reply with the greeting and filtered text
    await message.reply(f"HEY {message.from_user.first_name}, {greeting} 🌞\n\n{filtered_text}")

async def start():
    print('\n')
    print('Initializing Your Bot')
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
    # Send restart message only if it hasn't been sent yet
    if not temp.RESTART_MESSAGE_SENT:
        await TechVJBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
        temp.RESTART_MESSAGE_SENT = True
    if CLONE_MODE:
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
