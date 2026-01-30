from app import app
from pyrogram import Client, filters
from database.users import create_user

@app.on_message(filters.command('start'))
async def start_handler(client, message):
    user_id = message.from_user.id
    
    await create_user(user_id)
    await message.reply_text("Bot is alive . \n Your request is pending for approval.")