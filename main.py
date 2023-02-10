import openai
import discord
import os
import random
import time

# Load the GPT-3 model
openai.api_key = ''
model_engine = "text-davinci-002"
# Create new discord client agent
JoeGPT = discord.Client()
os.environ['token'] = ''
my_secret = os.environ['token']
beep_boop = ["beep", "boop", "beep", "boop", "beep"]

def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
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
    query = message.content.strip()
    # ignore messages from itself
    if message.author == JoeGPT.user:
        if "Systems processing..." in query:
            time.sleep(2)
            await message.delete()
        else:
            return

    elif "!joebot" in query:
        random.shuffle(beep_boop)
        GPT_response = generate_text(query).replace('?', '')
        await message.channel.send(f'Systems processing... {beep_boop[0]} {beep_boop[1]} {beep_boop[2]} {beep_boop[3]} {beep_boop[4]}')
        time.sleep(2)
        await message.channel.send(f' {GPT_response}')

# token confirmation to communicate with Discord API
JoeGPT.run(my_secret)
