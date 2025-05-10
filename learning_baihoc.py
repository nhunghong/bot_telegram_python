from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram.ext import MessageHandler, filters
from lessons.stage1 import stage1_lessons
from lessons.stage2 import stage2_lessons
from lessons.stage3 import stage3_lessons
from lessons.stage4 import stage4_lessons
from lessons.exercises import exercises
import nest_asyncio
nest_asyncio.apply()
import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

#BOT_TOKEN = "7442682123:AAEC5a-kK2dls3UKlC8Ya3ASO6b-pb820tc"

stages = {
    "gd1": "Giai đoạn 1: Làm quen Python",
    "gd2": "Giai đoạn 2: Thực hành thực tế",
    "gd3": "Giai đoạn 3: Automation Test",
    "gd4": "Giai đoạn 4: Nâng cao"
}

lessons = {
    **stage1_lessons,
    **stage2_lessons,
    **stage3_lessons,
    **stage4_lessons 
}

# Gán bài tập từ exercises vào lessons nếu có
for code in exercises:
    if code in lessons:
        lessons[code]["exercise"] = exercises[code]

async def hoc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🐍 Giai đoạn 1: Làm quen Python", callback_data="gd1")],
        [InlineKeyboardButton("⚙️ Giai đoạn 2: Thực hành thực tế", callback_data="gd2")],
        [InlineKeyboardButton("🤖 Giai đoạn 3: Automation Test", callback_data="gd3")],
        [InlineKeyboardButton("🚀 Giai đoạn 4: Nâng cao", callback_data="gd4")],
    ]
    
    text = "*Chọn giai đoạn học:*"
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(text, reply_markup=reply_markup, parse_mode="Markdown")
    elif update.callback_query:
        await update.callback_query.edit_message_text(text, reply_markup=reply_markup, parse_mode="Markdown")


async def show_stage_lessons(query, stage):
    lessons_keyboard = []
    stage_key = f"g{stage[2]}"  # gd1 -> g1, gd2 -> g2 ...
    for i in range(1, 10):
        code = f"{stage_key}_b{i}"
        if code in lessons:
            title = lessons[code]["title"]
            btn = InlineKeyboardButton(title, callback_data=code)
            if len(lessons_keyboard) == 0 or len(lessons_keyboard[-1]) == 2:
                lessons_keyboard.append([btn])
            else:
                lessons_keyboard[-1].append(btn)
    lessons_keyboard.append([InlineKeyboardButton("💖 Quay lại menu giai đoạn", callback_data="menu")])
    await query.edit_message_text(
        f"*{stages[stage]}*",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(lessons_keyboard)
    )


async def show_lesson_detail(query, code):
    lesson = lessons.get(code)
    if not lesson:
        return
    stage_number = code.split("_")[0][1]  # "g1" -> "1"
    stage = f"gd{stage_number}"           # "gd1"

    current_number = int(code.split("_b")[1])
    prev_code = f"g{stage_number}_b{current_number - 1}" if f"g{stage_number}_b{current_number - 1}" in lessons else None
    next_code = f"g{stage_number}_b{current_number + 1}" if f"g{stage_number}_b{current_number + 1}" in lessons else None

    buttons = []
    if prev_code:
        buttons.append(InlineKeyboardButton("⬅️ Bài trước", callback_data=prev_code))
    if next_code:
        buttons.append(InlineKeyboardButton("➡️ Bài tiếp", callback_data=next_code))
    buttons.append(InlineKeyboardButton("🔙 Quay lại", callback_data=stage))

    # 👉 Thêm phần bài tập nếu có
    exercise = f"\n\n{lesson['exercise']}" if 'exercise' in lesson else ""

    await query.edit_message_text(
        f"*{lesson['title']}*\n\n{lesson['content']}{exercise}",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([buttons])
    )



async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "menu":
        # Gọi lại menu nhưng dùng edit_message_text vì đang ở callback
        await hoc_callback(query)
    elif data in stages:
        return await show_stage_lessons(query, data)
    elif data in lessons:
        return await show_lesson_detail(query, data)

async def hoc_callback(query):
    keyboard = [
        [InlineKeyboardButton("🐍 Giai đoạn 1: Làm quen Python", callback_data="gd1")],
        [InlineKeyboardButton("⚙️ Giai đoạn 2: Thực hành thực tế", callback_data="gd2")],
        [InlineKeyboardButton("🤖 Giai đoạn 3: Automation Test", callback_data="gd3")],
        [InlineKeyboardButton("🚀 Giai đoạn 4: Nâng cao", callback_data="gd4")],
    ]
    await query.edit_message_text(
        "*Chọn giai đoạn học:*",
        reply_markup=InlineKeyboardMarkup(keyboard),
        parse_mode="Markdown"
    )

async def block_spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    if "t.me" in text or "@JetonVPNNbot" in text or "VPN" in text:
        await update.message.delete()
        return

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    await app.bot.set_my_commands([BotCommand("hoc", "Xem danh sách bài học")])

    app.add_handler(CommandHandler("hoc", hoc))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), block_spam))  # ✅ dòng cần thêm

    print("✅ Bot bài học Python đã khởi động.")
    await app.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
