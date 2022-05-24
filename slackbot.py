import configparser

from slack import RTMClient

import actions

conf = configparser.ConfigParser()


def get_bot_token():
    conf.read("config.ini")
    return str(conf.get("ACCESS", "TOKEN"))


@RTMClient.run_on(event="message")
def sambotto(**payload):
    """
    This function triggers when someone sends
    a message on the slack
    """
    data = payload["data"]
    web_client = payload["web_client"]
    bot_id = data.get("bot_id", None)

    # If a message was not send by the bot
    if not bot_id:
        channel_id = data.get("channel")

        # Extracting message sent by the user on slack
        text = data.get("text", "")
        text = text.split(">")[-1].strip()

        if "help" in text.lower():
            # helptext
            user = data.get("user", "I")
            response = "Hi <@{}>! I am Sambotto :)\r\n".format(user) + actions.help()

        elif "flip" in text.lower():
            # flip a coin
            user = data.get("user", "I")
            response = actions.flip(user)

        else:
            # ?!?!
            response = None

        if response:
            # Sending message back to slack
            web_client.chat_postMessage(channel=channel_id, text=response)


if __name__ == "__main__":
    try:
        _auth_token = get_bot_token()
        print("Found auth token: {}".format(_auth_token))
        rtm_client = RTMClient(token=_auth_token)
        print("Bot is up and running!")
        rtm_client.start()
        print("Bot has gone sleepy...")
    except Exception as err:
        print(err)
