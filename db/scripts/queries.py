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
        conn.execute(text("DROP TABLE Item"))
        conn.commit()


def drop_craved_item_table():
    """Delete CravedItem table"""
    with create_connection() as conn:
        conn.execute(text("DROP TABLE CravedItem"))
        conn.commit()