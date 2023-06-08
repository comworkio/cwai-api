import os
import requests
import logging
import json
import sys

from utils.common import is_not_empty, is_true

LOG_LEVEL = os.environ['LOG_LEVEL']
SLACK_TRIGGER = os.environ['SLACK_TRIGGER']
LOG_FORMAT = os.getenv('LOG_FORMAT')

def slack_message(log_level, message, is_public):
    if is_true(SLACK_TRIGGER):
        token = os.getenv('SLACK_TOKEN')
        if is_public and is_not_empty(os.getenv('SLACK_TOKEN_PUBLIC')):
            if is_not_empty(token):
                slack_message(log_level, message, False)
            token = os.environ['SLACK_TOKEN_PUBLIC']

        data = { "attachments": [{ "color": get_color_level(log_level), "text": message, "title": log_level }], "username": os.environ['SLACK_USERNAME'], "channel": os.environ['SLACK_CHANNEL'], "icon_emoji": os.environ['SLACK_EMOJI'] }
        requests.post("https://hooks.slack.com/services/{}".format(token),json=data)

def discord_message(log_level, message, is_public):
    if is_true(SLACK_TRIGGER):
        token = os.getenv('DISCORD_TOKEN')
        if is_public and is_not_empty(os.getenv('DISCORD_TOKEN_PUBLIC')):
            if is_not_empty(token):
                discord_message(log_level, message, False)
            token = os.environ['DISCORD_TOKEN_PUBLIC']

        data = { "text": "[{}] {}".format(log_level, message), "username": os.environ['SLACK_USERNAME'] }
        requests.post("https://discord.com/api/webhooks/{}/slack".format(token),json=data)

def is_level_partof(level, levels):
    return any(l == "{}".format(level).lower() for l in levels)

def is_debug(level):
    return is_level_partof(level, ["debug", "notice"])

def is_warn(level):
    return is_level_partof(level, ["warning", "warn"])

def is_error(level):
    return is_level_partof(level, ["error", "fatal", "crit"])

def get_color_level(level):
    if is_debug(level):
        return "#D4D5D7"
    elif is_warn(level):
        return "#FDCB94"
    elif is_error(level):
        return "#D80020"
    else:
        return "#95C8F3"

def get_int_value_level(level):
    if is_debug(level):
        return 0
    elif is_warn(level):
        return 2
    elif is_error(level):
        return 3
    else:
        return 1

if is_debug(LOG_LEVEL):
    logging.basicConfig(stream=sys.stdout, level="DEBUG")
elif is_warn(LOG_LEVEL):
    logging.basicConfig(stream=sys.stdout, level="WARNING")
elif is_error(LOG_LEVEL):
    logging.basicConfig(stream=sys.stderr, level="ERROR")
else:
    logging.basicConfig(stream=sys.stdout, level="INFO")

def quiet_log_msg (log_level, message):
    formatted_log = "[{}] {}".format(log_level, message)
    if is_not_empty(LOG_FORMAT) and LOG_FORMAT == "json":
        formatted_log = json.dumps({"body": message, "level": log_level})

    if is_debug(log_level):
        logging.debug(formatted_log)
    elif is_warn(log_level):
        logging.warning(formatted_log)
    elif is_error(log_level):
        logging.error(formatted_log)
    else:
        logging.info(formatted_log)

def log_msg(log_level, message, is_public = False):
    quiet_log_msg (log_level, message)

    if get_int_value_level(log_level) >= get_int_value_level(LOG_LEVEL):
        slack_message(log_level, message, is_public)
        discord_message(log_level, message, is_public)
