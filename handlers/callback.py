from aiogram import types, dispatcher
from config import bot
from keyboards.inline_buttons import quesionnaire_one_keybords
# from scraping.async_m_scraper import NewMoviesScraper

async def start_quesionnaire(call: types.callback_query):
  print(call)
  await bot.send_message(
    chat_id=call.message.chat.id,
    text="Do you want to go on a trip?",
    reply_markup=await quesionnaire_one_keybords()
  )


async def yes_answer(call: types.callback_query):
  await bot.edit_message_text(
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    text="You'll have a trip soon",
  )


async def no_answer(call: types.callback_query):
  await bot.edit_message_text(
    chat_id=call.message.chat.id,
    message_id=call.message.message_id,
    text="Don't forget to take a break",
  )


# async def latest_movies(call: types.callback_query):
#   scraper = NewMoviesScraper()
#   links = scraper.parse_page()
#   for link in links:
#     await bot.send_message(
#       chat_id=call.message.chat.id,
#       text=link
#     )

def reqister_callback_handlers(dp: dispatcher):
  dp.register_callback_query_handler(start_quesionnaire,
                                     lambda call: call.data == "start_quesionnaire")
  dp.register_callback_query_handler(yes_answer,
                                     lambda call: call.data == "yes_trip")
  dp.register_callback_query_handler(no_answer,
                                     lambda call: call.data == "no_trip")
  # dp.register_callback_query_handler(latest_movies,
  #                                    lambda call: call.data == "latest_movies")
