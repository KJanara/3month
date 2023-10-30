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
  view_profiles_button = InlineKeyboardButton(
    "view profile",
    callback_data="random_profile"
  )
  reference_menu_button = InlineKeyboardButton(
    "Referral Menu ",
    callback_data="reference_menu"
  )
  latest_movies_button = InlineKeyboardButton(
    "latest movies ",
    callback_data="latest_movies"
  )
  markup.add(quastionaire_button)
  markup.add(registration_button)
  markup.add(my_profile_button)
  markup.add(view_profiles_button)
  markup.add(reference_menu_button)
  markup.add(latest_movies_button)
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

async def like_dislike_keyboard(owner_tg_id):
  markup = InlineKeyboardMarkup()
  user_form_like_button = InlineKeyboardButton(
    "like",
    callback_data=f"user_form_like{owner_tg_id}"
  )
  user_form_dislike_button = InlineKeyboardButton(
    "dislike",
    callback_data="random_profile"
  )
  markup.add(user_form_like_button)
  markup.add(user_form_dislike_button)
  return markup

async def edit_delete_keyboard():
  markup = InlineKeyboardMarkup()
  edit_form_button = InlineKeyboardButton(
    "update",
    callback_data="fsm_start"
  )
  delete_form_button = InlineKeyboardButton(
    "delete",
    callback_data="delete_profile"
  )
  markup.add(edit_form_button)
  markup.add(delete_form_button)
  return markup

async def my_profile_register():
  markup = InlineKeyboardMarkup()
  registation_button = InlineKeyboardButton(
    "registration",
    callback_data="fsm_start"
  )
  markup.add(registation_button)
  return markup


async def reference_menu_keyboard():
  markup = InlineKeyboardMarkup()
  reference_link_button = InlineKeyboardButton(
    "Referral Link ",
    callback_data="reference_link"
  )
  reference_list_button = InlineKeyboardButton(
    "Referral List ",
    callback_data="reference_list"
  )
  markup.add(reference_link_button)
  markup.add(reference_list_button)
  return markup
