import asyncio
import logging
from random import randint
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
Token = "6886839570:AAHopkG3mv0HJqpeh-w70xde3ISIBZk8G3k"

bot = Bot(token=Token)

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(f"<b>{message.from_user.full_name}</b> Salom",
                         parse_mode="HTML")
    print(f"""
{message.from_user.first_name}
{message.from_user.last_name}
{message.from_user.username}
{message.from_user.id}""")


@dp.message(Command("yordam"))
async def cmd_yordam(message: types.Message):
    await message.reply(
        f"<b>{message.from_user.full_name}</b> sizga qanday yordam kerak?\nBotni qaytarish: <b>/start</b>\nSavollar: <b>/savol</b>\n<u>Rasm: <b>/img</b></u>",
        parse_mode="HTML")


@dp.message(Command("img"))
async def cmd_python(message: types.Message):
    name = [
        "https://avatars.mds.yandex.net/i?id=314286713e101c0db4ae8b33e9a9618f3919594f-5194823-images-thumbs&n=13",
        "https://avatars.mds.yandex.net/i?id=5cf0dbdb7a6f017556b209ef86f61d04bae36d1b-8276139-images-thumbs&n=13",
        "https://t4.ftcdn.net/jpg/04/18/67/63/240_F_418676324_h6utFQWggqwkDi7GgSJWsmS8zZh7kCbI.jpg",
        "https://t4.ftcdn.net/jpg/05/05/41/39/240_F_505413960_r4BUfFKXvzMkSCrXUl0HnMK8Bszuq6y4.jpg",
        "https://t4.ftcdn.net/jpg/01/75/19/91/240_F_175199100_WMgwUL0TqvZIPtAvbzQLxmRsbo0btcJG.jpg",
        "https://t4.ftcdn.net/jpg/03/16/16/79/240_F_316167997_mZRA3nERj6eLVXE41f8DwcIZhOXWbOoE.jpg",
        "https://t3.ftcdn.net/jpg/04/16/81/02/240_F_416810262_aTI8GcxNcsJcCZ1SDPhaHP2QCJZDFzMg.jpg",
        "https://t3.ftcdn.net/jpg/03/99/36/10/240_F_399361008_v9dGH2AP36iw8vsB9nCnUQW64YkPbb7N.jpg"
    ]

    captions = ["Bu rasmda dasturlash tasvirlangan",
                "Rasmda dasturlash tasvirlangan",
                "Dasturlash tasvirlangan rasm",
                "Dasturlashga oid rasm"
                ]

    await message.answer_photo(photo=name[randint(0, len(name))], caption=captions[randint(0, len(captions))])


