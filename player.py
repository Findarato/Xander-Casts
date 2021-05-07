#!/usr/bin/env python

import pychromecast
import time
import json
import logging


class Player:
    def __init__(self, cc):
        self.cc = cc
        self.cc.wait()
        self.cc.media_controller.register_status_listener(self)

    def play(self, pls):

        def media_producer():
            for i in pls:
                nowplaying = i
                logging.info(f'Starting to play {nowplaying}')
                self.cc.media_controller.play_media(**i)
                self.cc.media_controller.block_until_active()
                yield

        self._media = media_producer()

        self.new_media_status(None)
        self.cc.join()

    def new_media_status(self, status):
        if status is None or (status.player_state == 'IDLE' and status.idle_reason == 'FINISHED'):
            try:
                next(self._media)
                time.sleep(3)
            except StopIteration:
                self.cc.quit_app()
                self.cc.__del__()
