# For @UniBorg

"""Countdown Commands

.timer

.fcd"""



from telethon import events

from datetime import datetime

from uniborg.util import admin_cmd

import importlib.util

import asyncio

import random

import importlib.util




@borg.on(events.NewMessage(outgoing=True, pattern='^\.(f?f)charge '))

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n`Wireless Charging (beta) Starts In` '

 j=500

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k+10

  await asyncio.sleep(10)

 if e.pattern_match.group(1) == 'f':

  await e.edit("`Wireless Charging (beta) Started...\n\n\n Device Detected: Nokia 1100 \n\n Battery Percentage : 69%` ")

