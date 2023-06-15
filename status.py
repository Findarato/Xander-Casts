import logging
import time
import random

import json
# import gui
import datetime

class Track_status:
    def __init__(self, logfile = "/data/progress.json"):

        self.log_file =  logfile

        self.mode = {
            0: "sleeping",
            1: "playing",
            2: "stopped",
            3: "finished"
        }

        self.tracked_status = {
            "files": {
                "name": "",
                "hash": "",
                "progress": "0",
                "total": "0"
            }
        }
        self.start_time = datetime.datetime.now()

        print("Attempting to Load state")
        self.tracked_status = self.load_state()

        try:
            logging.info(f'Attempting to Load State')
            self.load_state()
        except:
            logging.info(f'Failed to load state Creating new state')
            self.save_state()

    def update_state(self,file,progress):
        self.tracked_status

    def save_state(self):
        with open(self.log_file, 'w') as outfile:
            json.dump(self.tracked_status, outfile, sort_keys=True, indent=4)


    def load_state(self):
        with open(self.log_file) as json_file:
            load_state = json.load(json_file)
            new_data = {**self.tracked_statusa, **load_state}
            return new_data

# while True:

#     if np.all(hsv_value != _previousValue):

#         start_loop = datetime.datetime.now()
#         _previousValue = hsv_value
#         if np.all(hsv_value == [21, 255, 101]):
#             _current_mode = 0
#             # fish_data["current_mode"] = mode[0]
#             print("Sleeping")
#         elif np.all(hsv_value == [102, 165, 213]):
#             start_time = datetime.datetime.now()
#             _current_mode = 1
#             print("Fishing")
#         elif np.all(hsv_value == [60, 255, 204]):
#             # print("Caught Fish")
#             rand_wait(.5,1)
#             _current_mode = 2
#             pyautogui.press('e')

#             fish_data["total_fish_caught"] += 1
#             _fishCaught += 1

#             end_time = datetime.datetime.now()
#             elapsed_time = end_time - start_time

#             fish_data["total_fish_time"] += elapsed_time.total_seconds()
#             fish_data["fish_times"].append([elapsed_time.total_seconds()])
#             print("Caught " + str(_fishCaught) + " Fish")
#             print("Caught " + str(fish_data["total_fish_caught"]) + " Total Fish")

#             save_state()

#             rand_wait()

#             print("Casting")

#             pyautogui.press('e')
#         else:
#             if _current_mode == 2:
#                 print("Hole Depleted")
#                 save_state()

#                 _current_mode = mode[3]
#                 rand_wait(.25, 1)
#                 end_loop = datetime.datetime.now()
#                 elapsed_loop = end_loop - start_loop

#                 fish_data["total_runtime_time"] += elapsed_loop.total_seconds()
