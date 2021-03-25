"""
Replying
"""

import json

from src import settings
from src.core.modules import log

# get reply


def get_reply(cmd, system=False, module=False, stage=0) -> str:
    # keep console clean
    if not system:
        log.debug("Getting reply...")

    with open(settings.REPLIES_FILE_PATH, "r+", encoding="utf-8") as replies_file:
        replies_file_data = json.load(replies_file)

    if system:
        if module:
            reply = replies_file_data["system"][cmd[0]][cmd[1]][settings.LANGUAGE][
                "data"
            ][stage]
        else:
            reply = replies_file_data["system"][cmd][settings.LANGUAGE]["data"][stage]
    else:
        reply = replies_file_data[cmd][settings.LANGUAGE]["data"][stage]

    return reply
