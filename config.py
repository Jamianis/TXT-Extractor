#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6787943482:AAHyCNpoHedsWC8XcZvpPlgtny_V_9wcVdk")
    API_ID = int(os.environ.get("API_ID", "27006142"))
    API_HASH = os.environ.get("API_HASH", "8d5171c23fd1836db908b8739d288336")
    AUTH_USERS = os.environ.get("AUTH_USERS", "1798290309")
