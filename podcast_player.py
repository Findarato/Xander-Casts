import json
import os
import random
import time
import opml
import pychromecast

import logging

from datetime import datetime

from player import Player

from update_feeds import Update_feeds

#
# Update the list of podcasts from a feed
#
class Podcast_player():

    def __init__(self, cast_name, TPPTP=0):
        self.chrome_cast = cast_name
        self.total_podcasts_to_play = TPPTP
        self.podcasts = []
        self.json_data = []

    def getUpdate(self):

        logging.info(f'Updating podcast list')

        outline = opml.parse("podcasts.xml")

        logging.info("Getting Feeds")
        # try:
        if outline[0].text == "feeds":  # This is a pocket casts feed
            for podcast_feed in outline[0]:
                self.json_data.extend(Update_feeds.getFeeds(podcast_feed.xmlUrl))
        else:
            for podcast_feed in outline:
                self.json_data.extend(Update_feeds.getFeeds(podcast_feed.xmlUrl))

        # Update_feeds.writeFeeds(self.json_data)

    def play(self):

        logging.info(f'Going to play: {self.total_podcasts_to_play}')
        logging.info(f'Chromecast: {self.chrome_cast}')

        logging.info("Selecting Podcasts")

        count=0

        self.getUpdate()
        #
        # Build out total list of podcasts to play
        #
        while len(self.podcasts) < self.total_podcasts_to_play:
            podCast_selected = random.choice(self.json_data)
            self.podcasts.append(podCast_selected)
            podcast_title = podCast_selected['title']
            logging.info(f'{count}: {podcast_title}')
            count=count+1

        chrome_cast_target, browser = pychromecast.get_listed_chromecasts(friendly_names=[self.chrome_cast])


        if len(chrome_cast_target) == 0:
            logging.critical(f'No Devices Found')
            exit()
        else:
            logging.info(f'Looking for: {self.chrome_cast} ')
            logging.info(f'Found it ')


        chrome_cast_target[0].wait()

        chrome_cast = chrome_cast_target[0]


        chromecast_player = Player(chrome_cast)

        chromecast_player.play(self.podcasts)


        # book_player = Player(chrome_cast)
        # book_player.play(BOOK,100)

        browser.stop_discovery()