import os
import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str):
        if not os.path.isfile(database_name):
            raise FileNotFoundError("No such database")
        self.database_name = database_name

        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

        if table_name not in map(
            lambda x: x[0],
            self.cursor.execute(
                "SELECT name FROM sqlite_master " "WHERE type='table';"
            ),
        ):

            self.conn.close()
            raise AttributeError(f"No such table {table_name} in database")

        self.table_name = table_name

    def __getitem__(self, item):
        data = self.cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        ).fetchone()
        names_field = list(map(lambda x: x[0], self.cursor.description))
        if data is not None:
            return {field: field_data for field, field_data in zip(names_field, data)}
        return None

    def __iter__(self):
        data = self.cursor.execute(f"SELECT * from {self.table_name}")
        names_field = list(map(lambda x: x[0], self.cursor.description))

        while data_to_send := data.fetchone():
            yield {names_field[i]: data_to_send[i] for i in range(len(names_field))}

    def __len__(self):
        return self.cursor.execute(
            f"SELECT Count(*) FROM {self.table_name}"
        ).fetchone()[0]

    def __contains__(self, item):
        if self.__getitem__(item) is not None:
            return True
        return False
