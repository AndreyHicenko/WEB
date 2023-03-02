# from flask import app
from flask import Flask
# import sqlalchemy
# from sqlalchemy import orm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    session = db_session.create_session()

    user = User()
    user.surname = 'Домнич'
    user.name = 'Алексей'
    user.age = 42
    user.position = 'coptain'
    user.speciality = 'director'
    user.address = "module_1"
    user.email = "domnich@gpk.org"
    user.hashed_password = "cap"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = 'Иванов'
    user.name = 'Алексей'
    user.age = 58
    user.position = 'ingener'
    user.speciality = 'builder'
    user.address = "module_2"
    user.email = "ingener@gpk.org"
    user.hashed_password = "ing"
    user.set_password(user.hashed_password)
    session.add(user)
    # app.run()

    user = User()
    user.surname = 'Карло'
    user.name = 'Папа'
    user.age = 55
    user.position = 'pilot'
    user.speciality = 'voditel'
    user.address = "module_2"
    user.email = "voditel_karlo@gpk.org"
    user.hashed_password = "vod"
    user.set_password(user.hashed_password)
    session.add(user)

    user = User()
    user.surname = 'Алексеев'
    user.name = 'Александр'
    user.age = 29
    user.position = 'it_speciality'
    user.speciality = 'programmer'
    user.address = "module_2"
    user.email = "prog@gpk.org"
    user.hashed_password = "prroger"
    user.set_password(user.hashed_password)
    session.add(user)
    session.commit()

if __name__ == '__main__':
    main()
