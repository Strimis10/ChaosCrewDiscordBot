###Code stol..ehm, loaned from:
### https://www.youtube.com/watch?v=46ZHJcNnPJ8 / https://github.com/alphascriptyt/Discord_Rewrite_Tutorials/blob/master/episodes/episode-16.py




import asyncio
from discord_slash import cog_ext, SlashContext
from discord.ext import commands
import discord
import discord.utils
import youtube_dl
import pafy
import os
from please_wait import please_wait
import random

class music(commands.Cog):
    def __init__(self, bot):
        import what_server
        if what_server.Kennevo:
            guild_id = 786013884216639509
        else:
            guild_id = 932684556572700773
        self.bot = bot
        self.song_queue = {932684556572700773:[], 786013884216639509:[]}
        
    


        


    
        
    async def check_queue(self, ctx):
        print(self.song_queue)
        if len(self.song_queue[ctx.guild.id]) > 0:
            await self.play_song(ctx, self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)
            print(self.song_queue)
            

    

    async def search_song(self, amount, song, get_url=False):
        

        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            "source_address":"144.126.210.176"
        }],
}
        info = youtube_dl.YoutubeDL(ydl_opts).extract_info(f"ytsearch{amount}:{song}", download=False, ie_key="YoutubeSearch")
        
        # print(info["entries"])
        #print(entry["webpage_url"] for entry in info["entries"])
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.bot.loop.create_task(self.check_queue(ctx))) 
        ctx.voice_client.source.volume = 0.3
    
    @cog_ext.cog_slash(name="Play", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def Play(self, ctx: SlashContext, search:str):
        member = ctx.guild.get_member(932687176997687316)


        message = await ctx.send(random.choice(please_wait))
        if ctx.author.voice is None:
            return await message.edit(content="You are not connected to any voice channel.")
        channel = ctx.author.voice.channel
        
        try:
            users = member.voice.channel.members
            if len(users) == 1:
                await channel.disconnect()
        except:
            pass
        try:
            await channel.connect()

        except discord.errors.ClientException:
            pass


    
        song = search
        in_urlls = False
        voice = ctx.voice_client
        urls = ["youtube.com/watch?","https://youtu.be/"] 
        Kennevo_rough = ["kennevo rough", "kenny rough", "tizzy kenny song", "tizzy song", "kenny axe dance"]
        for urll in urls:
            if urll in song:
                in_urlls = True

        if song.lower() in Kennevo_rough:
            song = "https://youtu.be/07RFyusfEM8"


            
        elif not in_urlls:

            
            result = await self.search_song(amount=1, song=search, get_url=True)
            #result = str(result)
            print(result)
            song_name = song
            try:
                song = result[0]
                print(song)

                if result is None:
                    await message.edit(content=f"No matches for {song_name}")
            except TypeError:
                await message.edit(content=f"No matches for {song_name}")

        

        

        if ctx.voice_client.source is not None:
            print("in the queue system")
            queue_len = len(self.song_queue[ctx.guild.id])

            if queue_len < 10:
                self.song_queue[ctx.guild.id].append(song)
                return await message.edit(content=f"song added to queue at position {queue_len+1}.")
            elif ctx.author.id == 427822985102098434:
                self.song_queue[str(ctx.guild.id)].append(song)
                return await message.edit(content=f"song added to queue at position {queue_len+1}.")
            else:
                return await message.edit(content=f"Only 10 songs can be placed in the queue, please wait for the current song to finish")
        
        
            
        await self.play_song(ctx, song)
        embed = discord.Embed(title="Now playing:", colour=0x3c005a)
        embed.set_footer(text=song)
        await message.edit(embed=embed)

        

    @cog_ext.cog_slash(name="queue", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def queue(self, ctx: SlashContext):
        if len(self.song_queue[ctx.guild.id]) == 0:
            return await ctx.send("There are currently no songs in the queue.")

        embed = discord.Embed(title="Song Queue", description="", colour=discord.Colour.dark_gold())
        i = 1
        for url in self.song_queue[ctx.guild.id]:
            embed.description += f"{i}) {url}\n"

            i += 1

        
        await ctx.send(embed=embed)

        
    @cog_ext.cog_slash(name="disconnect", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def disconnect(self, ctx: SlashContext):
        try:
            await ctx.voice_client.disconnect()
            await ctx.send("disconnected from the voice channel")
        except:
            await ctx.send("Dave is not in any voice channel")
    
    @cog_ext.cog_slash(name="Pause_music", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def Pause_music(self, ctx: SlashContext):
        voice = ctx.voice_client
        if voice.is_playing():
            voice.pause()
            await ctx.send("Paused")
        else:
            await ctx.send("There is no music to pause")
    
    @cog_ext.cog_slash(name="resume_music", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def resume_music(self, ctx: SlashContext):
        voice = ctx.voice_client
        try:
            if voice.is_paused():
                voice.resume()
                await ctx.send("Resumed")
            else:
                await ctx.send("There is no music to resume")
        except AttributeError:
            await ctx.send("There is no music to resume")

    @cog_ext.cog_slash(name="Stop_music", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def Stop_music(self, ctx: SlashContext):
        voice = ctx.voice_client
        if voice.is_playing():
            voice.stop()
            await ctx.send("Music stopped")
            await ctx.voice_client.disconnect()
        else:
            await ctx.send("There is no music to Stop")
    
    @cog_ext.cog_slash(name="skip_song", description="",guild_ids=[932684556572700773,786013884216639509,983015288910000188])
    async def skip(self, ctx: SlashContext):
        if ctx.voice_client is None:
            return await ctx.send("No song to skip.")

        if ctx.author.voice is None:
            return await ctx.send("You are not connected to any voice channel.")

        if ctx.author.voice.channel.id != ctx.voice_client.channel.id:
            return await ctx.send("I am not currently playing any songs for you.")

        poll = discord.Embed(title=f"Vote to Skip Song by - {ctx.author.name}#{ctx.author.discriminator}", description="**80% of the voice channel must vote to skip for it to pass.**", colour=discord.Colour.blue())
        poll.add_field(name="Skip", value=":white_check_mark:")
        poll.add_field(name="Stay", value=":no_entry_sign:")
        poll.set_footer(text="Voting ends in 5 seconds.")

        poll_msg = await ctx.send(embed=poll) # only returns temporary message, we need to get the cached message to get the reactions
        poll_id = poll_msg.id

        await poll_msg.add_reaction(u"\u2705") # yes
        await poll_msg.add_reaction(u"\U0001F6AB") # no
        
        await asyncio.sleep(5) # 5 seconds to vote

        poll_msg = await ctx.channel.fetch_message(poll_id)
        
        votes = {u"\u2705": 0, u"\U0001F6AB": 0}
        reacted = []

        for reaction in poll_msg.reactions:
            if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
                async for user in reaction.users():
                    if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
                        votes[reaction.emoji] += 1

                        reacted.append(user.id)

        skip = False

        if votes[u"\u2705"] > 0:
            if votes[u"\U0001F6AB"] == 0 or votes[u"\u2705"] / (votes[u"\u2705"] + votes[u"\U0001F6AB"]) > 0.79: # 80% or higher
                skip = True
                embed = discord.Embed(title="Skip Successful", description="***Voting to skip the current song was succesful, skipping now.***", colour=discord.Colour.green())

        if not skip:
            embed = discord.Embed(title="Skip Failed", description="*Voting to skip the current song has failed.*\n\n**Voting failed, the vote requires at least 80% of the members to skip.**", colour=discord.Colour.red())

        embed.set_footer(text="Voting has ended.")

        await poll_msg.clear_reactions()
        await poll_msg.edit(embed=embed)

        if skip:
            ctx.voice_client.stop()
    

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
    
        if not member.id == self.bot.user.id:
            return

        elif before.channel is None:
            voice = after.channel.guild.voice_client
            time = 0
            while True:
                await asyncio.sleep(1)
                time = time + 1
                if voice.is_playing() and not voice.is_paused():
                    time = 0
                if time == 120:
                    await voice.disconnect()
                if not voice.is_connected():
                    break

        


def setup(bot):
    bot.add_cog(music(bot))