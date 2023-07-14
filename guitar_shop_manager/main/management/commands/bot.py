import telebot
from telebot import types
from datetime import date
import requests
import base64

config = {
    'name': 'GuitarShopManager',
    'token': '6011605172:AAExztACmzo32S4_aQAEIF_UBDLp-MTeBCg'
}

bot = telebot.TeleBot(config["token"])

reg_buttons = telebot.types.InlineKeyboardMarkup()
reg_buttons.add(telebot.types.InlineKeyboardButton(text="Авторизуватись", callback_data="Login"))

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Керувати електрогітарами")
button2 = types.KeyboardButton("Керувати бас-гітарами")
button3 = types.KeyboardButton("Додати новину")
button4 = types.KeyboardButton("Додати відео")
keyboard.add(button1, button2)
keyboard.add(button3, button4)

guitar_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Додати нову електрогітару")
btn2 = types.KeyboardButton("Назад")
btn3 = types.KeyboardButton("Видалити гітару з бази")
guitar_keyboard.add(btn1)
guitar_keyboard.add(btn3)
guitar_keyboard.add(btn2)

bass_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("Додати нову бас-гітару")
btn2 = types.KeyboardButton("Назад")
btn3 = types.KeyboardButton("Видалити бас-гітару з бази")
bass_keyboard.add(btn1)
bass_keyboard.add(btn3)
bass_keyboard.add(btn2)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Вітаємо у боті-менеджері інтернет-магазину GuitarShop. Щоб почати роботу "
                                      "з ботом вам потрібно авторизуватись як адмін",
                     reply_markup=reg_buttons)


@bot.callback_query_handler(func=lambda call: call.data in 'Login')
def reg_login(call):
    if call.data == "Login":
        username = bot.send_message(call.from_user.id, 'Введіть логін')
        bot.register_next_step_handler(username, login)
    else:
        bot.send_message(call.from_user.id, 'Збій у роботі бота. Зверніться у підтримку')


def login(message):
    try:
        url = "http://127.0.0.1:8000/main/admins/"
        json_list = requests.get(url).json()
        counter = 0
        username = message.text
        for i in json_list:
            if i['username'] == username:
                counter += 1
        if counter == 1:
            password = bot.send_message(message.chat.id, "Логін адміна є у базі. Тепер введіть пароль:")

            def password_check(message):
                back_to_login = telebot.types.InlineKeyboardMarkup()
                back_to_login.add(telebot.types.InlineKeyboardButton(text="Повторний логін", callback_data="Login"))
                for i in json_list:
                    if i['username'] == username and i['password'] == message.text:
                        func = bot.send_message(message.chat.id, "Логін успішний. Функціонал доступний "
                                                                 "(відкрийте клавіатуру з командами)",
                                                reply_markup=keyboard)

                        bot.register_next_step_handler(func, functions)
                        break
                    elif i['username'] == username and i['password'] != message.text:
                        bot.send_message(message.chat.id, "Пароль невірний. Спробуйте залогінитись ще раз",
                                         reply_markup=back_to_login)

            bot.register_next_step_handler(password, password_check)
        else:
            bot.send_message(message.chat.id, "Адміна не знайдено. Спробуйте ще раз", reply_markup=reg_buttons)
    except:
        bot.send_message(message.chat.id, "Збій у роботі бота. Зверніться у підтримку")


