import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("7998522860:AAFZ5Q4PF5ykkB2Vpcth2_6oSSPVuvdoCeQ")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔎 ID Checker Bot\n\n"
        "Xabar yozing yoki forward qiling, men quyidagilarni ko‘rsataman:\n"
        "🆔 User ID\n👤 Username\n📛 Ism\n👥 Guruh ID\n📢 Kanal ID\n🔁 Forward qilingan user ID\n🔍 Username orqali ID"
    )

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    user = update.effective_user
    chat = update.effective_chat

    text = f"👤 USER INFO\n\n🆔 User ID: {user.id}\n👤 Username: @{user.username}\n📛 Ism: {user.first_name}\n"

    # Guruh yoki kanal ID
    text += f"\n👥 Chat ID: {chat.id}\n📢 Type: {chat.type}"

    # Forward qilingan user
    if msg.forward_from:
        f = msg.forward_from
        text += f"\n\n🔁 Forward qilingan user:\n🆔 ID: {f.id}\n👤 Username: @{f.username}\n📛 Ism: {f.first_name}"

    # Agar foydalanuvchi username yuborsa (bot bilan chat qilgan bo‘lsa)
    if msg.text and msg.text.startswith("@") and msg.text != f"@{user.username}":
        try:
            u = await context.bot.get_chat(msg.text)
            text += f"\n\n🔍 Username orqali ID:\n🆔 {u.id}\n👤 Username: @{u.username}\n📛 Name: {u.first_name}"
        except:
            text += f"\n\n🔍 Username orqali ID:\n❌ Topilmadi yoki bot bilan chat qilmagan"

    await msg.reply_text(text)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, check))
app.run_polling()