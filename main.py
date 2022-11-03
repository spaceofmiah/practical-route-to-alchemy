from src.basic import run_db_select_statement
from db.scripts import queries as q
from db.scripts import items_el

if __name__ == "__main__":
    # q.create_item_table()
    # q.create_craved_item_table()
    # q.show_all_tables()
    # q.rename_item_table('Commodity', 'Item')
    # q.drop_item_table()
    # q.drop_craved_item_table()
    # q.show_all_tables()
    # q.insert_item(name="Tesla Model S", category="Auto")
    # q.insert_multiple_items([
    #     {
    #         'name': 'Iphone 14 Pro Max',   
    #         'category': 'mobile'
    #     },
    #     {
    #         'name': 'Pizza',
    #         'category': 'meal'
    #     }
    # ])
    # q.update_existing_item_name(item_id=1, new_value="Tesla Starlink")
    # q.delete_item(1)
    # q.retrieve_all_item()
    # items_el.DDL.create_all_tables()
    # items_el.DDL.drop_all_tables()
    # items_el.DDL.drop_craveditem()
    # items_el.DDL.drop_item()
    q.show_all_tables()

        
