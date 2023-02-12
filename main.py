import openai
import discord
import os
import random
import time

# Load the GPT-3 model
os.environ['openai_key'] = ''
openai.api_key = os.environ['openai_key']
# Create new discord client agent
JoeGPT = discord.Client()
os.environ['discord_token'] = ''
discord_token = os.environ['discord_token']
beep_boop = ["beep", "boop", "beep", "boop", "beep"]
manual_mode = False
owner_id = "Kony2012#3449"
# hub_server = JoeGPT.get_guild(961311552907149365)
# manual_channel = JoeGPT.get_channel(1074146975496273950)

# get GPT response
def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

# Verify Bot is connected and ready
@JoeGPT.event
async def on_ready():
    print("JoeBot is beeping and booping\n")
    print("--------------------------------------")

# When a message is posted in any channel
@JoeGPT.event
async def on_message(message):
    global manual_mode
    query = message.content.strip()
    # handle message from itself
    if message.author == JoeGPT.user:
        if "Systems processing..." in query:
            time.sleep(2)
            await message.delete()
        else:
            return
    # get current mode
    elif str(message.author) == owner_id and "!mode" in query:
        if manual_mode:
            current_mode = "Current Mode = Manual"
        else:
            current_mode = "Current Mode = Auto"
        print(current_mode)

    # change to manual mode
    elif str(message.author) == owner_id and "!manual" in query:
        manual_mode = True
        print("Operating in Manual Mode...")
    # change to auto mode
    elif str(message.author) == owner_id and "!auto" in query:
        manual_mode = False
        print("Operating in Auto Mode...")

    # respond to query
    elif message.author != JoeGPT.user and "!joegpt" in query:
        query = query[7::]
        query_user = message.author
        print(f'FROM{query_user}-> {query}')
        random.shuffle(beep_boop)
        processing_message = f'Systems processing...{beep_boop[0]} {beep_boop[1]} {beep_boop[2]} {beep_boop[3]} {beep_boop[4]}'
        # auto mode
        if not manual_mode:
            GPT_response = generate_text(query).replace('?', '')
            await message.channel.send(processing_message)
            time.sleep(2)
            await message.channel.send(f' {GPT_response}')
            print(f'\nRESPONSE:{GPT_response}\n------------------------------------------')
        # manual mode
        elif manual_mode:
            await message.channel.send(processing_message)
            print(f'Query from {query_user}:\n "{query}"')
            manual_response = input("Enter a response->")
            await message.channel.send(f' {manual_response}')

# token confirmation to communicate with Discord API
JoeGPT.run(discord_token)
