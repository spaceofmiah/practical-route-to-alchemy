from db.scripts import queries as q, items_el




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
    # q.show_all_tables()
    # items_el.DML.add_item(name="Potatoes", category="Meal")
    # items_el.DML.add_item(name="Tuna", category="Grocery")
    # items_el.DML.add_item(name="PS 5", category="Game")
    # items_el.DML.add_items(
    #     payload=[
    #         {'name': 'Addidas ZX 22 Boost', 'category': 'Shoe'},
    #         {'name': 'Nike Revolution', 'category': 'Shoe'},
    #         {'name': 'NK Force Dunk', 'category': 'Shoe'},
    #         {'name': 'Nike Air', 'category': 'Shoe'},
    #     ]
    # )
    # items_el.DML.delete_item(item_id=19)
    # items_el.DML.delete_many_items_by_id([19, 20, 21, 22, 23])
    # items_el.DML.update_item(item_id=12, data={'category': 'Shoe'})
    results = items_el.DQL.retrieve_all_items()
    print("\n\n")
    for i in results:
        print("{id}) {name:<30s} {category}".format(
                id=i['id'],
                name=i['name'], 
                category=i['category']
            )
        )
    print("\n\n")

    print(items_el.DQL.retrieve_item_by_id(17).fetchall())

        
