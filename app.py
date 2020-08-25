#! /usr/bin/python3

import requests
import config
import json

from flask import Flask, url_for, request, render_template, \
    redirect, abort, flash, make_response
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


def trace(object):
    print('============')
    print(object)
    print('============')




@app.route('/', methods=['GET'])
def verify():
    """Аутентификация с API FaceBook"""
    # Once the endpoint is added as a webhook, it must return back
    # the 'hub.challenge' value it receives in the request arguments
    if (request.args.get('hub.verify_token', '') == config.FACEBOOK_API_KEY):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print('wrong verification token')
    return 'Hello World !'




@app.route('/', methods=['POST'])
def index():
    """При создании WebHook приходит запрос типа GET на указанный в настройках профиля адрес
    предоставляя токен в параетре hub.verify_token таким образом мы устанавливаем аутентификацию.
    Но Flask запущен на локалке а не в сети, так что его нкельзя установить ка WebHook, тут то
    в игру и вступает утилита ngrok которая расшарит локальный сайт, идаст ему доступ в Сеть.
    """

    data = request.get_json()
    trace(data)
    entry = data['entry'][0]

    if entry.get("messaging"):
        messaging_event = entry['messaging'][0]
        sender_id = messaging_event['sender']['id']
        message_text = messaging_event['message']['text']
        send_message(sender_id, message_text)

    return "Hello World!"





def send_message(recipient_id, message):
    """Метод отправки Сообщений к API FaceBook"""

    data = json.dumps({
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    })

    params = {
        "access_token": config.FACEBOOK_API_KEY
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://graph.facebook.com/v2.6/me/messages",
        params=params, headers=headers, data=data
    )
    trace(response)





if __name__ == '__main__':
    app.run(debug=True, port=5000)

