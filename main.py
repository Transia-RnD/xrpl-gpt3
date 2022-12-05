#!/usr/bin/env python
# coding: utf-8

from typing import List, Dict, Any
import os
import re
from dotenv import load_dotenv

import discord
import openai

load_dotenv()
openai.api_key = os.environ['OPENAPI_KEY']
app_name: str = os.environ['APP_NAME']

message_list: List[Dict[str, Any]] = []

language_map: Dict[str, Any] = {
    'py': 'Python',
    'ts': 'TypeScript',
    'js': 'JavaScript',
    'c': 'C',
    'cs': 'CSharp',
    'c+': 'C+',
    'c++': 'C++',
    'swift': 'Swift',
    'java': 'Java',
}

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def handle_mention_me(self, message):
        try:
            print('handle_mention_me')
            async with message.channel.typing():
                from_message = message.clean_content.replace(f'@{app_name}', '')
                _prompt = 'Human:' + from_message
                prompt = 'Jarvis is a xrpl and rippled decentralized ledger technology developer chatbot that will answer non xrpl questions with sarcastic responses: \n' + _prompt + '\n' + 'AI:'
                print(f'MESSAGE: {prompt}')
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=prompt,
                    temperature=0.9,
                    max_tokens=150,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0.6,
                    stop=[" Human:", "AI:"]
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

    async def handle_translate_gpt3(self, message):
        try:
            print('handle_coded_gpt3')
            # print(message.clean_content)
            content: str = message.clean_content.split('translate! ')[-1].strip()
            regex = r"([a-z]{2}) to ([a-z]{2})" 
            match = re.search(regex, content)

            start_lang = match.group(1)
            end_lang = match.group(2)

            code_regex = r"```((.|\n)*)```"
            match = re.search(code_regex, content)
            start_code = match.group(1)


            prompt = ''
            prompt += f'##### Translate this function from {start_lang} into {end_lang}\n'
            prompt += f'### {start_lang}\n'
            prompt += start_code
            prompt += '\n'
            prompt += f'### {end_lang}\n'

            async with message.channel.typing():
                print(f'MESSAGE: {prompt}')
                response = openai.Completion.create(
                    model="code-davinci-002",
                    prompt=prompt,
                    temperature=0,
                    max_tokens=54,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=["###"]
                )
                response_text: str = '```' + response.choices[0]['text'] + '```'
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

                cat_message += '\n'
                cat_message+= 'Tl;dr'
                
                print(f'MESSAGE: {cat_message}')
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=cat_message,
                    temperature=0.7,
                    max_tokens=300,
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

    async def handle_op(self, message):
        try:
            print('handle_coded_op')
            async with message.channel.typing():
                _prompt: str = message.clean_content.split('op! ')[-1].strip()
                prompt = 'Classify the sentiment in this message: ' + _prompt
                print(f'MESSAGE: {prompt}')
                response = openai.Completion.create(
                    model="code-davinci-002",
                    prompt=prompt,
                    temperature=0,
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

    async def on_message(self, message):
        # don't respond to ourselves
        print(message)
        if message.author == self.user:
            print('AT AUTHOR')
            return

        # dont respond to direct messages
        if not message.channel.guild:
            print('DIRECT MESSAGE')
            return

        mention_names: List[str] = [message.name for message in message.mentions]
        print(mention_names)
        if f'{app_name}' in mention_names and not message.reference:  
            await self.handle_mention_me(message)
        
        if message.content.startswith('code!'):
            await self.handle_coded_gpt3(message, )

        if message.content.startswith('gpt3!'):
            await self.handle_nlp_gpt3(message)

        if message.content.startswith('analogy!'):
            await self.handle_analogy_gpt3(message)

        if message.content.startswith('tldr!'):
            await self.handle_tldr(message)

        if message.content.startswith('op!'):
            await self.handle_op(message)

        if 'translate!' in message.clean_content:
            print('TRANSLATE')
            await self.handle_translate_gpt3(message)

        if message.content == 'ping':
            await message.channel.send('pong')



intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(os.environ['DISCORD_APP_KEY'])

# dict_prompt: Dict[str, Any] = {
#     f'{message.author.name}': response_text
# }
