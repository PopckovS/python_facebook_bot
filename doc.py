"""


Активировать в виртуальное окружение, локальной среды для проекта на Python:
    source venv/bin/activate
Подробнее тут - https://python-scripts.com/virtualenv


/*=========================== Создание FaceBook бота ==================================*/

FaceBook выдает секретный API_KEY для авторизации, и требует установку WebHook.
WebHook - устанавливается только на 1-ед URL адрес, при аутентификации FB отправляет
http GET на указанный WebHook, в параетре "hub.verify_token" который требуется сравнить с
API_KEY которыйы получили на сайте самого FB. И в случае успешной проверки вернуть FB
строку = "hub.challenge".

1) ngrok
WebHook устанавливается только на 1-ед. URL адрес, так что возникает вопрос
как открыть свой сайт в Сеть, чтобы он был доступен для http GET запроса, обычно
для этого используется программа ngrok, но она каждый раз устанавливает случайный адрес.
    По мимо этого у ngrok есть возможность устанавливать нужный URL для сайта,
при помощи команды:
    ngrok http 80 -subdomain yoursubdomain.ngrok.io
    Где yoursubdomain должен быть уникальным адресом, и оканчиваться обезательно на .ngrok.io
и все былобы прекрасно еслибы не 1 но! эта услуга платная.

2) localtunnel
Устанавливается через NodeJS так что установим его:

- 1 Способ
    sudo apt install nodejs
    sudo apt install npm

    node -v
    npm -v

- 2 Способ
    Установка програмного обеспечения для NodeJS
        sudo apt install build-essential checkinstall
        sudo apt install libssl-dev
        wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.8/install.sh | bash

    Перезагрузка терминала
        source /etc/profile

    Посмотреть доступные вресии odeJS
        nvm ls-remote

    Установка NodeJS
        nvm install 14.0.0

    Посмотреть текущую версию NodeJS
        node -v

После установки NodeJS установим сам localtunnel след командой
    npm install -g localtunnel
Теперь в нашей системе доступна утилита lt
Расшарим локальный сервер, советуют использовать эту команду, но она не работает
не знаю по чему, терминал прсото виснит: lt --port 5000

Расшарить локальный в Сеть:
    lt -h http://serverless.social -p 5000
В результате мы получим примерно такой ответ(Хост сатйа всегда разный):
    your url is: https://helpless-sloth-7.serverless.social
Устанавливаем дефолтное статичное доменное имя сайта:
Делается это указанием специального параметра:
    --subdomain
! ПРИМЕР ! Использования, запускаем сайт с доменным именем "sergio-popckov-fb-bot"
    Запускаем локальный хост в Сеть:
    lt -h http://serverless.social --subdomain sergio-popckov-fb-bot -p 5000
Получаем ответ:
    your url is: https://sergio-popckov-fb-bot.serverless.social


ПРИМЕР ЗАПРОСА ДЛЯ АУТЕНТИФИК ЧЕРЕЗ WebHook:
    "GET /?hub.mode=subscribe&hub.challenge=492181779&hub.verify_token=EAAnaCwoeFcUBAPaM6idYh
    wN2dmTBkAfuy7HXxmEHrQUhiW5CPaOxBT0vQachor0LM9EQVvmOLuUhagZBW7RR8bZAnNBhX4CBZCFnbLTzjoyxal
    pumK8kaVoID4Rx9ecFuOj5ngnVegrfrgegeevdcCLyZCZBOjosLSRIPPG3VsHl1LRiedC7HhnPZCsZD HTTP/1.1"

ПРИМЕР СООБЩЕНИЯ от пользователя хуком к нашему сервреу:
{
'object': 'page',
'entry':
    [
        {
            'id': '100801378426813',
            'time': 1598466342917,
            'messaging':
            [
                {
                'sender': {'id': '3205832699538232'},
                'recipient': {'id': '100801378426813'},
                'timestamp': 1598466342720,
                'message': {
                            'mid': 'm_hHvy52ucwRaFpGyFp5ZV68bSAG3DEnod7jz1Rgpi8bZjXTWBNOg7wM-sm-KP366eXFZl81wuELzBYafrvZWGdA',
                            'text': 'Hello World 1'
                            }
                }
            ]
        }
    ]
}






"""

