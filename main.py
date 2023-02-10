import requests
import os
import time
import database
import json

token = os.environ['TOKEN']
url = f'https://api.telegram.org/bot{token}'


def get_updates():
    url_updates = url + '/getUpdates'
    r = requests.get(url_updates)
    return r.json()

def counter():
    try:
        url_send = url + '/sendMessage'
        last_update_id = get_updates()['result'][-1]['update_id']
        while True:
            updated = get_updates()
            print('metka1')
            if last_update_id != updated['result'][-1]['update_id']:
                last_update_id = updated['result'][-1]['update_id']
                text = updated['result'][-1]['message']['text']
                chat_id = updated['result'][-1]['message']['chat']['id']
                print('metka2')
                # print(type(database.get()))
                # print('metka3')
                if text == '/start':
                    data = json.loads(database.get())
                    payload = {'chat_id': chat_id, 'text': f"Likes : {data['like']}\nDislikes : {data['dislike']}"}
                    requests.post(url_send, params=payload)
                elif text == 'like':
                    database.update('like')
                    print('metka4')
                    # print(type(data))
                    # print(data)
                    data = json.loads(database.get())
                    payload = {'chat_id': chat_id, 'text': f"Likes : {data['like']}\nDislikes : {data['dislike']}"}
                    requests.post(url_send, params=payload)
                elif text == 'dislike':
                    database.update('dislike')
                    data = json.loads(database.get())
                    payload = {'chat_id': chat_id, 'text': f"Likes : {data['like']}\nDislikes : {data['dislike']}"}
                    requests.post(url_send, params=payload)
                else:
                    payload = {'chat_id': chat_id, 'text': 'Please, type like or dislike'}
                    requests.post(url_send, params=payload)
            time.sleep(2)
    except:
        print('Something went wrong')
        counter()


# def like_button():

#     inline_keyboard = [
#         [
#             InlineKeyboardButton("Like", callback_data='like'),
#             InlineKeyboardButton("Dislike", callback_data='dislike')
#         ]
#     ]
#     reply_markup = InlineKeyboardMarkup(inline_keyboard)


if __name__ == '__main__':
    database.init()
    counter()