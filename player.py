#!/usr/bin/env python

import time
import logging
import pychromecast
import json

class Player:
    def __init__(self, CHROMECAST):
        self.ChromeCast = CHROMECAST


    def update(self):
            ''' Request an update from the chromecast '''
            self.ChromeCast.device.media_controller.update_status()

    def new_media_status(self, status):
        if status is None or (status.player_state == 'IDLE' and status.idle_reason == 'FINISHED'):
            try:
                next(self._media) # Advance to the next list
                time.sleep(3)
            except StopIteration:
                self.ChromeCast.quit_app()
                self.ChromeCast.__del__()
        # else:

    def play(self, play_list):
        logging.debug(f'chromecast: {self.ChromeCast}')
        self.ChromeCast.wait()
        self.media_controller = self.ChromeCast.media_controller.register_status_listener(self)
        def media_producer():
            for now_playing in play_list:
                logging.info(f'Starting to play {now_playing}')
                self.ChromeCast.media_controller.play_media(**now_playing)
                self.ChromeCast.media_controller.block_until_active()
                yield

        self._media = media_producer()

        self.new_media_status(None)

        logging.info(f'Playing at {self.ChromeCast.media_controller.status.current_time}')

        # This works to seek.
        # Next step will be to put this into a book player
        while (
            self.ChromeCast.media_controller.status.player_state != 'IDLE'):

            self.ChromeCast.media_controller.update_status()
            time.sleep(10)
            logging.info(f'Current Time 🕰️: {self.ChromeCast.media_controller.status.current_time}')



        # self.ChromeCast.join()