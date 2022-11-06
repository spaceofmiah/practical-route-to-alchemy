"""
Module contains code to interact with item 
database table model with SQLAlchemy
expression language
"""
from typing import List, Dict
from sqlalchemy import Integer
from sqlalchemy.sql import select, bindparam

from db.core.initializer import engine, create_connection
from db.models.items import table_meta, Item, CravedItem


class DDL:
	"""Encapsulates database definition language (DML)"""

	@staticmethod
	def create_all_tables():
		"""Creates all tables"""
		table_meta.create_all(engine)

	@staticmethod
	def create_item_table_with_core():
		"""Creates item table"""
		Item.create(engine, checkfirst=True)

	@staticmethod
	def create_craveditem_table_with_core():
		"""Creates craved item table"""
		CravedItem.create(engine, checkfirst=True)

	@staticmethod
	def drop_all_tables():
		"""Drop all tables"""
		table_meta.drop_all(engine)

	@staticmethod
	def drop_item():
		"""Drops Item table"""
		Item.drop(engine)

	@staticmethod
	def drop_craveditem():
		"""Drops CravedItem table"""
		CravedItem.drop(engine)


class DQL:
	"""Encapsulates database query language (DML)"""

	@staticmethod
	def retrieve_all_items():
		"""Retrieves all data entries and 
		corresponding columns from Item table.
		"""
		statement = select(Item)
		with create_connection() as conn:
			result = conn.execute(statement)
			return result

	@staticmethod
	def retrieve_item_by_id(id:int):
		"""Retrieves a single item by it's id.
		
		- id <int> A unique identifier of an item.
		"""
		statement = (
			select(Item)
			.where(Item.c.id==bindparam('id', type_=Integer))
		)
		with create_connection() as conn:
			result = conn.execute(statement, {'id': id})
			return result


class DML:
	"""Encapsulates database manipulation language (DML)"""

	@staticmethod
	def add_item(name:str, category:str):
		"""Adds a single item to Item table"""
		statement = Item.insert().values(name=name, category=category)
		with create_connection() as conn:
			result = conn.execute(statement)
			conn.commit()


	@staticmethod
	def add_items(payload:List[Dict[str, str]]):
		"""Inserts multiple items to Item table
		
		- payload <list> new data to be added to
						 Item table. Each dict has
						 key mapped to the Item table
						 and it's corresponding value.
		"""
		with create_connection() as conn:
			conn.execute(Item.insert(), payload)
			conn.commit()

	@staticmethod
	def delete_item(item_id:int):
		"""Deletes an item whose id is passed as a 
		parameter

		- item_id <int> Uniquely identifies an item
						instance
		"""
		with create_connection() as conn:
			statement = Item.delete().where(
				Item.c.id==bindparam('id', type_=Integer)
			)
			conn.execute(statement, {'id': item_id})
			conn.commit()


	@staticmethod
	def delete_many_items_by_id(id:list):
		"""Deletes multiple items with the corresponding
		id
		"""
		with create_connection() as conn:
			statement = Item.delete().where(Item.c.id.in_(ids))
			conn.execute(statement)
			conn.commit()


	@staticmethod
	def update_item(item_id:int, data:Dict[str, str]):
		"""Updates an existing item

		- item_id <int> Uniquely identifies an item
						instance

		- data <dict> 	Key-value pair with column name
						as key and the new entry for 
						column as value.
		"""
		with create_connection() as conn:
			statement=Item.update().where(
				Item.c.id==bindparam('item_id', type_=Integer)
			).values(**data)
			conn.execute(statement, {'item_id': item_id})
			conn.commit()


