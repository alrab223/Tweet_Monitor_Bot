import asyncio
import os
import re

from discord.ext import commands

from cog.util import thread_webhook as webhook
from cog.util import tweet_stream
from cog.util.DbModule import DbModule as db


class TweetMonitor(commands.Cog):

   def __init__(self, bot):
      self.bot = bot
      self.tweet_wait = False
      self.db = db()

   async def tweet_send(self, ctx):
      while self.db.select("select *from flag_control where flag_name='tweet_get'")[0]["flag"] == 1:
         try:
            tweet = self.db.select("select *from Twitter_log limit 1")[0]
            self.db.delete("Twitter_log", {"tweet_id": tweet["tweet_id"]})
         except IndexError:
            await asyncio.sleep(2)
            continue
         urls = []
         medias = ["media1", "media2", "media3", "media4"]
         for media in medias:
            if tweet[media] is not None:
               urls.append(tweet[media])
            else:
               break
         pattern = "https?://[\\w/:%#\\$&\\?\\(\\)~\\.=\\+\\-]+"
         url_flag: list = re.findall(pattern, tweet["text"])
         if url_flag != []:
            tweet["text"] = re.sub(pattern, "", tweet["text"])
            tweet["text"] += "```\nURLが含まれているツイートです。URL先で確認して下さい```"

         payload = webhook.payload_edit(tweet["user"], tweet["icon"], tweet["text"], urls)
         url = f"https://twitter.com/{tweet['screen_id']}/status/{tweet['tweet_id']}"
         payload["embeds"].append({"title": "ツイート先に飛ぶ", "url": url})
         Ch_webhook = await webhook.get_webhook(ctx)
         webhook.custom_send(payload, Ch_webhook.url, ctx)
         await asyncio.sleep(2)

   # @commands.has_role("テスター") 権限を設定する場合
   @commands.slash_command(name="ツイート取得")
   async def tweet_get(self, ctx, word: str):
      """ツイートを取得してここに垂れ流します"""
      if self.db.select("select *from flag_control where flag_name='tweet_get'")[0]["flag"] == 1:
         await ctx.respond("すでにこの機能が使用されているため、現在使えません")
         return
      self.db.delete("Twitter_log")
      tweet_stream.main(word)
      self.db.update("flag_control", {"flag": 1}, {"flag_name": "tweet_get"})
      await ctx.respond(f"{word}でツイート取得を開始します")
      await self.tweet_send(ctx)

   @commands.slash_command(name="ツイート取得停止")
   async def tweet_get_stop(self, ctx):
      """ツイート取得を停止します"""
      self.db.update("flag_control", {"flag": 0}, {"flag_name": "tweet_get"})
      await ctx.respond("ツイート取得を停止しました")

   @commands.Cog.listener()
   async def on_application_command_error(self, ctx, error):
      if isinstance(error, (commands.MissingRole, commands.MissingAnyRole, commands.CheckFailure)):
         await ctx.reply("権限がありません")
      else:
         print(error)


def setup(bot):
   bot.add_cog(TweetMonitor(bot))
