from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from aiogram import Router
from aiogram import types, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext


from users.models import UserProfile
from .db_methods import get_user_from_db

from .keyboard import start
from .callbacks import Form

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    current_user_id = message.from_user.id
    try: 
        user = await get_user_from_db(current_user_id)
        text = "Заполните данные, чтобы бот смог сгенерировать видео"
        await message.answer(
            text=f"{text}",
            reply_markup=start(message),
        )
    except ObjectDoesNotExist:
        user = UserProfile(telegram_id=current_user_id)
        await sync_to_async(user.save)()
        text = "Заполните данные, чтобы бот смог сгенерировать видео"
        await message.answer(
            text=f"{text}",
            reply_markup=start(message)
        )


@start_router.message(commands=['sendfile'])
async def get_short_handler(message: Message) -> None:
    await message.answer("Команда /get_short была вызвана. Здесь будет логика для генерации видео.")
    file_path = 'path/to/your/file.txt'  # Укажите путь к вашему файлу
    with open(file_path, 'rb') as file:
        await message.answer_document(file)


# form_process = Router()

# @form_process.message(state=Form.waiting_for_fio)
# async def process_fio(message: types.Message, state: FSMContext):
#     current_user_id = message.from_user.id
#     user_fio = message.text
#     print(user_fio)


