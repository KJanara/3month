from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
  markup = InlineKeyboardMarkup()
  quastionaire_button = InlineKeyboardButton(
    "Start Questionaire",
    callback_data="start_quesionnaire"
  )
  markup.add(quastionaire_button)
  return markup

async def quesionnaire_one_keybords():
  markup = InlineKeyboardMarkup()
  yes_button = InlineKeyboardButton(
    "yes",
    callback_data="yes_trip"
  )
  no_button = InlineKeyboardButton(
    "no",
    callback_data="no_trip"
  )
  markup.add(yes_button)
  markup.add(no_button)
  return markup
