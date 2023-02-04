import psycopg2
from config import Config
# from sqlalchemy import create_engine
# engine = create_engine(f'postgresql://{Config().db_config()["user"]}:{Config().db_config()["password"]}@{Config().db_config()["host"]}/{Config().db_config()["database"]}')


class ConnectDB:
    def __init__(self):
        config = Config()
        db_config = config.db_config()
        self.host = db_config["host"]
        self.database = db_config["database"]
        self.user = db_config["user"]
        self.password = db_config["password"]
        self.db_name = db_config["db_name"]

    def write_db(self, note):
        conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO {self.db_name} (text) VALUES ('{note}')")
        conn.commit()
        conn.close()

    def read_db_full(self):
        conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.db_name}")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def read_db(self):
        conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        cursor = conn.cursor()
        cursor.execute(f"SELECT text FROM {self.db_name}")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def tg_token(self):
        config = Config()
        return config.telegram_config()
