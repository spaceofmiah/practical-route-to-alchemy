from sqlalchemy import text
from db.core.initializer import create_connection


def run_db_select_statement():
    with create_connection() as conn:
        result = conn.execute(text("select 'Hello World'"))
        print(result.all())
