from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Savol-javoblar lug'ati
QA_DATA = {
    "q1": "SS Accounting faoliyati nimalardan iborat?\nZamonaviy kasblarga oʻqitish.",
    "q2": "SS Accounting oʻquv binosi qayerda joylashgan?\nSergeli tumani TIST binosida.",
    "q3": "Hozirgi vaqtda qanday yoʻnalishlar boʻyicha taʼlim beriladi?\nBuxgalteriya.",
    "q4": "Oʻquv kurslarga qabul qachon ochiladi?\nHar oyning 10 kunida."
}

# Asosiy menyu funksiyasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Biz haqimizda", callback_data="biz_haqimizda")],
        [InlineKeyboardButton("Kurslar", callback_data="kurslar")],
        [InlineKeyboardButton("Savol-javob", callback_data="savol_javob")],
        [InlineKeyboardButton("Admin bilan bog'lanish", callback_data="boglanish")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:  # Agar message mavjud bo'lsa
        await update.message.reply_text("Asosiy menyu:", reply_markup=reply_markup)
    elif update.callback_query:  # Agar callback_query mavjud bo'lsa
        await update.callback_query.message.reply_text("Asosiy menyu:", reply_markup=reply_markup)

# "Biz haqimizda" bo'limi uchun funksiya
async def biz_haqimizda(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = (
        "Biz bilan 4 oy mobaynida kasb egasi bo'ling🧑‍💻\n\n"
        "Bunda siz hozirgi paytda buxgalteriya kasibini o'rganish bilan birga real korxonada amalyot o'tashingiz mumkin. 💥\n\n"
        "Bunda sizga:\n"
        "1) 1C dasturida ishlash✅\n"
        "2) DIDOX ✅\n"
        "3) My.soliq✅\n"
        "4) my.mehnat✅\n"
        "5) Internet bank✅\n"
        "platformalarida ishlashni o'rganasiz. Bunda sizga malakali ustozlardan buxgalteriya kasbining sir-asrorlari bilan tanishasiz.😉"
    )
    keyboard = [
        [InlineKeyboardButton("Asosiy menyu", callback_data="main_menu")],
        [InlineKeyboardButton("Orqaga", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, reply_markup=reply_markup)

# "Kurslar" bo'limi uchun funksiya
async def kurslar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "Bizda quyidagi kurslar mavjud:\n- Python\n- Blender\n- Buxgalteriya"
    keyboard = [
        [InlineKeyboardButton("Asosiy menyu", callback_data="main_menu")],
        [InlineKeyboardButton("Orqaga", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, reply_markup=reply_markup)

# "Admin bilan bog'lanish" bo'limi uchun funksiya
async def boglanish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = "Admin bilan bog'lanish uchun: @broo_ooooo\nTelefon nomeri: +998907990331\nIsmi: Sirojjidin"
    keyboard = [
        [InlineKeyboardButton("Asosiy menyu", callback_data="main_menu")],
        [InlineKeyboardButton("Orqaga", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text(text, reply_markup=reply_markup)

# Savol-javob bo'limi uchun menyu
async def savol_javob(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("1. Faoliyat", callback_data="q1")],
        [InlineKeyboardButton("2. O‘quv binosi?", callback_data="q2")],
        [InlineKeyboardButton("3. Ta'lim yo‘nalishlari", callback_data="q3")],
        [InlineKeyboardButton("4. Qabul vaqti", callback_data="q4")],
        [InlineKeyboardButton("Asosiy menyu", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text("Savol-javoblar:", reply_markup=reply_markup)

# Callback funksiyasi
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    if query.data == "main_menu":
        await start(update, context)
    elif query.data == "savol_javob":
        await savol_javob(update, context)
    elif query.data == "biz_haqimizda":
        await biz_haqimizda(update, context)
    elif query.data == "kurslar":
        await kurslar(update, context)
    elif query.data == "boglanish":
        await boglanish(update, context)
    elif query.data in QA_DATA:
        response = QA_DATA[query.data]
        keyboard = [
            [InlineKeyboardButton("Asosiy menyu", callback_data="main_menu")],
            [InlineKeyboardButton("Orqaga", callback_data="savol_javob")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(text=response, reply_markup=reply_markup)

# Asosiy dastur
def main():
    app = ApplicationBuilder().token("7916058508:AAFCoxUGzGFn4ERHKMtwBpjvuzxNW6dAuI8").build()  # Tokenni yangilashingiz kerak

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()

if __name__ == "__main__":
    main()
