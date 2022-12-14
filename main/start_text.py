from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN


@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="This is personal use bot π. Do you want your own bot? π Click the source code to deploy"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("π€ SOURCE CODE", url="https://github.com/Rajrohit000666/Simple-Rename-Bot")
        ],[
        InlineKeyboardButton("π₯οΈ How To Deploy", url="https://github.com/Rajrohit000666")
    ]])
    if msg.from_user.id != ADMIN:
        await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
        return
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"hai {msg.from_user.mention} i am simple rename bot with personal usage.\nthis bot is made by <b><a href=https://github.com/Rajrohit000666>ππππ² π΄πΆπΏπΉ</a></b>"                                     
    button= [[
        InlineKeyboardButton("π€ Bot Updates", url="https://t.me/movie4ubotschannel")
        ],[
        InlineKeyboardButton("βΉοΈ Help", callback_data="help"),
        InlineKeyboardButton("π‘ About", callback_data="about") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt=f"just send a file and /rename <new name> with replayed your file\n\nReply a photo and send /set to set permanent thumbnail\n/view to see your thumbnail"
    button= [[        
        InlineKeyboardButton("π« Close", callback_data="del"),
        InlineKeyboardButton("β¬οΈ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/cute_girl_rani>ππππ² π΄πΆπΏπΉ π₯π?π»πΆ π¦</a> & <a href=https://t.me/movie4ubotschannel>Movie4u bots</a>"  
    Source="<a href=https://github.com/Rajrohit000666/Movie4u-Rename-Bot>Click Here</a>"
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://github.com/Rajrohit000666>ππππ² π΄πΆπΏπΉ π₯π?π»πΆ π¦</a>\nBot Updates: <a href=https://t.me/movie4ubotschannel>Movie4u bots</a>\nMy Master's: {Master}\nSource Code: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("π« Close", callback_data="del"),
        InlineKeyboardButton("β¬οΈ Back", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


