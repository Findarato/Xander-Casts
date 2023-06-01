import json
import os
import random
# import time
import opml
import pychromecast

import logging

from datetime import datetime

from player import Player

from update_feeds import Update_feeds

CAST_NAME = os.getenv('CAST_NAME','Xander Room')
TOTAL_PODCASTS_TO_PLAY = int(os.getenv('total_podcast_to_play',5))
PODCASTS = []

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

def getUpdate():
    json_data = []

    outline = opml.parse("podcasts.xml")

    logging.info("Getting Feeds")
    # try:
    if outline[0].text == "feeds":  # This is a pocket casts feed
        for podcast_feed in outline[0]:
            json_data.extend(Update_feeds.getFeeds(podcast_feed.xmlUrl))
    else:
        for podcast_feed in outline:
            json_data.extend(Update_feeds.getFeeds(podcast_feed.xmlUrl))

    # print("Writting JSON data")
    Update_feeds.writeFeeds(json_data)

timestamp = datetime.timestamp( datetime.now() )

st = os.stat('podcasts.json')

mtime = st.st_mtime

timeDiff = (timestamp - mtime)

if timeDiff >= 604800 or True:
    getUpdate()
    logging.info(f'Updating podcast list')

with open('podcasts.json') as json_file:
    podcast_data = json.load(json_file)

if len(podcast_data) == 0:
    getUpdate()
    with open('podcasts.json') as json_file:
        podcast_data = json.load(json_file)

logging.info(f'Going to play: {TOTAL_PODCASTS_TO_PLAY}')
logging.info(f'Chromecast: {CAST_NAME}')

logging.info("Selecting Podcasts")

count=0

while len(PODCASTS) < TOTAL_PODCASTS_TO_PLAY:
    podCast_selected = random.choice(podcast_data)
    PODCASTS.append(podCast_selected)
    podcast_title = podCast_selected['title']
    logging.info(f'{count} : {podcast_title}')
    count=count+1

# ChromeCasts = pychromecast.get_chromecasts(timeout=5)
chrome_cast_target, browser = pychromecast.get_listed_chromecasts(friendly_names=[CAST_NAME])


if len(chrome_cast_target) == 0:
    logging.critical(f'No Devices Found')
    exit()
else:
    logging.info(f'Looking for: {CAST_NAME} ')
    logging.info(f'Found it ')



chromecast_player = Player(chrome_cast_target[0])

chromecast_player.play(PODCASTS)

browser.stop_discovery()