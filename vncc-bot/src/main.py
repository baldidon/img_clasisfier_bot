import os
from PIL import Image
import requests
from dotenv import load_dotenv
from bot import Bot
import json


load_dotenv()
bot = Bot(os.environ.get('API_KEY'))

inference_endpoint = 'http://model:8080/predictions/densenet'  # obv is a post!
photo_session = list()

@bot.message_handler(commands=['start'])
def startup(message):
    bot.send_message(message.from_user.id,
                        "Welcome! I'm an image classifier! Give me an image and i'll try to classify it 😎")
    bot.send_message(message.from_user.id, "Let's go. Upload an image😎!")


@bot.message_handler(content_types=['photo'])
def get_images(message):
    bot.increment_counter()
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(bot.token, file_info.file_path))
    file_name = f'queries/photo_{bot.counter}.jpg'
    photo_session.append(file_name)
    with open(f'{file_name}', 'wb') as f:
        f.write(file.content)
    f.close()
    bot.send_message(message.from_user.id, "Let me think...")
    output = get_prediction(file_name)
    top_class = list(output.keys())[0]
    top_accuracy = output[list(output.keys())[0]]
    bot.send_message(message.from_user.id, f"It's a {top_class}  With accuracy of {top_accuracy*100}%!")

    bot.send_message(message.from_user.id, f"top 5 class prediction \n{list(output.keys())}")
    bot.send_message(message.from_user.id, "Let's go. Upload another image😎!")

def get_prediction(file_name):
    Image.open(file_name).resize((224,224)).save(file_name)
    predictions = requests.post(inference_endpoint,
                                files={'data': open(file_name, 'rb')}).text
    os.remove(file_name)
    predictions = json.loads(predictions)
    return predictions

bot.polling()

