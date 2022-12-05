#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Any
import discord
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.environ['OPENAPI_KEY']

message_list: List[Dict[str, Any]] = []

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def handle_mention_me(self, message):
        try:
            print('handle_mention_me')
            async with message.channel.typing():
                print(f'MESSAGE: {message.clean_content}')
                from_message: str = message.clean_content.split('@xrpl-gpt3')[-1].strip()
                _prompt = 'Human: ' + from_message
                prompt = 'Jarvis is a xrpl and rippled decentralized ledger technology developer chatbot that will answer non xrpl questions with sarcastic responses: ' + _prompt
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    temperature=0.9,
                    max_tokens=150,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0.6,
                    stop=[" Human:"]
                )
                if response.choices[0]['text'] is None:
                    raise ValueError('I had an error')
                
                response_text: str = response.choices[0]['text']
                await message.channel.send(response_text)
        except Exception as e:
            await message.channel.send(str(e))


    async def handle_nlp_gpt3(self, message):
        try:
            print('handle_nlp_gpt3')
            async with message.channel.typing():
                prompt: str = message.clean_content.split('gpt3! ')[-1].strip()
                print(f'MESSAGE: {prompt}')
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    temperature=0.9,
                    max_tokens=250,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0.6
                )
                if response.choices[0]['text'] is None:
                    raise ValueError('I had an error')
                
                response_text: str = response.choices[0]['text']
                await message.channel.send(response_text)
        except Exception as e:
            await message.channel.send(str(e))

    async def handle_analogy_gpt3(self, message):
        try:
            print('handle_analogy_gpt3')
            async with message.channel.typing():
                _prompt: str = message.clean_content.split('analogy! ')[-1].strip()
                prompt = 'Create an analogy for this phrase: ' + _prompt
                print(f'MESSAGE: {prompt}')
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    temperature=0.5,
                    max_tokens=60,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                if response.choices[0]['text'] is None:
                    raise ValueError('I had an error')
                
                response_text: str = response.choices[0]['text']
                await message.channel.send(response_text)
        except Exception as e:
            await message.channel.send(str(e))

    async def handle_coded_gpt3(self, message):
        try:
            print('handle_coded_gpt3')
            async with message.channel.typing():
                prompt: str = message.clean_content.split('code! ')[-1].strip()
                print(f'MESSAGE: {prompt}')
                response = openai.Completion.create(
                    model="code-davinci-002",
                    prompt=prompt,
                    temperature=0,
                    max_tokens=400,
                    top_p=1,
                    frequency_penalty=0.5,
                    presence_penalty=0,
                )
                if response.choices[0]['text'] is None:
                    raise ValueError('I had an error')
                
                response_text: str = response.choices[0]['text']
                await message.channel.send(response_text)
        except Exception as e:
            await message.channel.send(str(e))

    async def handle_tldr(self, message):
        try:
            print('handle_tldr')
            async with message.channel.typing():
                cat_message: str = ''
                async for msg in message.channel.history(limit=30):
                    cat_message += msg.clean_content + ' '
                
                print(f'MESSAGE: {cat_message}')
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=cat_message,
                    temperature=0.7,
                    max_tokens=60,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=1
                )
                if response.choices[0]['text'] is None:
                    raise ValueError('I had an error')
                
                response_text: str = response.choices[0]['text']
                await message.channel.send(response_text)
        except Exception as e:
            await message.channel.send(str(e))

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            print('AT AUTHOR')
            return

        # dont respond to direct messages
        if not message.channel.guild:
            print('DIRECT MESSAGE')
            return

        mention_names: List[str] = [message.name for message in message.mentions]
        if 'xrpl-gpt3' in mention_names and not message.reference:  
            await self.handle_mention_me(message)
        
        if message.content.startswith('code!'):
            await self.handle_coded_gpt3(message, )

        if message.content.startswith('gpt3!'):
            await self.handle_nlp_gpt3(message)

        if message.content.startswith('analogy!'):
            await self.handle_analogy_gpt3(message)

        if message.content == 'ping':
            await message.channel.send('pong')



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ['DISCORD_APP_KEY'])

# dict_prompt: Dict[str, Any] = {
#     f'{message.author.name}': response_text
# }
