from typing import List, Any, Dict

from sqlalchemy import text
from db.core.initializer import create_connection



def create_item_table():
    """Creates Item table.

    col: id              Unique identifier - primary key.
    col: timestamp       datetime defualts to current 
                         date and time the item is tracked.
    col: name            Name of item - field is required.
    col: category        Category of the tracked item
    """
    # Creates a connection to the database
    with create_connection() as conn:
        # Utilizes connection instance to execute SQL query 
        conn.execute(
            text(
                '''
                CREATE TABLE Item (
                    id              SERIAL PRIMARY KEY,
                    date_tracked    TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    name            VARCHAR(250) NOT NULL,
                    category        VARCHAR(200)
                )
                '''
            )
        )

        # Sends the query to the database
        conn.commit()


def show_all_tables():
    """Show all available tables in the database
    
    Returned tables excludes those having their
    schema as `pg_catalog` and `information_schema`.
    """
    with create_connection() as conn:
        results = conn.execute(
            text(
                '''
                SELECT * FROM pg_catalog.pg_tables
                WHERE schemaname != 'pg_catalog' 
                AND schemaname != 'information_schema';
                '''
            )
        )

        for data in results:
            print(f"{data[1]} Table".title())


def rename_item_table(old_table_name:str, new_table_name:str):
    """Rename Item table if it exists in the database"""
    with create_connection() as conn:
        conn.execute(
            text(
                f'''
                ALTER TABLE {old_table_name}
                RENAME TO {new_table_name}
                '''
            )
        )

        conn.commit()


def create_craved_item_table():
    """Create CravedItem table.

    This table keeps tracks of items that are craved for

    col: id              Unique identifier - primary key.
    col: item_id         Item unique identifier - field is
                         required.
    col: date_tracked    datetime defualts to current 
                         date and time the item is tracked.
    col: is_satisfied    Denotes either or not craved item
                         has been satisfied.
    """
    # Creates a connection to the database
    with create_connection() as conn:
        # Utilizes connection instance to execute SQL query 
        conn.execute(
            text(
                '''
                CREATE TABLE CravedItem (
                    id              SERIAL      PRIMARY KEY,
                    item_id         INT         NOT NULL,
                    date_tracked    TIMESTAMP   DEFAULT CURRENT_TIMESTAMP,
                    is_satisfied    BOOLEAN     DEFAULT False,
                    CONSTRAINT      fk_item     FOREIGN KEY(item_id) REFERENCES Item(id)
                )
                '''
            )
        )

        # Sends the query to the database
        conn.commit()


def drop_item_table():
    """Delete Item table"""
    with create_connection() as conn:
        conn.execute(text("DROP TABLE Item CASCADE"))
        conn.commit()


def drop_craved_item_table():
    """Delete CravedItem table"""
    with create_connection() as conn:
        conn.execute(text("DROP TABLE CravedItem"))
        conn.commit()


def insert_item(name:str, category:str):
    """Inserts new record into Item table

    param: name [str] Represents an item name to be added
    param: category [str] Represents an item category
    """
    with create_connection() as conn:
        conn.execute(
            text("INSERT INTO Item (name, category) VALUES (:name, :category)"),
            {'name':name, 'category':category}
        )
        conn.commit()


def insert_multiple_items(data:List[Dict[str, Any]]):
    """Allows insertion of multiple records into Item table

    param: data [List] sequence of dictionary where each 
           dictionary represents a record to be added to 
           the db
    """
    with create_connection() as conn:
        conn.execute(
            text("INSERT INTO Item (name, category) VALUES (:name, :category)"),
            data
        )
        conn.commit()


def retrieve_all_item():
    """Retrieves all records from Item table"""
    with create_connection() as conn:
        results = conn.execute(
            text("SELECT * FROM Item")
        )

        for result in results:
            print(result)