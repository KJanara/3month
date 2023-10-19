from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_keyboard():
  markup = InlineKeyboardMarkup()
  quastionaire_button = InlineKeyboardButton(
    "Start Questionaire",
    callback_data="start_quesionnaire"
  )
  registration_button = InlineKeyboardButton(
    "registration",
    callback_data="fsm_start"
  )
  my_profile_button = InlineKeyboardButton(
    "my profile",
    callback_data="my_profile"
  )
  markup.add(quastionaire_button)
  markup.add(registration_button)
  markup.add(my_profile_button)
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

async def admin_keybords():
  markup = InlineKeyboardMarkup()
  admin_user_list_button = InlineKeyboardButton(
    "user list",
    callback_data="admin_user_list"
  )
  markup.add(admin_user_list_button)
  return markup

