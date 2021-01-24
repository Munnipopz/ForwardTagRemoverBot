# ForwardTagRemoverBot - A Telegram Bot To Hide Forward Source
#Copyright (C) 2020 by Rasak <https://github.com/Artis7eeR>
#ForwardTagRemoverBot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#ForwardTagRemoverBot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

class Config:
	
 TOKEN=os.environ.get("BOT_TOKEN",None)
 SOURCE="https://t..me/mpazaan"
 START_TEXT="Hi [{}](tg://user?id={})\nI am A Forward Tag remover Bot.Send /help To Know What I Can Do \n ©Artis7eeR"
 HELP_TEXT="ꜰᴏʀᴡᴀʀᴅ ᴍᴇ ᴀ ꜰɪʟᴇ,ᴠɪᴅᴇᴏ,ᴀᴜᴅɪᴏ,ᴘʜᴏᴛᴏ ᴏʀ ᴀɴʏᴛʜɪɴɢ ᴀɴᴅ \nɪ ᴡɪʟʟ ꜱᴇɴᴅ ʏᴏᴜ ᴛʜᴇ ꜰɪʟᴇ ʙᴀᴄᴋ\n\n`ʜᴏᴡ ᴛᴏ ꜱᴇᴛ ᴄᴀᴘᴛɪᴏɴ?`\nʀᴇᴘʟʏ ᴄᴀᴘᴛɪᴏɴ ᴛᴏ ᴀ ꜰɪʟᴇ,ᴘʜᴏᴛᴏ,ᴀᴜᴅɪᴏ,ᴍᴇᴅɪᴀ"
	
