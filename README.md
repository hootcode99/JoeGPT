# JoeGPT

## What is this?
I wanted to learn more about leveraging the OpenAI API for GPT in Python. \
I also wanted to learn more about building a Discord bot (as a developer who is active on Discord alot). \
So merging the two interests into 1 project seems appropriate.

The bot is named JoeGPT as it is a running joke in the discord server I deployed it in that my youngest brother Joseph can sometimes act like a bot. :)

## What is it built on?
### OpenAI Python API

https://openai.com/blog/openai-api

This script leverages GPT-3.5 through the OpenAI Python API. One can simply make a developer account with OpenAI here to recieve an API key. You receive a generous amount of submission tokens for free.
Though, since this bot was used by multiple people several times a day, I did exhaust my free access.

### Discord Python API
https://discordpy.readthedocs.io/

This is the Python Discord API handler. I absolutely love the simplicity and think it's probably the best option.

You will need to obtain you API keys and configuration (for free) here: https://discord.com/developers

### Repl.it
Initially, I hosted this bot on https://replit.com/ wrapped in a Flask app since Repl.it will allow you to host simple websites for free. 
Later, I ended up building a home server and moved the deployment there.

## How does it work?

The bot begins by consuming your supplied Discord API keys and tokens. After that, it is simply a discord interface to GPT-3.5. 
The bot triggers on each message in the server in any channel. It ignores all messages from itself, checks each other new message 
for the command flag "!joegpt", and makes sure the query isn't too long (which would burn tokens faster). 
Similar to my Facebook Messenger bot, I did implement a manual mode here as wwell to have a little fun after our free OpenAI tokens ran out.
Every interaction is logged to a terminal for monitoring and debugging purposes.
