import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message
from openai import OpenAI

prompt = " " # your prompt tune

bot = Bot(token=" ") # bot's telegram token
dp = Dispatcher()
client = OpenAI(base_url=" ", api_key="not-needed") # standart base_url="http://localhost:1234/v1"
messages = [{'role': 'system', 'content': prompt}]


@dp.message()
async def message(message: types.Message): 
    user_input = message.text
    if message.text != "":
        messages.append({'role': 'user', 'content': user_input})
        response = client.chat.completions.create(
        model="local_model",
        messages=messages,
        temperature=0.9
        
        )
        llm_reply = response.choices[0].message.content
        messages.append({'role': 'assistant', 'content': llm_reply})
          
    else:
        return
    print(llm_reply)
    await message.answer(str(llm_reply))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
