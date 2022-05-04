from discord.ext import commands



class Utility(commands.Cog):
    Algo = (
        ("MergeSort", "Merge.JPG"),
        ("BubbleSort",
         "https://adrianmejia.com/most-popular-algorithms-time-complexity-every-programmer-should-know-free-online"
         "-tutorial-course/#Bubble-sort"),
        ("QuickSort", "https://www.geeksforgeeks.org/quick-sort/"),
        ("HeapSort", "https://www.geeksforgeeks.org/heap-sort/"),
        ("SelectionSort", "https://www.geeksforgeeks.org/selection-sort/"),
        ("RadixSort", "https://www.geeksforgeeks.org/radix-sort/"),
        ("BucketSort", "https://www.geeksforgeeks.org/bucket-sort-2/"))

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')

    @commands.command()
    async def test(self, ctx):
        await ctx.send('This is a test')

def setup(bot):
    bot.add_cog(Utility(bot))
