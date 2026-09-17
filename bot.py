import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# কনফিগারেশন
BOT_TOKEN = "7973487211:AAHQtqebBZjkCPnUxRNyh0v04wCtf6g1NK8"  # @BotFather থেকে পাওয়া টোকেন
WEBSITE_URL = "https://live-score-hub-plum.vercel.app"  # আপনার ওয়েবসাইটের লাইভ লিঙ্ক
CHANNEL_ID = "https://t.me/rafimhossen3"  # আপনার চ্যানেল বা গ্রুপের ইউজারনেম

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ইউজারদের জন্য মেনু কিবোর্ড
def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🔴 Watch Live Match", url=WEBSITE_URL),
            InlineKeyboardButton(text="👑 VIP Access", url=WEBSITE_URL)
        ],
        [
            InlineKeyboardButton(text="📢 Join Official Channel", url="https://t.me/rafimhossen3")
        ]
    ])
    return keyboard

# /start কমান্ড হ্যান্ডলার
@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    welcome_text = (
        f"👋 **হ্যালো {message.from_user.first_name}!**\n\n"
        "**RAFIM PRIME LIVE** স্ট্রিমিং বটে স্বাগতম।\n"
        "এখানে আপনি ক্রিকেট, ফুটবল এবং ২৪/৭ ফ্রি সিনেমা বাফারিং ছাড়া দেখতে পারবেন।\n\n"
        "👇 সরাসরি খেলা দেখতে নিচের বাটনে ক্লিক করুন:"
    )
    await message.answer(welcome_text, reply_markup=get_main_keyboard(), parse_mode="Markdown")

# এডমিনদের জন্য অটো-পোস্টিং ফাংশন (চ্যানেলে ম্যাচ অ্যালার্ট পাঠানো)
async def broadcast_match_alert(match_title: str, match_time: str):
    alert_text = (
        f"🚨 **LIVE MATCH ALERT!** 🚨\n\n"
        f"⚽ **ম্যাচ:** {match_title}\n"
        f"⏰ **সময়:** {match_time}\n"
        f"📺 **কোয়ালিটি:** 1080p FHD (No Buffer)\n\n"
        "সরাসরি মোবাইল বা পিসিতে কোনো অ্যাড ছাড়াই দেখতে এখনই ভিজিট করুন:"
    )
    
    alert_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="▶️ Click Here To Watch Live", url=WEBSITE_URL)]
    ])
    
    await bot.send_message(chat_id=CHANNEL_ID, text=alert_text, reply_markup=alert_keyboard, parse_mode="Markdown")

async def main():
    print("✅ বট সফলভাবে চালু হয়েছে...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
