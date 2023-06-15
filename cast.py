import json
import os

import logging

from datetime import datetime
from player import Player

CAST_NAME = os.getenv('CAST_NAME','Xander Room')
TOTAL_PODCASTS_TO_PLAY = int(os.getenv('TOTAL_PODCASTS_TO_PLAY',5))
PLAYER_TYPE = os.getenv('PLAYER_TYPE',"Podcast")
BOOK = os.getenv('BOOK_URL',"http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")

# fmt = "%(asctime)s %(levelname)s (%(threadName)s) [%(name)s] %(message)s"
fmt = "%(asctime)s %(levelname)s (%(threadName)s) %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO)

# logging.info(f'BOOK_PLAYER is {PLAYER_TYPE}')
logging.info(f'Total Podcasts to play is {TOTAL_PODCASTS_TO_PLAY}')

if PLAYER_TYPE == "Book":
    logging.info(f'Starting Book Player')
    from book_player import Book_player

    player = Book_player(CAST_NAME,BOOK)
else:
    logging.info(f'Starting Podcast Player')
    from podcast_player import Podcast_player

    player = Podcast_player(CAST_NAME,TOTAL_PODCASTS_TO_PLAY)
    player.play()
