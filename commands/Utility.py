from discord.ext import commands
import requests
import json

class Utility(commands.Cog):
    algos = [
        ["MergeSort", "Merge.JPG"],
        ["BubbleSort",
         "https://adrianmejia.com/most-popular-algorithms-time-complexity-every-programmer-should-know-free-online"
         "-tutorial-course/#Bubble-sort"],
        ["QuickSort", "https://www.geeksforgeeks.org/quick-sort/"],
        ["HeapSort", "https://www.geeksforgeeks.org/heap-sort/"],
        ["SelectionSort", "https://www.geeksforgeeks.org/selection-sort/"],
        ["RadixSort", "https://www.geeksforgeeks.org/radix-sort/"],
        ["BucketSort", "https://www.geeksforgeeks.org/bucket-sort-2/"]]

    def __init__(self, bot):
        self.bot = bot

    def get_algos(self):
        output = ""
        for line in self.algos:
            output += line[0] + " " + line[1]
            output += "\n"
        return output

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command()
    async def test(self, ctx):
        await ctx.send('This is a test')

    @commands.command()
    async def algo(self, ctx):
        await ctx.send(self.get_algos())

    @commands.command()
    async def trivia(self, ctx):
        response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=multiple") # https://opentdb.com/api_config.php
        json_data = json.loads(response.text)
        question = ""
        for i in range(10):
            question += json_data['results'][i]['question']
        await ctx.send(question)





def setup(bot):
    bot.add_cog(Utility(bot))
