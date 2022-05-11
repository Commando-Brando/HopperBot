from discord.ext import commands
import requests
import json
import random


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
    async def joke(self, ctx):
        response = requests.get(
            "https://geek-jokes.sameerkumar.website/api?format=json")  # https://opentdb.com/api_config.php
        json_data = json.loads(response.text)
        await ctx.send(json_data['joke'])

    @commands.command()
    async def algo(self, ctx):
        await ctx.send(self.get_algos())

    @commands.command()
    async def trivia(self, ctx):
        response = requests.get(
            "https://opentdb.com/api.php?amount=3&category=18&type=multiple")  # https://opentdb.com/api_config.php
        multiple_choice = ['a) ', 'b) ', 'c) ', 'd ']
        choices = []
        json_data = json.loads(response.text)
        question = json_data['results'][0]['question'] + "\n\n"
        answer = json_data['results'][0]['correct_answer']
        # question += answer + "\n"
        for i in range(len(json_data['results'][0]['incorrect_answers'])):
            choices.append(json_data['results'][0]['incorrect_answers'][i])
            # question += choices[i] + "\n"
        choices.append(answer)
        random.shuffle(choices)
        for i in range(len(choices)):
            question += multiple_choice[i] + choices[i] + '\n'

        question += "\nReply with 'a', 'b', 'c', or 'd'\n"
        answer_key = {'a': choices[0], 'b': choices[1], 'c': choices[2], 'd': choices[3]}

        await ctx.send(question)

        def check(message):
            if message.content in {'a', 'b', 'c', 'd'} and answer_key[message.content] == answer:
                return True
            return False

        try:
            msg = await self.bot.wait_for("message", check=check, timeout=60.0)
            await ctx.send("Correct!")
        except:
            await ctx.send("\nTimes up! The answer was " + answer)


def setup(bot):
    bot.add_cog(Utility(bot))
