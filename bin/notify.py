import json
import os
import time
import logging
from os.path import exists, expanduser

import bin.configuration as configuration

home_dir = expanduser("~") + "/"


def do_notify(start_time):
    while True:
        config = json.loads(configuration.get_config())
        time_since = round((time.time() - start_time) / 60, 1)
        if time_since > float(config["reminder_minutes"]["value"]):
            with open(
                home_dir + "whatubinup2/tmp/do_notify", "w", encoding="UTF-8"
            ) as do_notify_file:
                do_notify_file.write(str(time.time()))
                start_time = time.time()
                logging.debug("Notification sent, timer restarting")
                continue
        else:
            remaining_time = round(
                float(config["reminder_minutes"]["value"]) - time_since, 1
            )
            logging.debug("Not ready to notify, %s minutes left", remaining_time)
            time.sleep(9)