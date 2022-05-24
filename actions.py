import random

COMMANDS = [
    ("__help__", "shows a list of available commands"),
    ("__flip__", "flips a coin"),
]


def flip(user):
    results = "heads" if not random.randint(0, 1) else "tails"
    return "<@{}> flips a :coin:... and it's {}! Huzzah!".format(user, results)


def help():
    rsp = "Currently I support the following commands:\r\n"

    for command in COMMANDS:
        rsp += "- {}: {}".format(command[0], command[1]) + "\r\n"

    return rsp
