import logging
import os
import datetime


def setup() -> None:
    if not os.path.isdir('logs'):
        os.mkdir("logs")
    now = datetime.datetime.now()
    name = "%s-%s-%s-log" % (now.day, now.month, now.year)
    file_log = logging.FileHandler(f"logs/{name}.log")
    console_log = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s", handlers=(
                            file_log, console_log))
