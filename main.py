from src.basic import run_db_select_statement
from db.scripts.queries import (
    create_item_table, 
    drop_item_table, 

    create_craved_item_table,
    drop_craved_item_table
)

if __name__ == "__main__":
    create_item_table()
        
