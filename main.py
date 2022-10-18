from src.basic import run_db_select_statement
from db.scripts.queries import (
    create_item_table, 
    drop_item_table, 
    show_all_tables,
    rename_item_table,
    insert_item,
    retrieve_all_item,
    insert_multiple_items,
    update_existing_item_name,

    create_craved_item_table,
    drop_craved_item_table
)

if __name__ == "__main__":
    # create_item_table()
    # create_craved_item_table()
    # show_all_tables()
    # rename_item_table('Commodity', 'Item')
    # drop_item_table()
    # drop_craved_item_table()
    # show_all_tables()
    # insert_item(name="Tesla Model S", category="Auto")
    # insert_multiple_items([
    #     {
    #         'name': 'Iphone 14 Pro Max',   
    #         'category': 'mobile'
    #     },
    #     {
    #         'name': 'Pizza',
    #         'category': 'meal'
    #     }
    # ])
    update_existing_item_name(item_id=1, new_value="Tesla Starlink")
    retrieve_all_item()

        
