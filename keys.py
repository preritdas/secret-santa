import configparser
import os


current_dir = os.path.dirname(__file__)
keys_path = os.path.join(current_dir, "keys.ini")


keys = configparser.RawConfigParser()
keys.read(keys_path)


class Gmail:
    SENDER = keys["Gmail"]["sender"]
    PASSWORD = keys["Gmail"]["password"]
    SMTP_HOST = keys["Gmail"]["smtp_host"]
    SMTP_PORT = keys["Gmail"]["smtp_port"]
