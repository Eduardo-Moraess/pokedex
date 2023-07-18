import requests
import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

load_dotenv()
DISCORD_KEY = os.getenv('DISCORD_KEY')

imgs = {
	'normal': ['https://archives.bulbagarden.net/media/upload/7/73/GO_Normal_M.png',0xA8A77A,'Normal'],
	'fire': ['https://archives.bulbagarden.net/media/upload/d/d6/GO_Fire_M.png',0xEE8130,'Fogo'],
	'water': ['https://archives.bulbagarden.net/media/upload/2/2e/GO_Water_M.png',0x6390F0,'Água'],
	'electric': ['https://archives.bulbagarden.net/media/upload/7/7f/GO_Electric_M.png',0xF7D02C,'Elétrico'],
	'grass': ['https://archives.bulbagarden.net/media/upload/c/cd/GO_Grass_M.png',0x7AC74C,'Grama'],
	'ice': ['https://archives.bulbagarden.net/media/upload/d/dd/GO_Ice_M.png',0x96D9D6,'Gelo'],
	'fighting': ['https://archives.bulbagarden.net/media/upload/7/76/GO_Fighting_M.png',0xC22E28,'Lutador'],
	'poison': ['https://archives.bulbagarden.net/media/upload/2/26/GO_Poison_M.png',0xA33EA1,'Venenoso'],
	'ground': ['https://archives.bulbagarden.net/media/upload/8/8f/GO_Ground_M.png',0xE2BF65,'Terra'],
	'flying': ['https://archives.bulbagarden.net/media/upload/6/6b/GO_Flying_M.png',0xA98FF3,'Voador'],
	'psychic': ['https://archives.bulbagarden.net/media/upload/2/2a/GO_Psychic_M.png',0xF95587,'Psíquico'],
	'bug': ['https://archives.bulbagarden.net/media/upload/8/8c/GO_Bug_M.png',0xA6B91A,'Inseto'],
	'rock': ['https://archives.bulbagarden.net/media/upload/b/b0/GO_Rock_M.png',0xB6A136,'Pedra'],
	'ghost': ['https://archives.bulbagarden.net/media/upload/d/db/GO_Ghost_M.png',0x735797,'Fantasma'],
	'dragon':['https://archives.bulbagarden.net/media/upload/3/3f/GO_Dragon_M.png',0x6F35FC,'Dragão'],
	'dark': ['https://archives.bulbagarden.net/media/upload/c/c9/GO_Dark_M.png',0x705746,'Sombrio'],
	'steel': ['https://archives.bulbagarden.net/media/upload/1/1d/GO_Steel_M.png',0xB7B7CE,'Aço'],
	'fairy': ['https://archives.bulbagarden.net/media/upload/a/a7/GO_Fairy_M.png',0xD685AD,'Fada']
}

class myclient(discord.Client):
    async def on_message(self, message):
        if not message.author.bot:

            mensagem = message.content
            if ('?' in message.content):
                poke = mensagem.replace('?', '')
                url = f'https://pokeapi.co/api/v2/pokemon/{poke}'

                response = requests.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    fotopokemon = data['sprites']['other']['official-artwork']['front_default']
                    nomepokemon = data['name']
                    
                    tiposdokemon = []
                    if len(data['types']) > 1:
                        tiposdokemon = data['types'][0]['type']['name'],data['types'][1]['type']['name']
                        embed = discord.Embed (title = nomepokemon.capitalize(), description = f'Este pokemon é dos tipos:', colour=imgs[tiposdokemon[0]][1])  
                        embed.add_field(name=f'•{imgs[tiposdokemon[0]][2]}', value='' , inline=False)                        
                        embed.add_field(name=f'•{imgs[tiposdokemon[1]][2]}', value='' , inline=False)
                        embed.set_thumbnail(url=imgs[tiposdokemon[0]][0])

                    else:
                        tiposdokemon = data['types'][0]['type']['name']
                        embed = discord.Embed (title = nomepokemon.capitalize(), description = f'Este pokemon é do tipo:', colour=imgs[tiposdokemon][1])  
                        embed.add_field(name=f'•{imgs[tiposdokemon][2]}', value='' , inline=False)                        
                        embed.set_thumbnail(url=imgs[tiposdokemon][0])

                    embed.set_image(url = fotopokemon)
                    embed.set_footer(text = 'Essa informação veio da pokeApi', icon_url = 'https://raw.githubusercontent.com/PokeAPI/media/master/logo/pokeapi_256.png')
                    # embed.set_thumbnail(pokeicon)

                    await message.channel.send (embed = embed)
                
                else:
                    await message.channel.send('não encontrei esse pokemon, tente outro, por favor? :(')
                    
            

client = myclient(intents=intents)
client.run(DISCORD_KEY)
