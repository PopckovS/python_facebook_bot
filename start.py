import os
from config import SERVER_START_COMMAND_FOR_CLI
import multiprocessing


def sharing_local_host():
    """Выполнение команды как, командв CLi на расшариваение локального хоста в Сеть."""
    os.system(SERVER_START_COMMAND_FOR_CLI)


def server_start():
    """Метод завпускает дочерний процесс на расшаривание локального хостинга в Сеть,
    и не дожидаясь завершения провесса."""

    p1 = multiprocessing.Process(target=sharing_local_host)
    p1.start()
    # эта команд ожидает завершение процесса
    # p1.join()

