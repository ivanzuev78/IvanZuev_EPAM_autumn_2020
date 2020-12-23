import os
import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str):
        if not os.path.isfile(database_name):
            raise FileNotFoundError("No such database")
        self.database_name = database_name

        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
        except sqlite3.OperationalError:
            raise AttributeError(f"No such table {table_name} in database")

        self.table_name = table_name
        self.conn.close()

    def __connect(self):
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()

    def __close_connection(self):
        self.conn.close()

    def __getitem__(self, item):
        self.__connect()
        data = self.cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        ).fetchone()
        names_field = map(lambda x: x[0], self.cursor.description)
        self.__close_connection()
        if data is not None:
            return {field: field_data for field, field_data in zip(names_field, data)}
        return None

    def __iter__(self):
        self.__connect()
        data = self.cursor.execute(f"SELECT * from {self.table_name}")
        names_field = list(map(lambda x: x[0], self.cursor.description))
        data_to_send = data.fetchone()
        while data_to_send:
            next_data_to_send = {
                name: data for name, data in zip(names_field, data_to_send)
            }
            data_to_send = data.fetchone()
            yield next_data_to_send

        self.__close_connection()

    def __len__(self):
        self.__connect()
        len_value = self.cursor.execute(
            f"SELECT Count(*) FROM {self.table_name}"
        ).fetchone()[0]
        self.__close_connection()
        return len_value

    def __contains__(self, item):
        if self.__getitem__(item) is not None:
            return True
        return False
