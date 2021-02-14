import json

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
    cmd_weather_forecast
)

# match command name with module
commands = {
    "time": cmd_time,
    "date": cmd_date,
    "weather": cmd_weather,
    "weatherforecast": cmd_weather_forecast,
    "news": cmd_google_news,
    "echo": cmd_echo,
    "note": cmd_note_read,
    "note_add": cmd_note_add,
    "note_clear": cmd_note_clear,
    "me_info": cmd_about_me
}


def setup():
    pass


# check command match
def check_match(input: str):
    cmd = {
        "name": None,
        "text": None,
        "input": input
    }

    with open(settings.PHRASES_FILE_PATH, encoding="utf-8") as phrases_file:
        phrases_file_data = json.load(phrases_file)

    # scan phrases file for match for every command title
    for cmd_title in phrases_file_data:
        for cmd_phrase in phrases_file_data[cmd_title][settings.LANGUAGE]["data"]:
            if cmd_phrase in input.lower():
                cmd = {"name": cmd_time, "text": cmd_phrase, "input": input}
                return cmd

# test command match


def test_match(input: str):
    cmd = {
        "name": None,
        "text": None,
        "input": input
    }

    with open(settings.PHRASES_FILE_PATH, encoding="utf-8") as phrases_file:
        phrases_file_data = json.load(phrases_file)

    for cmd_title in phrases_file_data:
        keyword = phrases_file_data[cmd_title][settings.LANGUAGE]["keyword"]

        if keyword in input.lower():
            tts.speak(replying.get_reply(["matching", "ask"], system=True, module=True))
            binary_input = stt.listen_for_binary()

            # if yes
            if binary_input:
                # read the phrases file
                with open(settings.PHRASES_FILE_PATH, "r+", encoding="utf-8") as phrases_file:
                    phrases_file_data = json.load(phrases_file)

                # add the new phrase to the command list
                phrases_file_data[cmd_title][settings.LANGUAGE]["data"].append(input.lower())

                # write the new list to the file
                with open(settings.PHRASES_FILE_PATH, "r+", encoding="utf-8") as phrases_file:
                    json.dump(phrases_file_data, phrases_file, indent=2, ensure_ascii=False)

                tts.speak(replying.get_reply(["matching", "added"], system=True, module=True))

                cmd = {
                    "name": cmd_time,
                    "text": phrases_file_data[cmd_title][settings.LANGUAGE]["data"][0],
                    "input": input
                }

                return cmd


def google_match(input: str):
    # if not found, google it

    log.debug("Google Search...")

    try:
        cmd_google_search.ex(input)
        cmd = {
            "name": "google",
            "text": input,
            "input": input
        }

        return cmd
    except:
        log.debug("No result from Google Search...")


def get_match(input: str):
    log.debug("Matching...")

    cmd = {
        "name": None,
        "text": None,
        "input": input
    }

    jobs = [check_match, test_match, google_match]

    for job in range(len(jobs)):
        cmd = jobs[job](input)

        if cmd is not None:
            log.debug("Matched command '{0}'".format(cmd["name"]))
            return cmd
        else:
            continue

    log.debug("Couldn't match the command from the input...")


def execute_match(cmd: dict):
    log.debug("Executing command...")

    try:
        if commands.__contains__(cmd["name"]):
            log.debug("Replying...")
            commands.get(cmd["name"]).ex(cmd)
        elif cmd["name"] == "google":
            log.debug("Already executed...")
        else:
            log.error("Couldn't match command script!")
    except TypeError:
        tts.speak(replying.get_reply(["replying", "fail"], system=True, module=True))
