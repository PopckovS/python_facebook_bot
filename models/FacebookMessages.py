# from flaskDB import db
from app import db
from datetime import datetime


class FacebookMessages(db.Model):
    '''Модель для работы с таблицей Facebook_Messages
    Сохраняет все сообщения как от пользователя так и от бота.'''

    __tablename__ = 'Facebook_Messages'

    id = db.Column(db.Integer(), primary_key=True)
    senderID = db.Column(db.Integer(), nullable=False)
    recipientID = db.Column(db.Integer(), nullable=False)
    message = db.Column(db.Text(), nullable=False)
    messageID = db.Column(db.Integer(), nullable=False)

    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)


    def __repr__(self):
        '''Возвращает все поля текущего обьекта.'''
        return "id={}\n" \
               "senderID={}\n" \
               "recipientID={}\n" \
               "message={}\n" \
               "messageID={}\n" \
               "created_on={}\n" \
               "updated_on={}".format(
            self.id,
            self.senderID,
            self.recipientID,
            self.message,
            self.messageID,
            self.created_on,
            self.updated_on
        )