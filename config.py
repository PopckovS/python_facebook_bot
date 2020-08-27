
def trace(object):
    """Метод отладчик,выводит информацию в терминале."""
    print('============')
    print(object)
    print('============')


# Название профиля
FACEBOOK_DEVELOPER_NAME = "Mitbot"

# ID профиля
FACEBOOK_APP_ID = "3811445255536797"

# Адрес по которому можно найти Бота в Соц Сети
FACEBOOK_URL_BOT = "MitBot-100801378426813"

# URL Ссылка на мессенджер в FaceBook
FACEBOOK_URL_ME_BOT = "m.me/100801378426813"

# Секретный ключ API для доступа к Чат Боту
FACEBOOK_API_KEY = ""

# Секретный ключ API для доступа к https://developers.giphy.com
GIPHY_API_KEY = ""

# Название приложения на сайте Giphy
GIPHY_APPLICATION_NAME = "SuperAgression"

# Порт на котором мы будем запускать наш сервер Flask
SERVER_PORT = 5000

# Статичное Имя Домена, для WebHook от FaceBook
SERVER_URL = "https://sergio-fb-bot.serverless.social"

# Команда для CLI терминала, чтобы расшарить локальный хост сервера, для доступа FaceBook Api Key
SERVER_START_COMMAND_FOR_CLI = "lt -h http://serverless.social --subdomain sergio-fb-bot -p 5000"

# ID страницы бота в FaceBook
BOT_ID = "100801378426813"

# Название Бота
# BOT_NAME = "MitBot"
BOT_NAME = "MitBotTest"

# Дравйер импользуемый для работы с БД
DB_SUBD = "mysql+pymysql"

# Имя пользователя для БД
DB_USERNAME = ""

# Пароль для входа в БД
DB_PASSWORD = "11"

# База данный с которой будем работать
DB_NAME = "facebook"

# Хост подключения к БД
DB_HOST = "localhost"

# Параметры подключения к БД
CONNECT_DB = DB_SUBD + "://" + DB_USERNAME + ":" + DB_PASSWORD + "@" + "/" + DB_NAME







