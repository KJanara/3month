from aiogram import types, dispatcher
from config import bot
from keyboards.inline_buttons import quesionnaire_one_keybords

async def start_quesionnaire(call: types.callback_query):
  print(call)
  await bot.send_message(
    chat_id=call.message.chat.id,
    text="Do you want to go on a trip?",
    reply_markup=await quesionnaire_one_keybords()
  )


async def yes_answer(call: types.callback_query):
  await bot.send_message(
    chat_id=call.message.chat.id,
    text="You'll have a trip soon",
  )


async def no_answer(call: types.callback_query):
  await bot.send_message(
    chat_id=call.message.chat.id,
    text="Don't forget to take a break",
  )

def reqister_callback_handlers(dp: dispatcher):
  dp.register_callback_query_handler(start_quesionnaire,
                                      lambda call: call.data == "start_quesionnaire")
  dp.register_callback_query_handler(yes_answer,
                                     lambda call: call.data == "yes_trip")
  dp.register_callback_query_handler(no_answer,
                                     lambda call: call.data == "no_trip")
