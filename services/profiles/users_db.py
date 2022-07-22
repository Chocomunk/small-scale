import sqlalchemy as sql
from typing import Any, Dict, Optional, Tuple
from abc import ABC, abstractclassmethod


class SQLInterface(ABC):

    @abstractclassmethod
    def get_table(self, tablename: str) -> sql.Table:
        pass

    @abstractclassmethod
    def execute(self, query: str, params: Optional[Tuple]=None) \
        -> Tuple[Tuple[Dict[str, Any], ...], int]:
        pass


class MYSQLInterface(SQLInterface):

    def __init__(self, host, user, password, database) -> None:
        super().__init__()
        url = f"mysql+pymysql://{user}:{password}@{host}/{database}"
        self.db = sql.create_engine(url)
        self.connection = self.db.connect()
        self.meta = sql.MetaData()

    def get_table(self, tablename):
        return sql.Table(tablename, self.meta, autoload=True, autoload_with=self.db)

    def execute(self, query, params=None):
        result = None, None
        exc = self.connection.execute(query, params)
        result = exc.fetchall(), exc.rowcount
        return result


# Abstraction layer so that the DB could be swapped out with any SQL-compliant
# DB if we wanted.
def get_users_db(host, user, password, database) -> SQLInterface:
    return MYSQLInterface(
        host=host,
        user=user,
        password=password,
        database=database,
    )
