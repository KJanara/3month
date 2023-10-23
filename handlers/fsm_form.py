import re
import sqlite3
import random

from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.inline_buttons import (like_dislike_keyboard,
                                      edit_delete_keyboard,
                                      my_profile_register)


class FormStates(StatesGroup):
  nickname = State()
  bio = State()
  age = State()
  occupation = State()
  photo = State()


async def fsm_start(call: types.CallbackQuery):
  await bot.send_message(
    chat_id=call.from_user.id,
    text="Send me ur nickname"
  )
  await FormStates.nickname.set()


async def load_nickname(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['nickname'] = message.text
    print(data)
  await bot.send_message(
    chat_id=message.from_user.id,
    text="Send me ur bio"
  )
  await FormStates.next()


async def load_bio(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['bio'] = message.text
    print(data)
  await bot.send_message(
    chat_id=message.from_user.id,
    text="how old are you?\n"
         "(use only numeric text)"
  )
  await FormStates.next()


async def load_age(message: types.Message, state: FSMContext):
  try:
    if type(int(message.text)) != int:
      pass
    async with state.proxy() as data:
      data['age'] = message.text
      print(data)
    await bot.send_message(
      chat_id=message.from_user.id,
      text="whats you're occupation?"
    )
    await FormStates.next()
  except ValueError as e:
    await message.reply(
      text='faild, because u used not numaric text'
    )
    await state.finish()
    return


async def load_occupation(message: types.Message, state: FSMContext):
  async with state.proxy() as data:
    data['occupation'] = message.text
    print(data)
  await bot.send_message(
    chat_id=message.from_user.id,
    text="send photo"
  )
  await FormStates.next()


async def load_photo(message: types.Message, state: FSMContext):
  path = await message.photo[-1].download(
    destination_dir=DESTINATION + "media"
  )
  async with state.proxy() as data:
    user = Database().sql_select_user_form_query(
      telegram_id=message.from_user.id
    )
    if user:
      Database().sql_update_form_query(
        nickname=data['nickname'],
        bio=data['bio'],
        age=data['age'],
        occupation=data['occupation'],
        photo=path.name,
        telegram_id=message.from_user.id
      )
      with open(path.name, 'rb') as photo:
        await bot.send_photo(
          chat_id=message.chat.id,
          photo=photo,
          caption=f"nickname: {data['nickname']}\n"
                  f"bio: {data['bio']}\n"
                  f"age: {data['age']}\n"
                  f"occupation: {data['occupation']}\n"
        )

      await bot.send_message(
        chat_id=message.from_user.id,
        text="updated successfully  "
      )
    else:
      print("no user")
      Database().sql_insert_user_form_query(
        telegram_id=message.from_user.id,
        nickname=data['nickname'],
        bio=data['bio'],
        age=data['age'],
        occupation=data['occupation'],
        photo=path.name
      )
      with open(path.name, 'rb') as photo:
        await bot.send_photo(
          chat_id=message.chat.id,
          photo=photo,
          caption=f"Nickname: {data['nickname']}\n"
                  f"Bio: {data['bio']}\n"
                  f"Age: {data['age']}\n"
                  f"Occupation: {data['occupation']}\n"
        )
      await bot.send_message(
        chat_id=message.from_user.id,
        text="Registered successfully"
      )
    await state.finish()


async def my_profile_call(call: types.CallbackQuery):
  user_form = Database().sql_select_user_form_query(
    telegram_id=call.from_user.id,
  )
  try:
    with open(user_form[0]["photo"], 'rb') as photo:
      await bot.send_photo(
        chat_id=call.from_user.id,
        photo=photo,
        caption=f"nickname: {user_form[0]['nickname']}\n"
                f"bio: {user_form[0]['bio']}\n"
                f"age: {user_form[0]['age']}\n"
                f"occupation: {user_form[0]['occupation']}\n",
        reply_markup=await edit_delete_keyboard()
      )
  except IndexError:
    await bot.send_message(
      chat_id=call.from_user.id,
      text="you don't have a form, please register",
      reply_markup=await my_profile_register()
    )

async def random_profiles_call(call: types.CallbackQuery):
  users = Database().sql_select_all_users_form_query()
  random_form = random.choice(users)
  with open(random_form['photo'], 'rb') as photo:
    await bot.send_photo(
      chat_id=call.from_user.id,
      photo=photo,
      caption=f"nickname: {random_form['nickname']}\n"
              f"bio: {random_form['bio']}\n"
              f"age: {random_form['age']}\n"
              f"occupation: {random_form['occupation']}\n",
      reply_markup=await like_dislike_keyboard(
        owner_tg_id=random_form['telegram_id']
      )
    )

async def like_detect_call(call: types.CallbackQuery):
  owner_tg_id = re.sub("user_form_like", "", call.data)
  print(owner_tg_id)
  try:
    Database().sql_insert_like_query(
      owner=owner_tg_id,
      liker=call.from_user.id
    )
  except sqlite3.IntegrityError:
    await bot.send_message(
      chat_id=call.from_user.id,
      text="you already liked form"
    )
  finally:
    await random_profiles_call(call=call)


async def delete_form_call(call: types.CallbackQuery):
  Database().sql_delete_form_query(
    owner=call.from_user.id
  )
  await bot.send_message(
    chat_id=call.from_user.id,
    text="your form deleted success"

  )

def register_fsm_form_handlers(dp: Dispatcher):
  dp.register_callback_query_handler(fsm_start,
                                     lambda call: call.data == "fsm_start")
  dp.register_message_handler(load_nickname,
                              state=FormStates.nickname,
                              content_types=['text'])
  dp.register_message_handler(load_bio,
                              state=FormStates.bio,
                              content_types=['text'])
  dp.register_message_handler(load_age,
                              state=FormStates.age,
                              content_types=['text'])
  dp.register_message_handler(load_occupation,
                              state=FormStates.occupation,
                              content_types=['text'])
  dp.register_message_handler(load_photo,
                              state=FormStates.photo,
                              content_types=types.ContentTypes.PHOTO)
  dp.register_callback_query_handler(my_profile_call,
                              lambda call: call.data == "my_profile")
  dp.register_callback_query_handler(random_profiles_call,
                                     lambda call: call.data == "random_profile")
  dp.register_callback_query_handler(like_detect_call,
                                     lambda call: "user_form_like" in call.data)
  dp.register_callback_query_handler(delete_form_call,
                                     lambda call:  call.data == "delete_profile")
