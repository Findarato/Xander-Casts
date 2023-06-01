#!/usr/bin/env python

import time
import logging
import pychromecast
import json

class Player:
    def __init__(self, CHROMECAST):
        self.ChromeCast = CHROMECAST

    def play(self, play_list):

        logging.debug(f'chromecast: {self.ChromeCast}')

        self.ChromeCast.wait()

        self.media_controller = self.ChromeCast.media_controller.register_status_listener(self)

        def media_producer():
            for now_playing in play_list:
                # nowplaying = i
                # now_playing_json = json.loads(now_playing)
                logging.info(f'Starting to play {now_playing}')
                # logging.info(f'Starting to play {json.dumps(now_playing_json, indent=2)}')
                self.ChromeCast.media_controller.play_media(**now_playing)

                self.ChromeCast.media_controller.block_until_active()

                yield

        self._media = media_producer()

        self.new_media_status(None)
        self.ChromeCast.join()

    def new_media_status(self, status):
        if status is None or (status.player_state == 'IDLE' and status.idle_reason == 'FINISHED'):
            try:
                next(self._media)
                time.sleep(3)
            except StopIteration:
                self.ChromeCast.quit_app()
                self.ChromeCast.__del__()
