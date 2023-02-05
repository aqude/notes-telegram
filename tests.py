from config import Config
from sqlalchemy import create_engine

engine = create_engine(
    f'postgresql://{Config().db_config()["user"]}:{Config().db_config()["password"]}@{Config().db_config()["host"]}/{Config().db_config()["database"]}')
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


class Notes(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    text = Column(String)
    date = Column(String)

    # text
    def __repr__(self):
        return f"{self.text}"

    # date + text
    def __str__(self):
        return f"{self.date} {self.text}"


def tg_token():
    return Config().telegram_config()


class ConnectDB:
    def __init__(self):
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def write_db(self, note):
        self.session.add(Notes(text=note))
        self.session.commit()

    def read_db(self, date=None):
        notes = self.session.query(Notes).all()
        notes = [note.text for note in notes]
        # конвертируем в строку
        notes = '\n'.join(notes)
        return notes

db = ConnectDB()
print(db.read_db())