# sambotto-slackbotto

Sambotto is a simple tutorial-styled slack bot that uses Slack's [RTM](https://api.slack.com/rtm) to respond to in channel messages with some basic actions.

## Setup

### Requirements

- Python3
- Slackclient (found in [requirements.txt](requirements.txt))
- A Slack Bot user

### Installation

1. Follow the instructions to create a [classic app](https://api.slack.com/apps?new_classic_app=1), install it into your workspace (you'll have to add [scopes](https://api.slack.com/authentication/basics#scopes) to it; remember, it **needs to be a CLASSIC APP or RTM won't work**!)
2. Clone this repository `git clone https://github.com/samuele-mattiuzzo/sambotto-slackbotto.git` and cd into the new directory
3. Copy `config.ini.example` to `config.ini` and copy the APP's BOT_TOKEN (without double-quotes)
4. Create a virtualenv `python3 -m venv .env`
5. Activate the virtualenv `source .env/bin/activate`
6. Install the dependencies `python3 -m pip install -r requirements.txt`

## Usage

From your terminal, simply run `python3 slackbot.py` and interact with the bot in the channel you've invited it to!

If you don't know how to start, simply type `help` in the channel and follow the bot's instructions.
