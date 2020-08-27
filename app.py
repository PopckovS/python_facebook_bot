#! /usr/bin/python3
# Указываем Shebang на случай если будем запускать приложениене не из виртуального окружения

import requests
import json

import config
from config import trace

from flask import Flask, url_for, request, render_template, \
    redirect, abort, flash, make_response
from flask_sqlalchemy import SQLAlchemy

import start


start.server_start()

app = Flask(__name__)
app.secret_key = 'some_secret'

app.config['SQLALCHEMY_DATABASE_URI'] = config.CONNECT_DB

# Создаем подключение к БД
# db = SQLAlchemy(app)
# db.create_all()


@app.route('/', methods=['GET'])
def verify_for_facebook_webhook():
    """Аутентификация с API FaceBook, происходит 1-ед раз при
    установке WebHook, данный метод отвечает на него при GET запросе.
    При создании WebHook приходит запрос типа GET на указанный в настройках профиля адрес
    предоставляя токен в параетре hub.verify_token таким образом мы устанавливаем аутентификацию.
    Но Flask запущен на локалке а не в сети, так что его нкельзя установить ка WebHook, тут то
    в игру и вступает утилита ngrok/localtunnel которая расшарит локальный сайт, идаст ему доступ в Сеть."""

    if request.args.get('hub.verify_token', '') == config.FACEBOOK_API_KEY:
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print('wrong verification token')
    return 'Hello World !'


@app.route('/', methods=['POST'])
def index_action_for_facebook_post_request():
    """Реагирует на входящий запрос типа POST, и прсото дублирует и возвращает его обратно."""
    if request.get_json():
        data = request.get_json()
        trace(data)
        entry = data['entry'][0]

        if entry.get("messaging"):
            messaging_event = entry['messaging'][0]
            sender_id = messaging_event['sender']['id']
            message_text = messaging_event['message']['text']

            send_text_message(sender_id, message_text)
            send_gif_message(sender_id, message_text)

    return "Hello World!"


def send_text_message(recipient_id, message):
    """Метод отправки текстовых сообщений пользователю через API FaceBook."""

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


def send_gif_message(recipient_id, message):
    """Метод генерирует запрос POST запрос к API FaceBook
    и отправляет пользователю гифку, на тему введенную пользователем."""

    gif_url = search_gif(message)

    data = json.dumps({
        "recipient": {"id": recipient_id},
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": gif_url
                }
            }}
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


def search_gif(text):
    """Метод делает GET запрос к сервису GIPHY
    и получает gif на заданную тему."""

    payload = {'s': text, 'api_key': config.GIPHY_API_KEY}
    response = requests.get('http://api.giphy.com/v1/gifs/translate', params=payload)
    response_json = response.json()
    gif_url = response_json['data']['images']['original']['url']

    trace(response_json)
    trace(gif_url)

    return gif_url


if __name__ == '__main__':
    """Запускаем работу сервера Flask"""
    app.run(debug=True, port=config.SERVER_PORT)

