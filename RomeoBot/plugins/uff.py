from . import *


@hell_cmd(pattern="uff")
async def _(event):
    if not event.is_reply:
        return await event.edit("Reply to a documents..")
    k = await event.get_reply_message()
    pic = await k.download_media()
    await bot.send_file("me",pic)
           
    await event.delete()

CmdHelp("uff").add_command(
  "Uff", "<anime name>", "Searches for the given anime and sends the details.", "anime Darling in the franxx"
).add()
