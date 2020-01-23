"""COMMAND : .eye"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "eye":

        await event.edit(input_str)

        animation_chars = [

            "👁👁\n  👄  =====> 1",
            "👁👁\n  👅  =====> 2",    
            "👁👁\n  💋  =====> 3",
            "👁👁\n  👄  =====> 4",
            "👁👁\n  👅  =====> 5",    
            "👁👁\n  💋  =====> 6",
            "👁👁\n  👄  =====> 7",
            "👁👁\n  👅  =====> 8",    
            "👁👁\n  💋  =====> 9",
            "👁👁\n  👄  =====> Hi All, How Are You Guys..."
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])
