import discord 
import random
import json


client = discord.Client()

messages = ["K bho muji? Fight garne ho?","wai wai jasto churum chrum khai dinux ma talai!","Randi! New khojeko?","Ma chikne khate", "randi ko bam","Tero mumi ko puti kha randi!","Tero Bau ko lado!","Kera na vako manxe chup lag!"]

gifs = ["https://images-ext-2.discordapp.net/external/43UwjHRWWmAJ9y6MsvhZbz8-Zom5YcZuW2zgWIeb-lQ/https/media.tenor.com/images/4da49d51af9f989e520080b7557e050c/tenor.gif?width=300&height=300","https://tenor.com/view/rajesh-nepal-topi-rajesh-hamal-gif-18658288","https://tenor.com/view/nepali-rajesh-hamal-heyy-angry-gif-13535272"]

lol_text = ["", "K ko lol muji"]

sad_text = ["","Kinw sad? Dw everthing will be fine just be happy :)", ":') SMOILE! you dont look while sad!", "kinw sad? be happy!", "'I just want to make you happy cuz ur the reason I'm happy'"]



@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name="Your mom"))
  print("Loged in as {0.user}".format(client))

@client.event

async def on_message(message):
  if message.author == client.user:
    return
  msg = message.content  
  if message.content.startswith("!updates"):
    await message.channel.send('''
    ```yaml
[UPDATES]
[September 17, 2021] 
[1> Added Random gifs, Added Random answers to "!oi", Added more replies!]
[Tuesday, September 21, 2021]
[1> Added "!praise" feature ]
[2> Improved Proper Random messages! (Which means less repeated gifs and text)]
    ```  
    ''')
   
  if message.content.startswith("!fukmuji"):
   await message.reply(random.choice(gifs))    

  if message.content.startswith("!sahayog"):
    await message.channel.send('''
    ```diff
    Commands:
!sahayog: Help command
!oi: Hello command
!fukmuji: Sends gif
!about: about the bot
!updates: Shows new features!
!fk: sends dig's personal image
!customcmd: used to make custom commands![Use "!customh" for guide]```
    ''')

  if message.content.startswith("!help"):
    await message.channel.send('''
    ```Commands:
!sahayog: Help command
!oi: Hello command
!fukmuji: Sends gif
!about: about the bot
!updates: Shows new features
!fk: sends dig's personal image
!customcmd: used to make custom commands![Use "!customh" for guide```
    ''')  

  if 'lol' in  message.content :
    if random.choice(lol_text) != "":
      await message.reply(lol_text[1])
      

  if ":(" in message.content:
    choice = random.choice(sad_text)
    if choice != "":
      await message.channel.reply(choice)
      
  if message.content.startswith("!about"):
    await message.channel.send('''
    ```
    yaml
    [ABOUT]
    I am a bot created by FuNk#1817
    ```
    ''')  

  if client.user.mentioned_in(message): 
    if "ass" in message.content:
      await message.reply("Ass vanxas? Khate Angreji ladodon ja!") 
    elif "ok" in message.content:
      await message.reply("K ok?")  
    else:
      await message.reply(random.choice(messages))                        
  
  if message.content.startswith("!praise"):
    await message.reply(":thumbsup:")
    await message.reply(":clap:  :open_mouth:")
    await message.reply(":open_mouth: :thumbsup:")
    await message.reply(''':open_mouth: 
:pray:''')

  if message.content.startswith("!fk"):
    await message.reply("https://cdn.discordapp.com/attachments/871339008477757502/889816421704564776/unknown.png")

  if message.content.startswith("!customcmd"):
    msg_splitted = msg.split()
    with open("user_commands.json", "r") as json_file: 
      file = json.load(json_file) 
    user_commanddetail = {"command": msg_splitted[1], "text": msg_splitted[2]}  
    if msg_splitted[1] in file:
      await message.reply("The command already exists!")
    else:
      file.update({msg_splitted[1]: user_commanddetail})  
      with open('user_commands.json', 'w') as json_file:
        json.dump(file,json_file) 
      await message.reply("command created sucessfull!")

  with open("user_commands.json", "r") as json_file: #opens the user_data.json file from the server folder
    file = json.load(json_file) #Loads the data into self.file variable 
  if msg in file:
    await message.channel.send(file[msg]["text"])      

  if message.content.startswith("!customh"):  
   await message.reply('''

```yaml
!customcmd [your_command_symbol] [your_text_or_image_link]
example:
!customcmd !a test
``` 
''')
       

client.run("ODg4MzI0MTQwMTExNjMwNDE2.YURCUw.k4rwWVu3AIdW4Th068cA6-t8wkQ")

