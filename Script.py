import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://t.me/QTVS_BOT_X_CLOUD')
    START_TXT = environ.get("START_TXT", """𝐇𝐞𝐥𝐥𝐨... {}
    
𝐌𝐲 𝐍𝐚𝐦𝐞 𝐈𝐬 <a href=https://t.me/Binthu_x_robot><b>☔𝐊𝐮𝐭𝐭𝐲 𝐏𝐚𝐚𝐩𝐚♣</b></a>

𝐈 𝐂𝐚𝐧 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐌𝐨𝐯𝐢𝐞𝐬, 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝 𝐌𝐚𝐤𝐞 𝐌𝐞 𝐀𝐝𝐦𝐢𝐧.. 𝐓𝐡𝐞𝐧 𝐒𝐞𝐞 𝐌𝐲 𝐏𝐨𝐰𝐞𝐫

𝐌𝐚𝐤𝐞𝐫 𝐌𝐞 <a href=https://t.me/SMD_Owner><b>♣𝐀𝐮𝐭𝐡𝐨𝐫🥀</b></a></b>""")
    HELP_TXT = """<b>𝐇𝐞𝐲 {} 𝐅𝐫𝐢𝐞𝐧𝐝𝐬 𝐇𝐞𝐫𝐞 𝐘𝐨𝐮𝐫 𝐁𝐮𝐭𝐭𝐨𝐧𝐬 👇</b>"""
    ABOUT_TXT = """<b>🎧 𝐌𝐲 𝐍𝐚𝐦𝐞 𝐢𝐬 : <a href=https://t.me/Binthu_x_robot>♣𝐊𝐮𝐭𝐭𝐲 𝐏𝐚𝐚𝐩𝐚♻️</a>
🔥 𝐀𝐫𝐭𝐢𝐬𝐭 : <a href=https://t.me/Owner_of_qtmve>🍁𝐐𝐭𝐦𝐯𝐞_𝐎𝐰𝐧𝐞𝐫☔</a>
🍻 𝐃𝐞𝐯𝐨𝐥𝐨𝐩𝐞𝐫 : <a href=https://t.me/SMD_Owner>🎋𝐒𝐌𝐃_𝐎𝐰𝐧𝐞𝐫🦞</a>
✍️ 𝐆𝐫𝐚𝐝𝐮𝐚𝐭𝐞 : <a href=https://t.me/Siva_Soft>🛬𝐒𝐢𝐯𝐚🚦</a>
♠ 𝐊𝐨𝐥𝐚𝐫𝐮 : <a href=https://t.me/Svaraz>🎭𝐔𝐚𝐫𝐮𝐭𝐨🔥</a>
👨‍🔧 𝐇𝐞𝐥𝐩𝐞𝐫 : <a href=https://t.me/Thavarajtj>🗽𝐓𝐡𝐚𝐯𝐚𝐫𝐚𝐣🌿</a>
⚜️ 𝐐𝐭𝐯𝐬𝐨𝐟𝐟𝐢𝐜𝐢𝐚𝐥 : <a href=https://t.me/QTVS_BOT_X_CLOUD>🥀𝐌𝐚𝐫𝐯𝐞𝐥🎋</a></b>"""
    SOURCE_TXT = ""𝐓𝐡𝐢𝐬 𝐈𝐬 𝐀𝐧 𝐎𝐩𝐞𝐧-𝐒𝐨𝐮𝐫𝐜𝐞 𝐏𝐫𝐨𝐣𝐞𝐜𝐭 𝐁𝐲 @SMD_Owner

- 𝟏𝟎𝟎﹪ 𝐂𝐨𝐝𝐞𝐝 𝐁𝐲 <a href=https://t.me/SMD_Owner>🌿𝐑𝐨𝐥𝐞𝐱🦞</a>

- & 𝐑𝐞𝐩𝐨 𝐋𝐢𝐧𝐤 👇 𝐇𝐞𝐫𝐞"""
    MANUELFILTER_TXT = """ʜᴇʟᴩ: <b>ꜰɪʟᴛᴇʀꜱ</b>

• ꜰɪʟᴛᴇʀ ɪꜱ ᴛʜᴇ ꜰᴇᴀᴛᴜʀᴇ ᴡᴇʀᴇ ᴜꜱᴇʀꜱ ᴄᴀɴ ꜱᴇᴛ ᴀᴜᴛᴏᴍᴀᴛᴇᴅ ʀᴇᴘʟɪᴇꜱ ꜰᴏʀ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ᴋᴇʏᴡᴏʀᴅ ᴀɴᴅ ᴡɪʟʟ ʀᴇꜱᴘᴏɴᴅ ᴡʜᴇɴᴇᴠᴇʀ ᴀ ᴋᴇʏᴡᴏʀᴅ ɪꜱ ꜰᴏᴜɴᴅ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ

<b>ɴᴏᴛᴇ:</b>
1. ꜰʟɪᴍꜱ ꜱʜᴏᴜʟᴅ ʜᴀᴠᴇ ᴀᴅᴍɪɴ ᴘʀɪᴠɪʟʟᴀɢᴇ.
2. ᴏɴʟʏ ᴀᴅᴍɪɴꜱ ᴄᴀɴ ᴀᴅᴅ ꜰɪʟᴛᴇʀꜱ ɪɴ ᴀ ᴄʜᴀᴛ.
3. ᴀʟᴇʀᴛ ʙᴜᴛᴛᴏɴꜱ ʜᴀᴠᴇ ᴀ ʟɪᴍɪᴛ ᴏꜰ 64 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ.

<b>ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- MS Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Hb_LinkZzz supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/SMD_Owner)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of @Binthu_x_robot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """🗽★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
❤‍🔥★ 𝐓𝐨𝐭𝐚𝐥 𝐔𝐬𝐞𝐫𝐬: <code>{}</code>
❤‍🔥★ 𝐓𝐨𝐭𝐚𝐥 𝐂𝐡𝐚𝐭𝐬: <code>{}</code>
❤‍🔥★ 𝐔𝐬𝐞𝐝 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code> 𝙼𝚒𝙱
❤‍🔥★ 𝐅𝐫𝐞𝐞 𝐒𝐭𝐨𝐫𝐚𝐠𝐞: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
<b>᚛› @SMD_Owner </b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫-new 
    
<b>᚛› 𝐈𝐃⚡ - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞⚡ - {}</b>
<b>᚛› 𝐆𝐭 𝐅𝐢𝐥𝐭𝐞𝐫 </b>
"""
