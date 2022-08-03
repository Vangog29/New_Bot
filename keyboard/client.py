from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

button = 'Кнопка'
button1 = 'Перевод'
button_translate = '/Translate'
reply_markup = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=button), KeyboardButton(text=button1)
        ],
    ],
    resize_keyboard=True, one_time_keyboard=True
)

reply_markup_trans = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=button_translate)
        ]
    ]
)

inline_kayboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Перевод", callback_data='trans'),InlineKeyboardButton("Кнопка 2", callback_data=2)
        ]
    ]
)

reg_yes_no_kayboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Да", callback_data='yes_reg'), InlineKeyboardButton("Нет", callback_data="no_reg")
        ]
    ]
)