import telebot
from keyboard import phone_number, laptops, payment
from parsing_laptop import data_Base
from parsing_office_technique import technique_Base
from monitor_parsing import monitor_Base
from program_parsing import program_Base
from accessory_parsing import accessory_Base
from gadgets_parsing import gadgets_Base
from complects_parsing import complects_Base


token = "6766087680:AAF4ZnogYOe7hJCVlQsWJ6zLBtzfSJVrhuI"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    username = message.from_user.username
    bot.send_message(chat_id, f"Hello {first_name} {last_name}"
        f"\nYour id: {user_id}\nUsername: {username}", reply_markup=phone_number())
    bot.register_next_step_handler(message, get_phone_number)

def get_phone_number(message):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number
    bot.send_message(chat_id, f"Your number: {phone_number}\n"
                              f"Choose one of them!", reply_markup=laptops())
    bot.register_next_step_handler(message, laptop)

@bot.message_handler(func=lambda message: message.text == "Notebook")
def laptop(message):
    chat_id = message.chat.id
    for parsed_notebooks in data_Base:
        product_name = parsed_notebooks["Product_name"]
        product_price = parsed_notebooks["Product_price"]
        product_image = parsed_notebooks["Product_image"]

        bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
            reply_markup=payment("https://ultrashop.uz/ru/store/noutbuki"))



@bot.message_handler(func=lambda message: message.text == "Office Tech")
def technique(message):
    chat_id = message.chat.id
    for technique in technique_Base:
        technique_name = technique["Technique_name"]
        technique_price = technique["Technique_price"]
        technique_image = technique["Technique_image"]
        bot.send_photo(chat_id, technique_image, caption=f"Name: {technique_name}\nPrice: {technique_price}",
                   reply_markup=payment("https://ultrashop.uz/ru/store/pechatnaya-tehnika"))




@bot.message_handler(func=lambda message: message.text == "Monitor")
def monitor(message):
    chat_id = message.chat.id
    for monitor in monitor_Base:
        product_name = monitor["Product_name"]
        product_price = monitor["Product_price"]
        product_image = monitor["Product_image"]
        bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                   reply_markup=payment("https://ultrashop.uz/ru/store/monitory"))



@bot.message_handler(func=lambda message: message.text == "Program")
def pg_parsing(message):
    chat_id = message.chat.id
    for program in program_Base:
        product_name = program["Product_name"]
        product_price = program["Product_price"]
        product_image = program["Product_image"]
        bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                   reply_markup=payment("https://ultrashop.uz/ru/store/programmy"))



@bot.message_handler(func=lambda message: message.text == "Program")
def access_parsing(message):
    chat_id = message.chat.id
    for accessory in accessory_Base:
        product_name = accessory["Product_name"]
        product_price = accessory["Product_price"]
        product_image = accessory["Product_image"]
        bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                   reply_markup=payment("https://ultrashop.uz/ru/store/aksessuary"))



@bot.message_handler(func=lambda message: message.text == "Program")
def gadget_parsing(message):
    chat_id = message.chat.id
    for gadget in gadgets_Base:
        product_name = gadget["Product_name"]
        product_price = gadget["Product_price"]
        product_image = gadget["Product_image"]
        bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                   reply_markup=payment("https://ultrashop.uz/ru/store/aksessuary"))


@bot.message_handler(func=lambda message: message.text == "Program")
def complect(message):
    chat_id = message.chat.id
    for complect in complects_Base:
        product_name = complect["Product_name"]
        product_price = complect["Product_price"]
        product_image = complect["Product_image"]
        bot.send_photo(chat_id, product_image, caption=f"Name: {product_name}\nPrice: {product_price}",
                       reply_markup=payment("https://ultrashop.uz/ru/store/komplektuyushie"))
bot.polling(none_stop=True)

