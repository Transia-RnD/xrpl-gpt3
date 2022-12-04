#!/usr/bin/env python
# coding: utf-8

from typing import List
import discord
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ['OPENAPI_KEY']

message_list: List[str] = [
    'For the non tech savy people what is a git ?',
]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def handle_mention_dangell7(self, message):
        from_message: str = message.clean_content.split('@dangell7')[-1].strip()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=from_message,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        response_text: str = response.choices[0]['text']
        message_list.append(response_text)
        await message.channel.send(response_text)

    async def handle_nlp_gpt3(self, message):
        prompt: str = message.clean_content.split('gpt3! ')[-1].strip()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=250,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        response_text: str = response.choices[0]['text']
        message_list.append(response_text)
        await message.channel.send(response_text)

    async def handle_story_gpt3(self, message):
        prompt: str = message.clean_content.split('story! ')[-1].strip()
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.8,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        response_text: str = response.choices[0]['text']
        message_list.append(response_text)
        await message.channel.send(response_text)

    async def handle_anology_gpt3(self, message):
        _prompt: str = message.clean_content.split('anology! ')[-1].strip()
        prompt = 'Create an analogy for this phrase: ' + _prompt
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text: str = response.choices[0]['text']
        message_list.append(response_text)
        await message.channel.send(response_text)

    async def handle_marv_gpt3(self, message):
        _prompt: str = message.clean_content.split('marv! ')[-1].strip()
        prompt = 'Marv is a chatbot that reluctantly answers questions with sarcastic responses:. ' + _prompt
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=60,
            top_p=0.3,
            frequency_penalty=0.5,
            presence_penalty=0
        )
        response_text: str = response.choices[0]['text']
        message_list.append(response_text)
        await message.channel.send(response_text)


    async def handle_coded_gpt3(self, message):
        print('HANDLE: CODE')
        # strip mentions
        # add coding preficits
        prompt: str = message.clean_content.split('code! ')[-1].strip()
        print(prompt)
        response = openai.Completion.create(
          model="code-davinci-002",
          prompt=prompt,
          temperature=0,
          max_tokens=256,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0
        )
        response_text: str = response.choices[0]['text']
        await message.channel.send(response_text)

    async def handle_tldr(self, message):
        cat_message: str = ''
        async for msg in message.channel.history(limit=30):
            cat_message += msg.clean_content + ' '
        
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=cat_message,
            temperature=0.7,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=1
        )
        response_text: str = response.choices[0]['text']
        await message.channel.send(f'tldr: {response_text}')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # dont respond to direct messages
        if not message.channel.guild:
            return

        mention_names: List[str] = [message.name for message in message.mentions]
        if 'dangell7' in mention_names:    
            await self.handle_mention_dangell7(message)
        
        if message.content.startswith('code!'):
            await self.handle_coded_gpt3(message)

        if message.content.startswith('gpt3!'):
            await self.handle_nlp_gpt3(message)

        if message.content.startswith('marv!'):
            await self.handle_marv_gpt3(message)

        if message.content.startswith('story!'):
            await self.handle_story_gpt3(message)

        if message.content.startswith('anology!'):
            await self.handle_anology_gpt3(message)

        if message.content == 'ping':
            await message.channel.send('pong')


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ['DISCORD_APP_KEY'])
