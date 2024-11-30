from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class CD(CallbackData, prefix="CallbackData"): #NCM - navigation callback with message id
    cb_text: str = ""
    cb_message_id: int = 0

def start(message):
    builder = InlineKeyboardBuilder()
    builder.button(text="Ввести ФИО", callback_data=CD(cb_text="FIO",cb_message_id=message.message_id).pack())
    builder.button(text="Ввести дату рождения", callback_data=CD(cb_text="DateBirth",cb_message_id=message.message_id).pack())
    builder.button(text="Ввести дату смерти (если есть)", callback_data=CD(cb_text="DateDeath",cb_message_id=message.message_id).pack())
    builder.button(text="Прикрепить Эпиграф", callback_data=CD(cb_text="Epigraph",cb_message_id=message.message_id).pack())
    builder.button(text="Прикрепить фотографии", callback_data=CD(cb_text="Photos",cb_message_id=message.message_id).pack())
    builder.button(text="Сгенерировать короткое видео", callback_data=CD(cb_text="Short",cb_message_id=message.message_id).pack())
    builder.adjust(1)

    return builder.as_markup()