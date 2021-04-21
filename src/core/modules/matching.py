import json
from typing import Any

from src import settings
from src.core.modules import log, tts, stt, replying

from src.core.commands import (
    cmd_date,
    cmd_about_me,
    cmd_echo,
    cmd_google_news,
    cmd_google_search,
    cmd_note_add,
    cmd_note_clear,
    cmd_note_read,
    cmd_time,
    cmd_weather,
    cmd_register_install,
    cmd_coronavirus,
    cmd_commands,
)

# match command name with module
commands = {
    "time": cmd_time,
    "date": cmd_date,
    "weather": cmd_weather,
    "news": cmd_google_news,
    "echo": cmd_echo,
    "note": cmd_note_read,
    "note_add": cmd_note_add,
    "note_clear": cmd_note_clear,
    "me_info": cmd_about_me,
    "register_install": cmd_register_install,
    "covid": cmd_coronavirus,
    "commands": cmd_commands,
}


def check_match(cmd_input) -> dict:
    cmd = {"name": None, "text": None, "input": cmd_input}
    # get phrases file data as json
    with open(settings.PHRASES_FILE_PATH, encoding="utf-8") as phrases_file:
        phrases_file_data = json.load(phrases_file)
    # scan phrases file for match
    # for every command title
    for cmd_title in phrases_file_data:
        # for every data line of command title (in prefered language)
        for cmd_phrase in phrases_file_data[cmd_title][settings.LANGUAGE]["data"]:
            # check if in input
            if cmd_phrase in cmd_input.lower():
                # ready for return
                cmd = {"name": cmd_title, "text": cmd_phrase, "input": cmd_input}
                return cmd


"""
test match
"""


def test_match(cmd_input) -> dict:
    cmd = {"name": None, "text": None, "input": cmd_input}
    # get phrases file data as json
    with open(settings.PHRASES_FILE_PATH, encoding="utf-8") as phrases_file:
        phrases_file_data = json.load(phrases_file)
    # scan phrases file for match
    # for every command title
    for cmd_title in phrases_file_data:
        keyword = phrases_file_data[cmd_title][settings.LANGUAGE]["keyword"]
        # check if keyword in input
        if keyword in cmd_input.lower():
            tts.speak(
                replying.get_reply(
                    ["matching", "ask"], system=True, module=True
                ).format(keyword)
            )
            yn_input = stt.listen_for_binary()
            # if 'yes'
            if yn_input:
                # read the phrases file
                with open(
                    settings.PHRASES_FILE_PATH, "r+", encoding="utf-8"
                ) as phrases_file:
                    phrases_file_data = json.load(phrases_file)
                # add the new phrase to the command list
                phrases_file_data[cmd_title][settings.LANGUAGE]["data"].append(
                    cmd_input.lower()
                )
                # write the list to the file
                with open(
                    settings.PHRASES_FILE_PATH, "r+", encoding="utf-8"
                ) as phrases_file:
                    json.dump(
                        phrases_file_data, phrases_file, indent=2, ensure_ascii=False
                    )
                tts.speak(
                    replying.get_reply(["matching", "added"], system=True, module=True)
                )
                cmd = {
                    "name": cmd_title,
                    "text": phrases_file_data[cmd_title][settings.LANGUAGE]["data"][0],
                    "input": cmd_input,
                }
                return cmd


def google_match(cmd_input) -> dict:
    log.debug("Google Search...")
    try:
        cmd = {"name": "google_search", "text": cmd_input, "input": cmd_input}
        cmd_google_search.ex(cmd_input)
        return cmd
    except:
        log.debug("No result from Google Search...")


def get_match(cmd_input) -> Any:
    log.debug("Matching...")

    cmd = {"name": None, "text": None, "input": cmd_input}

    # all jobs in correct order
    jobs = [check_match, test_match, google_match]

    # for every job
    for job in range(len(jobs)):
        cmd = jobs[job](cmd_input)
        # check if matched
        if cmd is not None:
            log.debug("Matched command '{}'".format(cmd["name"]))
            return cmd
        else:
            # next stage matching
            continue
    # unable to match
    log.debug("Couldn't match command from input...")


def execute_match(cmd) -> None:
    log.debug("Executing...")
    #
    try:
        # check if command exists as python script
        if commands.__contains__(cmd["name"]):
            log.debug("Replying...")
            commands.get(cmd["name"]).ex(cmd)
        elif cmd["name"] == "google":
            log.debug("Already executed...")
        else:
            log.error("Couldn't match command script")
    # type error: no command found
    except TypeError:
        tts.speak(replying.get_reply(["matching", "fail"], system=True, module=True))
