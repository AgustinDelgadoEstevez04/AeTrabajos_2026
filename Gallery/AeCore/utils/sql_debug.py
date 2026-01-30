from PySide6.QtSql import QSqlQuery, QSqlError

def debug_query(query: QSqlQuery):
    if query.lastError().type() == QSqlError.ErrorType.NoError:
        print(f"Query OK: {query.lastQuery()}")
    else:
        print(f"Query KO: {query.lastError().text()}")
        print(f"Query text: {query.lastQuery()}")
