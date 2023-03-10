from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


remove = ReplyKeyboardRemove()


async def menu_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("🖼 Rasimga Joziba berish")
    btn.row("📊 Statistika", "👩‍💻 Biz bilan aloqa")
    return btn


async def effects_btn(data):
    btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        *[KeyboardButton(item['effect_name']) for item in data],
        KeyboardButton("🔙 Ortga")
    )

    return btn


async def cancel_support_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True)
    btn.row("❌ Bekor qilish")
    return btn


async def davom_etish():
    start_menu_btn = ReplyKeyboardMarkup(resize_keyboard=True)
    start_menu_btn.row('❌ Bekor qilish', 'Davom etish')
    return start_menu_btn

