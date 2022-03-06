import discord
from random import *
import asyncio

#iniciar o bot
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        
        #par ou ímpar
        if message.content == 'par ou ímpar':
          await message.channel.send('Escolhe ae:\n[ ]Par\n[ ]Ímpar')

          def is_correct(m):
            return m.author == message.author

          try:
            escolha = await self.wait_for('message', check=is_correct, timeout=30.0)
          except asyncio.TimeoutError:
            return await message.channel.send('Opa, demorou demais aí pra responder')
          
          if escolha.content == 'par' or escolha.content == 'Par':
            await message.channel.send('Ok, então vou de Ímpar')
            await message.channel.send('Que número vai escolher?')

            def is_correct(m):
              return m.author == message.author and m.content.isdigit()

            try:
              escolha = await self.wait_for('message', check=is_correct, timeout=30.0)
            except asyncio.TimeoutError:
              return await message.channel.send('Opa, demorou demais aí pra responder')

            comput = randint(1,10)
            soma = int(escolha.content) + comput

            await message.channel.send('=='*15+'\nVocê jogou {}\nO computador jogou {}\nA soma deu {}\n'.format(escolha.content,comput,soma)+'=='*15)

            if (soma % 2) == 0:
              await message.channel.send('Você ganhou!! 🎉')
            else:
              await message.channel.send('Você perdeu ✊')

          if escolha.content == 'impar' or escolha.content == 'Ímpar' or escolha.content == 'ímpar' or escolha.content == 'Ímpar':
            await message.channel.send('Ok, então vou de Par')
            await message.channel.send('Que número vai escolher?')

            def is_correct(m):
              return m.author == message.author and m.content.isdigit()

            try:
              escolha = await self.wait_for('message', check=is_correct, timeout=30.0)
            except asyncio.TimeoutError:
              return await message.channel.send('Opa, demorou demais aí pra responder')

            comput = randint(1,10)
            soma = int(escolha.content) + comput

            await message.channel.send('=='*15+'\nVocê jogou {}\nO computador jogou {}\nA soma deu {}\n'.format(escolha.content,comput,soma)+'=='*15)

            if (soma % 2) == 1:
              await message.channel.send('Você ganhou!! 🎉')
            else:
              await message.channel.send('Você perdeu ✊')
              
#autenticação
client = MyClient()
client.run('TOKEN')