@bot.message_handler(content_types=['text'])
def functions(message):
    if message.text == "Керувати електрогітарами":
        electro_moderate = bot.send_message(message.chat.id, "Оберіть функцію", reply_markup=guitar_keyboard)

        def guitar_func(message):
            keyboard_prod_name = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("CORT")
            button2 = types.KeyboardButton("ESP")
            button3 = types.KeyboardButton("FUJIGEN")
            button4 = types.KeyboardButton("PARKSONS")
            button5 = types.KeyboardButton("WARWICK")
            button6 = types.KeyboardButton("YAMAHA")
            keyboard_prod_name.add(button1, button2)
            keyboard_prod_name.add(button3, button4)
            keyboard_prod_name.add(button5, button6)
            if message.text == "Додати нову електрогітару":
                prod_name = bot.send_message(message.chat.id, "Введіть назву виробника",
                                             reply_markup=keyboard_prod_name)
                bot.register_next_step_handler(prod_name, guitar1)
            elif message.text == "Назад":
                bot.send_message(message.chat.id, "Оберіть функціонал (відкрийте клавіатуру з командами)",
                                 reply_markup=keyboard)
            elif message.text == "Видалити гітару з бази":
                prod_name = bot.send_message(message.chat.id, "Введіть назву виробника",
                                             reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(prod_name, delete_guitar1)
            else:
                bot.send_message(message.chat.id, "Помилкова команда. Використайте клавіатуру команд",
                                 reply_markup=guitar_keyboard)

        def guitar1(message1):
            model_name = bot.send_message(message.chat.id, "Введіть назву моделі",
                                             reply_markup=types.ReplyKeyboardRemove())

            def guitar2(message2):
                price = bot.send_message(message.chat.id, "Введіть ціну гітари")

                def guitar3(message3):
                    discount = bot.send_message(message.chat.id, "Поточна знижка на товар. Якщо немає - введіть '0'")

                    def guitar4(message4):
                        present = bot.send_message(message.chat.id, "Наявна кількість (цифрою)")

                        def guitar5(message5):
                            color = bot.send_message(message.chat.id, "Вкажіть основний колір")

                            def guitar6(message6):
                                keyboard_body = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                button1 = types.KeyboardButton("Explorer")
                                button2 = types.KeyboardButton("Singlecut (LP)")
                                button3 = types.KeyboardButton("Stratocaster")
                                button4 = types.KeyboardButton("Super Strat")
                                button5 = types.KeyboardButton("Tele")
                                button6 = types.KeyboardButton("Vintage")
                                keyboard_body.add(button1, button2)
                                keyboard_body.add(button3, button4)
                                keyboard_body.add(button5, button6)
                                body = bot.send_message(message.chat.id, "Тип корпуса", reply_markup=keyboard_body)

                                def guitar7(message7):
                                    keyboard_body_material = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    button1 = types.KeyboardButton("Агатіс")
                                    button2 = types.KeyboardButton("Афзелія")
                                    button3 = types.KeyboardButton("Бубінга")
                                    button4 = types.KeyboardButton("Клен")
                                    button5 = types.KeyboardButton("Червоне дерево")
                                    button6 = types.KeyboardButton("Липа")
                                    button7 = types.KeyboardButton("Меранті")
                                    button8 = types.KeyboardButton("Не заявлений")
                                    button9 = types.KeyboardButton("Овангкол")
                                    button10 = types.KeyboardButton("Вільха")
                                    button11 = types.KeyboardButton("Тополя")
                                    keyboard_body_material.add(button1, button2, button3)
                                    keyboard_body_material.add(button4, button5, button6)
                                    keyboard_body_material.add(button7, button8, button9)
                                    keyboard_body_material.add(button10, button11)
                                    body_material = bot.send_message(message.chat.id, "Матеріал корпуса",
                                                                     reply_markup=keyboard_body_material)

                                    def guitar8(message8):
                                        keyboard_scale = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                        button1 = types.KeyboardButton("24,75\"")
                                        button2 = types.KeyboardButton("25.5\"")
                                        # button3 = types.KeyboardButton("32\"")
                                        # button4 = types.KeyboardButton("34\"")
                                        keyboard_scale.add(button1, button2)
                                        # keyboard_scale.add(button3, button4)
                                        scale = bot.send_message(message.chat.id, "Мензура", reply_markup=keyboard_scale)

                                        def guitar9(message9):
                                            keyboard_strings = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                            button1 = types.KeyboardButton("6")
                                            button2 = types.KeyboardButton("7")
                                            keyboard_strings.add(button1, button2)
                                            strings = bot.send_message(message.chat.id, "Вкажіть кількість струн",
                                                                       reply_markup=keyboard_strings)

                                            def guitar10(message10):
                                                default_strings = bot.send_message(message.chat.id,
                                                                                   "Калібр заводських струн",
                                                                                   reply_markup=types.ReplyKeyboardRemove())

                                                def guitar11(message11):
                                                    keyboard_frets = types.ReplyKeyboardMarkup(
                                                        resize_keyboard=True)
                                                    button1 = types.KeyboardButton("20")
                                                    button2 = types.KeyboardButton("21")
                                                    button3 = types.KeyboardButton("22")
                                                    button4 = types.KeyboardButton("24")
                                                    button5 = types.KeyboardButton("26")
                                                    keyboard_frets.add(button1, button2, button3)
                                                    keyboard_frets.add(button4, button5)
                                                    frets = bot.send_message(message.chat.id,
                                                                             "К-ть ладів (числом)", reply_markup=keyboard_frets)

                                                    def guitar12(message12):
                                                        keyboard_fretboard_material = types.ReplyKeyboardMarkup(
                                                            resize_keyboard=True)
                                                        button1 = types.KeyboardButton("Венге")
                                                        button2 = types.KeyboardButton("Клен")
                                                        button3 = types.KeyboardButton("Червоне дерево")
                                                        button4 = types.KeyboardButton("Овангкол")
                                                        keyboard_fretboard_material.add(button1, button2)
                                                        keyboard_fretboard_material.add(button3, button4)
                                                        fretboard_material = bot.send_message(message.chat.id,
                                                                                              "Матеріал грифа",
                                                                                              reply_markup=keyboard_fretboard_material)

                                                        def guitar13(message13):
                                                            keyboard_fretboard_pad_material = types.ReplyKeyboardMarkup(
                                                                resize_keyboard=True)
                                                            button1 = types.KeyboardButton("Венге")
                                                            button2 = types.KeyboardButton("Мербау")
                                                            button3 = types.KeyboardButton("Палісандр")
                                                            button4 = types.KeyboardButton("Овангкол")
                                                            button5 = types.KeyboardButton("Чорне дерево")
                                                            button6 = types.KeyboardButton("Ятоба")
                                                            keyboard_fretboard_pad_material.add(button1, button2, button3)
                                                            keyboard_fretboard_pad_material.add(button4, button5, button6)
                                                            fretboard_pad_material = bot.send_message(message.chat.id,
                                                                                                      "Матеріал накладки грифа",
                                                                                                      reply_markup=keyboard_fretboard_pad_material)

                                                            def guitar14(message14):
                                                                keyboard_neck_attachment = types.ReplyKeyboardMarkup(
                                                                    resize_keyboard=True)
                                                                button1 = types.KeyboardButton("Вклеєний гриф")
                                                                button2 = types.KeyboardButton("Гриф на болтах")
                                                                button3 = types.KeyboardButton("Наскрізний гриф")
                                                                keyboard_neck_attachment.add(button1, button2, button3)
                                                                neck_attachment = bot.send_message(message.chat.id,
                                                                                                   "Тип кріплення грифа",
                                                                                                   reply_markup=keyboard_neck_attachment)

                                                                def guitar15(message15):
                                                                    keyboard_bridge = types.ReplyKeyboardMarkup(
                                                                        resize_keyboard=True)
                                                                    button1 = types.KeyboardButton("TOM + StopBar")
                                                                    button2 = types.KeyboardButton("Тремоло Bigsby")
                                                                    button3 = types.KeyboardButton("Тремоло Floyd Rose")
                                                                    button4 = types.KeyboardButton("Тремоло Vintage")
                                                                    button5 = types.KeyboardButton("Фіксований")
                                                                    keyboard_bridge.add(button1, button2, button3)
                                                                    keyboard_bridge.add(button4, button5)
                                                                    bridge = bot.send_message(message.chat.id,
                                                                                              "Вкажіть тип бріджа",
                                                                                              reply_markup=keyboard_bridge)

                                                                    def guitar16(message16):
                                                                        pickups = bot.send_message(message.chat.id,
                                                                                                   "Звукознімачі",
                                                                                                   reply_markup=types.ReplyKeyboardRemove())

                                                                        def guitar17(message17):
                                                                            pegs = bot.send_message(message.chat.id,
                                                                                                    "Кілки")

                                                                            def guitar18(message18):
                                                                                country = bot.send_message(
                                                                                    message.chat.id,
                                                                                    "Вкажіть країну-виробника")

                                                                                def guitar19(message19):
                                                                                    description = bot.send_message(
                                                                                        message.chat.id,
                                                                                        "Введіть опис")

                                                                                    def guitar20(message20):
                                                                                        images = bot.send_message(
                                                                                            message.chat.id,
                                                                                            "Вставте зображення (обов'язково зі стисненням і групуванням)")

                                                                                        today = date.today()
                                                                                        data = {
                                                                                            'type': "Guitar",
                                                                                            'prod_name': message1.text,
                                                                                            'model': message2.text,
                                                                                            'date_add': today,
                                                                                            'prod_price': message3.text,
                                                                                            'discount': message4.text,
                                                                                            'present': message5.text,
                                                                                            'color': message6.text,
                                                                                            'body': message7.text,
                                                                                            'body_material': message8.text,
                                                                                            'scale': message9.text,
                                                                                            'strings': message10.text,
                                                                                            'default_strings': message11.text,
                                                                                            'frets': message12.text,
                                                                                            'fretboard_material': message13.text,
                                                                                            'fretboard_pad_material': message14.text,
                                                                                            'neck_attachment': message15.text,
                                                                                            'bridge': message16.text,
                                                                                            'pickups': message17.text,
                                                                                            'pegs': message18.text,
                                                                                            'country': message19.text,
                                                                                            'description': message20.text, }

                                                                                        requests.post(
                                                                                            url=f"http://127.0.0.1:8000/main/guitars/",
                                                                                            data=data)

                                                                                        @bot.message_handler(
                                                                                            content_types=['photo'])
                                                                                        def guitar_images(message):
                                                                                            file_info = bot.get_file(
                                                                                                message.photo[
                                                                                                    len(message.photo) - 1].file_id)
                                                                                            downloaded_file = bot.download_file(
                                                                                                file_info.file_path)
                                                                                            src = '/Diploma/img/' + \
                                                                                                  message.photo[
                                                                                                      1].file_id + ".png"
                                                                                            with open(src,
                                                                                                      'wb') as new_file:
                                                                                                new_file.write(
                                                                                                    downloaded_file)
                                                                                            with open(src,
                                                                                                      'rb') as photo:
                                                                                                photo_read = photo.read()
                                                                                                photo_64_encoded = base64.b64encode(
                                                                                                    photo_read)

                                                                                            url = "http://127.0.0.1:8000/main/guitars/"
                                                                                            json_list = requests.get(
                                                                                                url).json()

                                                                                            object_id = 0
                                                                                            for i in json_list:
                                                                                                if i["model"] == f"{message2.text}":
                                                                                                    object_id = i["id"]
                                                                                                    break

                                                                                            data = {
                                                                                                'item_name': object_id,
                                                                                                'image': photo_64_encoded}
                                                                                            requests.post(
                                                                                                url=f"http://127.0.0.1:8000/main/guitar-img/",
                                                                                                data=data)

                                                                                        bot.register_next_step_handler(
                                                                                            images, guitar_images)

                                                                                    bot.register_next_step_handler(
                                                                                        description, guitar20)

                                                                                bot.register_next_step_handler(country,
                                                                                                               guitar19)

                                                                            bot.register_next_step_handler(pegs,
                                                                                                           guitar18)

                                                                        bot.register_next_step_handler(pickups,
                                                                                                       guitar17)

                                                                    bot.register_next_step_handler(bridge, guitar16)

                                                                bot.register_next_step_handler(neck_attachment,
                                                                                               guitar15)

                                                            bot.register_next_step_handler(fretboard_pad_material,
                                                                                           guitar14)

                                                        bot.register_next_step_handler(fretboard_material, guitar13)

                                                    bot.register_next_step_handler(frets, guitar12)

                                                bot.register_next_step_handler(default_strings, guitar11)

                                            bot.register_next_step_handler(strings, guitar10)

                                        bot.register_next_step_handler(scale, guitar9)

                                    bot.register_next_step_handler(body_material, guitar8)

                                bot.register_next_step_handler(body, guitar7)

                            bot.register_next_step_handler(color, guitar6)

                        bot.register_next_step_handler(present, guitar5)

                    bot.register_next_step_handler(discount, guitar4)

                bot.register_next_step_handler(price, guitar3)

            bot.register_next_step_handler(model_name, guitar2)

        def delete_guitar1(message1):
            model_name = bot.send_message(message.chat.id, "Введіть назву моделі",
                                          reply_markup=types.ReplyKeyboardRemove())

            def delete_guitar2(message2):
                url = "http://127.0.0.1:8000/main/guitars/"
                json_list = requests.get(
                    url).json()

                object_id = 0
                for i in json_list:
                    if i["model"] == f"{message2.text}" and i["prod_name"] == f"{message1.text}":
                        object_id += i["id"]
                        break
                requests.delete(url=f"http://127.0.0.1:8000/main/guitars/{object_id}/")

                bot.send_message(message.chat.id, "Видалено",
                                 reply_markup=keyboard)

            bot.register_next_step_handler(model_name, delete_guitar2)

        bot.register_next_step_handler(electro_moderate, guitar_func)
    elif message.text == "Керувати бас-гітарами":
        bass_moderate = bot.send_message(message.chat.id, "Оберіть функцію", reply_markup=bass_keyboard)

        def bass_func(message):
            keyboard_prod_name = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("CORT")
            button2 = types.KeyboardButton("ESP")
            button3 = types.KeyboardButton("FUJIGEN")
            button4 = types.KeyboardButton("PARKSONS")
            button5 = types.KeyboardButton("WARWICK")
            button6 = types.KeyboardButton("YAMAHA")
            keyboard_prod_name.add(button1, button2)
            keyboard_prod_name.add(button3, button4)
            keyboard_prod_name.add(button5, button6)
            if message.text == "Додати нову бас-гітару":
                prod_name = bot.send_message(message.chat.id, "Введіть назву виробника",
                                             reply_markup=keyboard_prod_name)
                bot.register_next_step_handler(prod_name, bass1)
            elif message.text == "Назад":
                bot.send_message(message.chat.id, "Оберіть функціонал (відкрийте клавіатуру з командами)",
                                 reply_markup=keyboard)
            elif message.text == "Видалити бас-гітару з бази":
                prod_name = bot.send_message(message.chat.id, "Введіть назву виробника",
                                             reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(prod_name, delete_guitar1)
            else:
                bot.send_message(message.chat.id, "Помилкова команда. Використайте клавіатуру команд",
                                 reply_markup=guitar_keyboard)

        def bass1(message1):
            model_name = bot.send_message(message.chat.id, "Введіть назву моделі",
                                             reply_markup=types.ReplyKeyboardRemove())

            def bass2(message2):
                price = bot.send_message(message.chat.id, "Введіть ціну бас-гітари")

                def bass3(message3):
                    discount = bot.send_message(message.chat.id, "Поточна знижка на товар. Якщо немає - введіть '0'")

                    def bass4(message4):
                        present = bot.send_message(message.chat.id, "Наявна кількість (цифрою)")

                        def bass5(message5):
                            color = bot.send_message(message.chat.id, "Вкажіть основний колір")

                            def bass7(message7):
                                keyboard_body_material = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                button1 = types.KeyboardButton("Агатіс")
                                button2 = types.KeyboardButton("Афзелія")
                                button3 = types.KeyboardButton("Бубінга")
                                button4 = types.KeyboardButton("Клен")
                                button5 = types.KeyboardButton("Червоне дерево")
                                button6 = types.KeyboardButton("Липа")
                                button7 = types.KeyboardButton("Меранті")
                                button8 = types.KeyboardButton("Не заявлений")
                                button9 = types.KeyboardButton("Овангкол")
                                button10 = types.KeyboardButton("Вільха")
                                button11 = types.KeyboardButton("Тополя")
                                keyboard_body_material.add(button1, button2, button3)
                                keyboard_body_material.add(button4, button5, button6)
                                keyboard_body_material.add(button7, button8, button9)
                                keyboard_body_material.add(button10, button11)
                                body_material = bot.send_message(message.chat.id, "Матеріал корпуса",
                                                                 reply_markup=keyboard_body_material)

                                def bass8(message8):
                                    keyboard_scale = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                    # button1 = types.KeyboardButton("24,75\"")
                                    # button2 = types.KeyboardButton("25.5\"")
                                    button3 = types.KeyboardButton("32\"")
                                    button4 = types.KeyboardButton("34\"")
                                    # keyboard_scale.add(button1, button2)
                                    keyboard_scale.add(button3, button4)
                                    scale = bot.send_message(message.chat.id, "Мензура", reply_markup=keyboard_scale)

                                    def bass9(message9):
                                        keyboard_strings = types.ReplyKeyboardMarkup(resize_keyboard=True)
                                        button1 = types.KeyboardButton("6")
                                        button2 = types.KeyboardButton("7")
                                        keyboard_strings.add(button1, button2)
                                        strings = bot.send_message(message.chat.id, "Вкажіть кількість струн",
                                                                   reply_markup=keyboard_strings)

                                        def bass10(message10):
                                            default_strings = bot.send_message(message.chat.id,
                                                                               "Калібр заводських струн",
                                                                               reply_markup=types.ReplyKeyboardRemove())

                                            def bass11(message11):
                                                keyboard_frets = types.ReplyKeyboardMarkup(
                                                    resize_keyboard=True)
                                                button1 = types.KeyboardButton("20")
                                                button2 = types.KeyboardButton("21")
                                                button3 = types.KeyboardButton("22")
                                                button4 = types.KeyboardButton("24")
                                                button5 = types.KeyboardButton("26")
                                                keyboard_frets.add(button1, button2, button3)
                                                keyboard_frets.add(button4, button5)
                                                frets = bot.send_message(message.chat.id,
                                                                         "К-ть ладів (числом)", reply_markup=keyboard_frets)

                                                def bass12(message12):
                                                    keyboard_fretboard_material = types.ReplyKeyboardMarkup(
                                                        resize_keyboard=True)
                                                    button1 = types.KeyboardButton("Венге")
                                                    button2 = types.KeyboardButton("Клен")
                                                    button3 = types.KeyboardButton("Червоне дерево")
                                                    button4 = types.KeyboardButton("Овангкол")
                                                    keyboard_fretboard_material.add(button1, button2)
                                                    keyboard_fretboard_material.add(button3, button4)
                                                    fretboard_material = bot.send_message(message.chat.id,
                                                                                          "Матеріал грифа",
                                                                                          reply_markup=keyboard_fretboard_material)

                                                    def bass13(message13):
                                                        keyboard_fretboard_pad_material = types.ReplyKeyboardMarkup(
                                                            resize_keyboard=True)
                                                        button1 = types.KeyboardButton("Венге")
                                                        button2 = types.KeyboardButton("Мербау")
                                                        button3 = types.KeyboardButton("Палісандр")
                                                        button4 = types.KeyboardButton("Овангкол")
                                                        button5 = types.KeyboardButton("Чорне дерево")
                                                        button6 = types.KeyboardButton("Ятоба")
                                                        keyboard_fretboard_pad_material.add(button1, button2, button3)
                                                        keyboard_fretboard_pad_material.add(button4, button5, button6)
                                                        fretboard_pad_material = bot.send_message(message.chat.id,
                                                                                                  "Матеріал накладки грифа",
                                                                                                  reply_markup=keyboard_fretboard_pad_material)

                                                        def bass14(message14):
                                                            keyboard_neck_attachment = types.ReplyKeyboardMarkup(
                                                                resize_keyboard=True)
                                                            button1 = types.KeyboardButton("Вклеєний гриф")
                                                            button2 = types.KeyboardButton("Гриф на болтах")
                                                            button3 = types.KeyboardButton("Наскрізний гриф")
                                                            keyboard_neck_attachment.add(button1, button2, button3)
                                                            neck_attachment = bot.send_message(message.chat.id,
                                                                                               "Тип кріплення грифа",
                                                                                               reply_markup=keyboard_neck_attachment)

                                                            def bass15(message15):
                                                                keyboard_bridge = types.ReplyKeyboardMarkup(
                                                                    resize_keyboard=True)
                                                                button1 = types.KeyboardButton("TOM + StopBar")
                                                                button2 = types.KeyboardButton("Тремоло Bigsby")
                                                                button3 = types.KeyboardButton("Тремоло Floyd Rose")
                                                                button4 = types.KeyboardButton("Тремоло Vintage")
                                                                button5 = types.KeyboardButton("Фіксований")
                                                                keyboard_bridge.add(button1, button2, button3)
                                                                keyboard_bridge.add(button4, button5)
                                                                bridge = bot.send_message(message.chat.id,
                                                                                          "Вкажіть тип бріджа",
                                                                                          reply_markup=keyboard_bridge)

                                                                def bass16(message16):
                                                                    pickups = bot.send_message(message.chat.id,
                                                                                               "Звукознімачі",
                                                                                               reply_markup=types.ReplyKeyboardRemove())

                                                                    def bass17(message17):
                                                                        pegs = bot.send_message(message.chat.id,
                                                                                                "Кілки")

                                                                        def bass18(message18):
                                                                            country = bot.send_message(
                                                                                message.chat.id,
                                                                                "Вкажіть країну-виробника")

                                                                            def bass19(message19):
                                                                                description = bot.send_message(
                                                                                    message.chat.id,
                                                                                    "Введіть опис")

                                                                                def bass20(message20):
                                                                                    images = bot.send_message(
                                                                                        message.chat.id,
                                                                                        "Вставте зображення (обов'язково зі стисненням і групуванням)")

                                                                                    today = date.today()
                                                                                    data = {
                                                                                        'type': "Bass",
                                                                                        'prod_name': message1.text,
                                                                                        'model': message2.text,
                                                                                        'date_add': today,
                                                                                        'prod_price': message3.text,
                                                                                        'discount': message4.text,
                                                                                        'present': message5.text,
                                                                                        'color': message7.text,
                                                                                        'body_material': message8.text,
                                                                                        'scale': message9.text,
                                                                                        'strings': message10.text,
                                                                                        'default_strings': message11.text,
                                                                                        'frets': message12.text,
                                                                                        'fretboard_material': message13.text,
                                                                                        'fretboard_pad_material': message14.text,
                                                                                        'neck_attachment': message15.text,
                                                                                        'bridge': message16.text,
                                                                                        'pickups': message17.text,
                                                                                        'pegs': message18.text,
                                                                                        'country': message19.text,
                                                                                        'description': message20.text, }
                                                                                    requests.post(
                                                                                        url=f"http://127.0.0.1:8000/main/guitars/",
                                                                                        data=data)

                                                                                    @bot.message_handler(
                                                                                        content_types=['photo'])
                                                                                    def guitar_images(message):
                                                                                        file_info = bot.get_file(
                                                                                            message.photo[
                                                                                                len(message.photo) - 1].file_id)
                                                                                        downloaded_file = bot.download_file(
                                                                                            file_info.file_path)
                                                                                        src = '/Diploma/img/' + \
                                                                                              message.photo[
                                                                                                  1].file_id + ".png"
                                                                                        with open(src,
                                                                                                  'wb') as new_file:
                                                                                            new_file.write(
                                                                                                downloaded_file)
                                                                                        with open(src,
                                                                                                  'rb') as photo:
                                                                                            photo_read = photo.read()
                                                                                            photo_64_encoded = base64.b64encode(
                                                                                                photo_read)

                                                                                        url = "http://127.0.0.1:8000/main/guitars/"
                                                                                        json_list = requests.get(
                                                                                            url).json()

                                                                                        object_id = 0
                                                                                        for i in json_list:
                                                                                            if i["model"] == f"{message2.text}":
                                                                                                object_id += i["id"]
                                                                                                break

                                                                                        data = {
                                                                                            'item_name': object_id,
                                                                                            'image': photo_64_encoded}
                                                                                        requests.post(
                                                                                            url=f"http://127.0.0.1:8000/main/guitar-img/",
                                                                                            data=data)


                                                                                    bot.register_next_step_handler(
                                                                                        images, guitar_images)

                                                                                bot.register_next_step_handler(
                                                                                    description, bass20)

                                                                            bot.register_next_step_handler(country,
                                                                                                           bass19)

                                                                        bot.register_next_step_handler(pegs,
                                                                                                       bass18)

                                                                    bot.register_next_step_handler(pickups,
                                                                                                   bass17)

                                                                bot.register_next_step_handler(bridge, bass16)

                                                            bot.register_next_step_handler(neck_attachment,
                                                                                           bass15)

                                                        bot.register_next_step_handler(fretboard_pad_material,
                                                                                       bass14)

                                                    bot.register_next_step_handler(fretboard_material, bass13)

                                                bot.register_next_step_handler(frets, bass12)

                                            bot.register_next_step_handler(default_strings, bass11)

                                        bot.register_next_step_handler(strings, bass10)

                                    bot.register_next_step_handler(scale, bass9)

                                bot.register_next_step_handler(body_material, bass8)

                            bot.register_next_step_handler(color, bass7)

                        bot.register_next_step_handler(present, bass5)

                    bot.register_next_step_handler(discount, bass4)

                bot.register_next_step_handler(price, bass3)

            bot.register_next_step_handler(model_name, bass2)

        def delete_guitar1(message1):
            model_name = bot.send_message(message.chat.id, "Введіть назву моделі",
                                          reply_markup=types.ReplyKeyboardRemove())

            def delete_guitar2(message2):
                url = "http://127.0.0.1:8000/main/guitar/"
                json_list = requests.get(
                    url).json()

                object_id = 0
                for i in json_list:
                    if i["model"] == f"{message2.text}" and i["prod_name"] == f"{message1.text}":
                        object_id += i["id"]
                        break
                requests.delete(url=f"http://127.0.0.1:8000/main/guitar/{object_id}/")

                bot.send_message(message.chat.id, "Видалено",
                                 reply_markup=keyboard)

            bot.register_next_step_handler(model_name, delete_guitar2)
        bot.register_next_step_handler(bass_moderate, bass_func)

    elif message.text == "Додати новину":
        url_new = "http://127.0.0.1:8000/main/news/"
        json_new_list = requests.get(url_new).json()

        new_name = bot.send_message(message.chat.id, "Введіть назву новини", reply_markup=types.ReplyKeyboardRemove())

        def new1(message1):
            content = bot.send_message(message.chat.id, "Введіть вміст(контент) новини",
                                       reply_markup=types.ReplyKeyboardRemove())

            def new2(message2):
                image = bot.send_message(message.chat.id, "Надішліть головне зображення",
                                         reply_markup=types.ReplyKeyboardRemove())

                @bot.message_handler(content_types=['photo'])
                def photo_db_reformat(message):
                    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
                    downloaded_file = bot.download_file(file_info.file_path)
                    src = '/Diploma/img/' + message.photo[1].file_id + ".png"
                    with open(src, 'wb') as new_file:
                        new_file.write(downloaded_file)
                    with open(src, 'rb') as photo:
                        photo_read = photo.read()
                        photo_64_encoded = base64.b64encode(photo_read)

                    today = date.today()
                    data = {'new_name': message1.text,
                            'content': message2.text,
                            'date_add': today,
                            'image': photo_64_encoded}
                    requests.post(url=f"http://127.0.0.1:8000/main/news/", data=data)

                    bot.send_message(message.chat.id, "Новину додано", reply_markup=keyboard)

                bot.register_next_step_handler(image, photo_db_reformat)

            bot.register_next_step_handler(content, new2)

        bot.register_next_step_handler(new_name, new1)

    elif message.text == "Додати відео":
        link = bot.send_message(message.chat.id, "Вставте посилання на відео:")

        def check_video(message):
            url_video = "http://127.0.0.1:8000/main/videos/"
            json_video_list = requests.get(url_video).json()
            counter = 0
            for i in json_video_list:
                if i['link'] == message.text:
                    counter += 1
            if counter >= 1:
                bot.send_message(message.chat.id, "Відео вже є у базі", reply_markup=keyboard)
            else:
                data = {'link': message.text}
                requests.post(url=f"http://127.0.0.1:8000/main/videos/", data=data)
                bot.send_message(message.chat.id, "Відео додано", reply_markup=keyboard)

        bot.register_next_step_handler(link, check_video)
    else:
        bot.send_message(message.chat.id,
                         "Команда не розпізнана! Використовуйте клавіатуру команд нижче!", reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
