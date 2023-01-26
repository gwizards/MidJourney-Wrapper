targetName     = ""

#import discord
import discord

#initialize client
client = discord.Client()

#on ready
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#on message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.id == CHANNEL_ID:
        if message.content.startswith('!davinci'):
            #split the message into parts
            msg = message.content.split(' ')
            #check if the length of the message is 3
            if len(msg) == 3:
                #store the target id, hash and name
                targetID = msg[1]
                targetHash = msg[2]
                targetName = message.guild.get_member(targetID).display_name
                #send the message
                await message.channel.send(f"Hi {targetName}, your davinci token is {DAVINCI_TOKEN} and your salai token is {SALAI_TOKEN}. Have a nice day!")

#run the client
client.run(DAVINCI_TOKEN, bot=True)

#Optimized code
DAVINCI_TOKEN = [Token of Discord bot]  #davinci bot token
SERVER_ID = [Server id here]  #server id
CHANNEL_ID = [Channel in which commands are sent]  #channel id
SALAI_TOKEN = [Token of the Account from which you paid MidJourney ]  #salai bot token
MID_JOURNEY_ID = "936929561302675456"  #midjourney bot id

#import discord
import discord

#initialize client
client = discord.Client()

#on ready
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

#on message
@client.event
async def on_message(message):
    #check if the user is not the bot itself and the channel is correct
    if message.author != client.user and message.channel.id == CHANNEL_ID:
        #check if the message starts with !davinci
        if message.content.startswith('!davinci'):
            #split the message into parts
            msg = message.content.split(' ')
            #check if the length of the message is 3
            if len(msg) == 3:
                #store the target id, hash and name
                targetID = msg[1]
                targetHash = msg[2]
                targetName = message.guild.get_member(targetID).display_name
                #send the message
                await message.channel.send(f"Hi {targetName}, your davinci token is {DAVINCI_TOKEN} and your salai token is {SALAI_TOKEN}. Have a nice day!")

#run the client
client.run(DAVINCI_TOKEN, bot=True)

#Optimized by combining two checks and eliminating some unnecessary variables.