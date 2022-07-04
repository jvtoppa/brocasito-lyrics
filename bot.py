import discord
from discord.ext import commands
import lyricsgenius as lg
import asyncio
from io import BytesIO

bot = commands.Bot(command_prefix = '!')

artistas_list = []

genius = lg.Genius('EeTU39_jxfWIWEKpgCtIZQiVcQg4cC_-NSzi8xPAlryta-oj7UfCQLEzyd4oewDx', skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True)

@bot.command()
async def procurar(ctx, *, musica):

    songs = genius.search_song(musica, 'brocasito')
    
    s = songs.lyrics

    as_bytes = map(str.encode, s)
    content = b''.join(as_bytes)
    

    print(len(s))
    await ctx.send(file=discord.File(BytesIO(content), 'lyrics.txt'))




bot.run('OTkzMzY3MDQ5NjUwODM1NDg3.GZ4_I8.D7ZLzzVCG3ox_fzLIRuZfHA105-I1600z-LpQQ')


