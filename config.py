from yaml import load, CLoader as Loader


class Config:
    def __init__(self, file: str = "config.yaml"):
        self.file = file

    def telegram_config(self) -> None:
        try:
            with open(self.file, "r") as f:
                config = load(f, Loader=Loader)
                return config["telegram"]["token"]
        except FileNotFoundError:
            print("File not found")
            return None

    def db_config(self) -> None:
        try:
            with open(self.file, "r") as f:
                config = load(f, Loader=Loader)
                return config["db"]
        except FileNotFoundError:
            print("File not found")
            return None


# host = "127.0.0.1"
# database = "postgres"
# user = "postgres"
# password = "1984"
# db_name = "notes"