@dp.message(Command("savol"))
async def cmd_savol(message: types.Message):
    await message.answer("""
🟢savol
<i>1) Python nima?
2) Nima uchun aynan Python dasturlash tili?
3) Python dasturlash tili qachon ishlab chiqarilgan?
4) Python da Web dasturlash.
5) Python da Suniy intilekt AI.
6) Dasturlash tili nomlari</i>""",
                         parse_mode="HTML")

    @dp.message()
    async def cmd_javob(message: types.Message):
        if message.text == "1":
            await message.reply("""
Bu dasturlash tili o'rganish uchun oson, foydalanish uchun qulay, ko'p qirrali dasturlash tili bo'lib, dasturlashga yangi kirganlar uchun ham, soha mutaxassislari uchun ham zo'r tanlov.

Python quyidagilar uchun ishlatiladi:

        veb-ishlab chiqish (server tomonida),
        dasturiy ta'minotni ishlab chiqish,
        matematik amallar,
        tizim skriptlari.""")
        elif message.text == "2":
            await message.reply("""
            Bu dasturlash tili o'rganish uchun oson, foydalanish uchun qulay, ko'p qirrali dasturlash tili bo'lib, dasturlashga yangi kirganlar uchun ham, soha mutaxassislari uchun ham zo'r tanlov.
            Python turli xil platformalarda ishlaydi (Windows, Mac, Linux, Raspberry Pi va boshqalar).
            Python ingliz tiliga o'xshash oddiy sintaksisga ega.
            Python dasturlash tiliga bo'lgan talab yildan yilga oshib kelmoqda. CodingDojo portalining tadqiqotlariga ko'ra, 2020 yilda aynan Python tilida dasturlovchi mutaxassislarga eng ko'p talab bo'lgan.
            Python Artificial Intelligence (Sun'iy intellekt) va Data Science (Ulkan ma'lumotlar bilan ishlash) sohalarining tili hisoblanadi. Bugungi kunda keng ommalashib borayotgan sun'iy intellekt asosida ishlovchi dasturlarning aksari Pythonda yozilgan. Bu sohalardagi mutaxassislar bugungi kunda eng noyob va qimmatbaho kadrlar hisoblanadi.
            Keng qamrovli va universal til. Python dasturlari deyarli barcha operativ tizimlarda va platformalarda ishlaydi.
            O'rganish uchun ham, tushunish uchun ham juda qulay va sodda kod.
            Moslashuvchanlik —Python dasturlash tili ma'lum bir masalalarni yechish bilan chegaralanmagan. Bu til dasturchilarga yangi va yangi yo'nalishlarga ki'rish imkonini beradi. Python quyidagi sohalarda qo'llaniladi: Web va Internet dasturlash, kompyuter o'yinlarini yaratish, ma'lumotlar bazasi bilan ishlash (DB), computer vision, foydalanuvchilar uchun grafik interfeys (GUI), juda tez rivojlanayotgan buyumlar interneti (IoT) texnologiyasi va hokazo.""")
        elif message.text == "3":
            await message.reply("""
            <b>Python</b> - mashhur dasturlash tili. U <u>Guido van Rossum</u> tomonidan <i>1991 yilda ishlab chiqilgan.</i>""",
                                parse_mode="HTML")
        elif message.text == "4":
            await message.reply("""
Python veb-saytlarni ishlab chiqish uchun bir qator frameworklar bor. Mashhur frameworklar Django, Flask, Pylons va boshqalar. Ushbu frameworklar Python-da yozilganligi sababli , kodni tez va barqaror qilishiga asosiy sabab .

Boshqa veb-saytlardan ma'lumotlarni olish mumkin bo'lgan joylarda veb-qirqishlarni ham amalga oshirishingiz mumkin. Shuningdek, Instagram, bit chelak, Pinterest kabi ko'plab veb-saytlar faqat ushbu frameworklar bilan yozilgan.Yana bir pythonni gigant kompanyalar ishlatishi misol uchun google, facebook va boshqalar.""")
        elif message.text == "5":
            await message.reply("""
<b>AI texnologiya</b> dunyoda tez va jadal rivojlanib borayotgan yo'nalishlardan biri.Siz aslida inson miyasiday o'ylaydigan, tahlil qiladigan va qaror qabul qiladigan robotlar yaratishingiz mumkin.Bularni barchasini Keras va TensorFlow kutubxonalari bilan qilsa bo'ladi.Hozirda o'zim ham computer vision sohasida bir-ikkita loyihalar ham qilyapman. Computer vision bu rasmga qarab uni kimligini va uni harakatlarini aniqlaydigan yo'nalishlar bu albatta pythonda sodda ko'p qatorlik kod yozmaydi. Buni amalga oshirish uchun openCv kabi kutubxonalar mavjud.""",
                                parse_mode="HTML")
        elif message.text == "6":
            await message.reply("""
Quyida <b>2023</b> yilda talab qilinadigan eng mashhur va eng yaxshi dasturlash tillari roʻyxati keltirilgan:

<i>. Javascript
. Python
. Go
. Java
. Kotlin
. PHP
. C#
. Swift
. R
. Ruby
. C and C++
. Matlab
. TypeScript
. Scala
. SQL
. HTML
. CSS
. NoSQL
. Rust
. Perl</i>""", parse_mode="HTML")
        else:
            await message.reply("🇺🇿")


@dp.message(Command("ozmalum"))
async def kontakt(message: types.Message):
    ma = [
        [types.KeyboardButton(text="Location", request_location=True)],
        [types.KeyboardButton(text="Contact", request_contact=True)]
    ]
    mal = types.ReplyKeyboardMarkup(keyboard=ma)
    await message.answer(text="<u>Qaysi ma'lumotni jo'natmoqchisiz?</u>", reply_markup=mal, parse_mode="HTML")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
