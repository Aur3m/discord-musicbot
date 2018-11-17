import discord
import os
import asyncio
import random
import playlist_splitter as Playlist

path_bot = os.getcwd()

print(u'\n\n\nBot crée par la mernwar\n')

try:
    on = True
    with open(path_bot + '/config.txt', 'r') as fichier:
        texte = fichier.read()
        lignes = texte.split('\n')
        ch1 = lignes[0]
        ch2 = ch1.split('TOKEN=')
        token = ch2[1]
        if token == '':
            on = False
        print('TOKEN = ' + token)
        ch1 = lignes[1]
        ch2 = ch1.split('VOICE CHANNEL=')
        salon = ch2[1]
        if salon == '':
            on = False
        print('SALON = ' + salon)
        ch1 = lignes[2]
        ch2 = ch1.split('PLAYLIST=')
        playlist = ch2[1]
        if playlist == '':
            on = False
        print('PLAYLIST = ' + playlist)
        ch1 = lignes[3]
        ch2 = ch1.split('RANDOM=')
        if ch2[1] == '1':
            Random = True
            print(u'RANDOM ON (mettez 0 pour la désactiver)')
        else:
            Random = False
            print('RANDOM OFF (mettez 1 pour l\'activer)')
except:
    with open(path_bot + '/config.txt', 'w') as fichier:
        fichier.write('TOKEN=(Enter bot\'s token here)\nVOICE CHANNEL=(Enter voice\'s channel ID here)\nPLAYLIST=(Enter playlist\'s URL here)\nRANDOM=0')
        on = False

if on == True:
    channel = discord.Object(id=salon)
    client = discord.Client()
    @client.event
    async def on_ready():
        print(u'\n\nVous êtes connecté avec le compte {0.user}'.format(client) + '\n\n')
        while True:
            try:
                voice = await client.join_voice_channel(channel)
            except:
                pass
            try:
                URL = Playlist.Splitter(playlist)
                if Random == True:
                    random.shuffle(URL)
                for i in range(len(URL)):
                    await asyncio.sleep(0.2)
                    player = await voice.create_ytdl_player(URL[i])
                    player.start()
                    player.volume = 0.5
                    print('Lecture de ' + URL[i])
                    while not player.is_done():
                        await asyncio.sleep(1)
            except:
                print(u'Une erreur est survenue\nRedémarrage du programme...')

    client.run(token)
else:
    print(u'\n\nFICHIER MAL FORMÉ, COMPLÉTEZ LE!!!')